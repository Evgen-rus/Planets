"""Offline preparation check. The injected transit is synthetic, not a discovery."""

import importlib
import importlib.metadata
import os
from pathlib import Path
import sys
import tomllib

import numpy as np
from astropy.timeseries import BoxLeastSquares


def main():
    root = Path(__file__).resolve().parents[1]
    os.environ["MPLCONFIGDIR"] = str(root / ".cache" / "matplotlib")
    if sys.version_info[:2] != (3, 11):
        raise RuntimeError("Use the project's Python 3.11 virtual environment")
    for name in ("numpy", "scipy", "astropy", "astroquery", "lightkurve", "matplotlib"):
        importlib.import_module(name)
        print(f"{name}: {importlib.metadata.version(name)}")

    with (root / "config/pilot.toml").open("rb") as handle:
        pilot = tomllib.load(handle)
    assert pilot["stage"] == "prepared"
    assert 20 <= pilot["initial_targets"] <= pilot["maximum_targets"] <= 50
    assert not pilot["claims"]["allow_discovery_claim"]
    assert not pilot["claims"]["allow_uncalibrated_probability"]
    with (root / ".codex/config.toml").open("rb") as handle:
        agents = tomllib.load(handle)["agents"]
    assert agents["default_subagent_model"] == "gpt-6-luna"
    assert agents["max_concurrent_threads_per_session"] == 2
    for name, effort in (("worker-low", "low"), ("worker-xhigh", "xhigh"), ("verifier", "xhigh")):
        with (root / f".codex/agents/{name}.toml").open("rb") as handle:
            agent = tomllib.load(handle)
        assert agent["model"] == "gpt-6-luna"
        assert agent["model_reasoning_effort"] == effort

    rng = np.random.default_rng(pilot["search"]["random_seed"])
    time = np.arange(0.0, 27.0, 10.0 / (24 * 60))
    period, epoch, duration, depth = 3.18, 0.7, 2.0 / 24, 0.0005
    phase = (time - epoch + period / 2) % period - period / 2
    in_transit = np.abs(phase) < duration / 2
    noise_only = 1.0 + rng.normal(0, 0.0001, len(time))
    flux = noise_only.copy()
    flux[in_transit] -= depth
    model = BoxLeastSquares(time, flux, dy=np.full(len(time), 0.0001))
    result = model.autopower(
        np.array(pilot["search"]["duration_hours"]) / 24,
        minimum_period=pilot["search"]["minimum_period_days"],
        maximum_period=pilot["search"]["maximum_period_days"],
    )
    best = int(np.argmax(result.power))
    recovered_period = float(result.period[best])
    recovered_depth = float(result.depth[best])
    assert abs(recovered_period - period) < 0.02, recovered_period
    assert abs(recovered_depth - depth) < depth * 0.25, recovered_depth
    noise_model = BoxLeastSquares(time, noise_only, dy=np.full(len(time), 0.0001))
    noise_result = noise_model.power(result.period, np.array(pilot["search"]["duration_hours"]) / 24)
    assert float(np.max(noise_result.power)) < float(result.power[best]) / 10
    print(f"PASS: synthetic transit recovered at {recovered_period:.5f} d, depth {recovered_depth:.6f}")
    print("PASS: this fixed white-noise control is weaker; no FAP calibration is implied.")
    print("No network queries, real observations, or planet candidates were used.")


if __name__ == "__main__":
    main()

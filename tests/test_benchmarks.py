"""Tests for the benchmark functions."""

import numpy as np
import pytest

from metaheuristics.benchmarks import BENCHMARKS, DIM

SEED = 42
NAMES = list(BENCHMARKS)


@pytest.mark.parametrize("name", NAMES)
def test_zero_at_optimum(name: str) -> None:
    """Each function is (almost) 0 at its known optimum point."""
    info = BENCHMARKS[name]
    x = np.full(DIM, info["optimum_x"])
    assert info["func"](x) == pytest.approx(0.0, abs=1e-12)


@pytest.mark.parametrize("name", NAMES)
def test_positive_at_random_point(name: str) -> None:
    """Each function is positive at a random point inside the bounds."""
    info = BENCHMARKS[name]
    low, high = info["bounds"]
    rng = np.random.default_rng(SEED)
    x = rng.uniform(low, high, size=DIM)
    assert info["func"](x) > 0.0


@pytest.mark.parametrize("name", NAMES)
@pytest.mark.parametrize("dim", [2, 30])
def test_returns_float(name: str, dim: int) -> None:
    """Each function returns a Python float for dim 2 and dim 30."""
    info = BENCHMARKS[name]
    low, high = info["bounds"]
    rng = np.random.default_rng(SEED)
    x = rng.uniform(low, high, size=dim)
    assert isinstance(info["func"](x), float)

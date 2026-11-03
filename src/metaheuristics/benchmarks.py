"""Benchmark functions for testing optimizers (all are minimization problems).

Bounds follow the original GWO paper (Mirjalili et al., 2014):
Sphere (F1), Rosenbrock (F5), Rastrigin (F9), Ackley (F10).
Every function has its global minimum value 0.
"""

import numpy as np

DIM = 30  # default number of dimensions for experiments


def sphere(x: np.ndarray) -> float:
    """Sphere: sum of squares. Minimum 0 at x = 0."""
    return float(np.sum(x**2))


def rastrigin(x: np.ndarray) -> float:
    """Rastrigin: sphere plus a cosine wave that creates many local minima.

    Minimum 0 at x = 0.
    """
    return float(np.sum(x**2 - 10.0 * np.cos(2.0 * np.pi * x) + 10.0))


def ackley(x: np.ndarray) -> float:
    """Ackley: almost flat outer area with a deep hole in the center.

    Minimum 0 at x = 0.
    """
    n = x.size
    term1 = -20.0 * np.exp(-0.2 * np.sqrt(np.sum(x**2) / n))
    term2 = -np.exp(np.sum(np.cos(2.0 * np.pi * x)) / n)
    return float(term1 + term2 + 20.0 + np.e)


def rosenbrock(x: np.ndarray) -> float:
    """Rosenbrock: a long, narrow, curved valley. Minimum 0 at x = 1.

    Needs at least 2 dimensions.
    """
    return float(np.sum(100.0 * (x[1:] - x[:-1] ** 2) ** 2 + (x[:-1] - 1.0) ** 2))


# Registry so experiments can loop over all functions.
# "bounds" is (lower, upper) for every dimension.
# "optimum_x" is the value of every coordinate at the global minimum,
# so the optimum point is np.full(dim, optimum_x) for any dim.
BENCHMARKS = {
    "sphere": {"func": sphere, "bounds": (-100.0, 100.0), "optimum_x": 0.0},
    "rastrigin": {"func": rastrigin, "bounds": (-5.12, 5.12), "optimum_x": 0.0},
    "ackley": {"func": ackley, "bounds": (-32.0, 32.0), "optimum_x": 0.0},
    "rosenbrock": {"func": rosenbrock, "bounds": (-30.0, 30.0), "optimum_x": 1.0},
}

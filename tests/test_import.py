"""Check that the package can be imported."""

import metaheuristics


def test_import_package() -> None:
    """The package imports and has a version string."""
    assert isinstance(metaheuristics.__version__, str)

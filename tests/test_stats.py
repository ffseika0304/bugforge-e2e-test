from calc.stats import mean, median


def test_mean_of_numbers():
    assert mean([1, 2, 3]) == 2


def test_median_of_numbers():
    assert median([3, 1, 2]) == 2


def test_mean_of_empty_returns_none():
    assert mean([]) is None

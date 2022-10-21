from src.counter import count_ocurrences


def test_counter():
    assert count_ocurrences("tests/mocks/jobs.csv", "trainee") == 1

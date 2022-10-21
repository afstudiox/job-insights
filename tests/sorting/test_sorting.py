from src.jobs import read
from src.sorting import sort_by


def test_sort_by_criteria():
    results = read("src/jobs.csv")
    print(results)
    assert sort_by(results, "min_salary") == 0

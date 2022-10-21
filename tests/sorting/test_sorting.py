from src.sorting import sort_by

JOBS = [
    {"min_salary": 10000, "max_salary": 50000, "date_posted": "2022-01-01"},
    {"min_salary": 7000, "max_salary": 14000, "date_posted": "2022-02-01"},
    {"min_salary": 3000, "max_salary": 7000, "date_posted": "2022-03-01"},
]


def test_sort_by_criteria():
    sort_by(JOBS, "min_salary")
    assert JOBS[0]["min_salary"] == 3000

    sort_by(JOBS, "max_salary")
    assert JOBS[0]["max_salary"] == 50000

    sort_by(JOBS, "date_posted")
    assert JOBS[0]["date_posted"] == "2022-03-01"

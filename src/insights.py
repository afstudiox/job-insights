import os
from src.jobs import read


def get_unique_job_types(path):
    """
        Gets the unique job types from the CSV file

        :param path: path to the CSV file

        :return: set of job types
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    all_jobs = read(path)

    # Using a set expression to directly obtain unique types
    job_types = {job["job_type"] for job in all_jobs}
    return job_types


def filter_by_job_type(jobs, job_type):
    filtered_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            filtered_jobs.append(job)
    return filtered_jobs


def get_unique_industries(path):
    all_jobs = read(path)
    industries = set()
    for job in all_jobs:
        if job["industry"] != "":
            industries.add(job["industry"])
    return industries


def filter_by_industry(jobs, industry):
    filtered_jobs = []
    for job in jobs:
        if job["industry"] == industry:
            filtered_jobs.append(job)
    return filtered_jobs


def get_max_salary(path):
    all_jobs = read(path)
    salarys = set()
    for job in all_jobs:
        if job["max_salary"] != "":
            try:
                salarys.add(int(job["max_salary"]))
            except ValueError:
                pass
    result = max(salarys)
    return result


def get_min_salary(path):
    all_jobs = read(path)
    salarys = set()
    for job in all_jobs:
        if job["min_salary"] != "":
            try:
                salarys.add(int(job["min_salary"]))
            except ValueError:
                pass
    result = min(salarys)
    return result


def matches_salary_range(job, salary):
    if type(salary) != int:
        raise ValueError("1")
    elif ("max_salary" or "min_salary") not in job:
        raise ValueError("2")
    elif (type(job["max_salary"]) or type(job["min_salary"])) != int:
        raise ValueError("3")
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError("4")
    return job["max_salary"] >= salary >= job["min_salary"]


def filter_by_salary_range(jobs, salary):
    filter_by_salary_range_values = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filter_by_salary_range_values.append(job)
        except ValueError:
            pass
    return filter_by_salary_range_values

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
    """
        Filters a job list by job type

        :param jobs: list of jobs
        :param job_type: job type to filter by

        :return: list of jobs filtered by job type
    """
    filtered_jobs = [job for job in jobs if job["job_type"] == job_type]
    return filtered_jobs


def get_unique_industries(path):
    """
        Gets the unique industries from the CSV file

        :param path: path to the CSV file

        :return: A set containing the unique industries.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    all_jobs = read(path)
    # Using a set expression to directly obtain unique industries
    industries = {job["industry"] for job in all_jobs}
    return industries


def filter_by_industry(jobs, industry):
    """
        Filters a job list by industry

        :param jobs: list of jobs
        :param industry: industry to filter by

        :return: list of jobs filtered by industry
    """
    filtered_jobs = [job for job in jobs if job["industry"] == industry]
    return filtered_jobs


def get_max_salary(path):
    """
        Gets the maximum salary from the CSV file

        :param path: path to the CSV file

        :return: The maximum salary
    """
    all_jobs = read(path)
    salaries = {
        int(job["max_salary"])  # Convert the salary to an integer
        for job in all_jobs
        if job["max_salary"].isdigit()  # Check if the salary is a digit
        }
    # Return the maximum salary if the salaries set is not empty
    return max(salaries, default=None) if salaries else None


def get_min_salary(path):
    """
        Gets the minimum salary from the CSV file

        :param path: path to the CSV file

        :return: The minimum salary
    """
    all_jobs = read(path)
    salaries = {
        int(job["min_salary"])  # Convert the salary to an integer
        for job in all_jobs
        if job["min_salary"].isdigit()  # Check if the salary is a digit
        }
    # Return the minimum salary if the salaries set is not empty
    return min(salaries, default=None) if salaries else None


def matches_salary_range(job, salary):
    """
        Checks if a job matches a salary range

        :param job: job to check
        :param salary: salary to check

        :return: True if the job matches the salary range, False otherwise
    """

    # string errors
    error1 = "Salary must be a integer"
    error2 = "The min_salary and max_salary"
    +"keys must be present."
    error3 = "The values of min_salary and max_salary must be integers."
    error4 = "The value of min_salary cannot be greater than max_salary."

    if not job[salary].isdigit():
        raise TypeError(error1)
    if ("min_salary" not in job) or ("max_salary" not in job):
        raise ValueError(error2)
    if not (job["min_salary"].isdigit() and job["max_salary"].isdigit()):
        raise ValueError(error3)
    if int(job["min_salary"]) > int(job["max_salary"]):
        raise ValueError(error4)



def filter_by_salary_range(jobs, salary):
    filter_by_salary_range_values = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filter_by_salary_range_values.append(job)
        except ValueError:
            pass
    return filter_by_salary_range_values

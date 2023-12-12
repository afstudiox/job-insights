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
        if job["max_salary"] and job["max_salary"].isdigit()  # Check if the salary is a digit
        }
    # Return the maximum salary if the salaries set is not empty
    return max(salaries, default=0) if salaries else 0


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
        if job["min_salary"] and job["min_salary"].isdigit()  # Check if the salary is a digit
        }
    # Return the minimum salary if the salaries set is not empty
    return min(salaries, default=0) if salaries else 0


def matches_salary_range(job, salary):
    """
        Checks if a job matches a salary range

        :param job: job to check
        :param salary: salary to check

        :return: True if the job matches the salary range, False otherwise
    """
    # Check if min_salary and max_salary are present
    check_salary_keys(job)

    # Check if min_salary and max_salary are integers
    check_salary_integers(job)

    # Check if min_salary is less than max_salary
    check_salary_order(job)

    # Check if salary is an integer
    check_salary_type(salary)

    # Check if salary is in range
    return check_salary_range(job, salary)


def check_salary_keys(job):
    """
        Checks if min_salary and max_salary keys are present in the job dictionary

        :param job: job dictionary

        :raises: ValueError if min_salary or max_salary keys are missing
    """
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("The min_salary and max_salary keys must be present.")


def check_salary_integers(job):
    """
        Checks if min_salary and max_salary values are integers in the job dictionary

        :param job: job dictionary

        :raises: ValueError if min_salary or max_salary values are not integers
    """
    min_salary = job.get("min_salary", "")
    max_salary = job.get("max_salary", "")

    if min_salary and not min_salary.isdigit():
        raise ValueError("The value of min_salary must be an integer.")
  
    if max_salary and not max_salary.isdigit():
        raise ValueError("The value of max_salary must be an integer.")


def check_salary_order(job):
    """
        Checks if min_salary is less than max_salary in the job dictionary

        :param job: job dictionary

        :raises: ValueError if min_salary is greater than max_salary
    """
    min_salary = job.get("min_salary", "")
    max_salary = job.get("max_salary", "")

    if min_salary and max_salary:
        if min_salary.isdigit() and max_salary.isdigit():
            if int(min_salary) > int(max_salary):
                raise ValueError("The value of min_salary cannot be greater than max_salary.")


def check_salary_type(salary):
    """
        Checks if salary is an integer

        :param salary: salary value

        :raises: ValueError if salary is not an integer
    """
    if not isinstance(salary, int):
        raise ValueError("Salary must be an integer.")


def check_salary_range(job, salary):
    """
        Checks if salary is within the range of min_salary and max_salary in the job dictionary

        :param job: job dictionary
        :param salary: salary value

        :return: True if salary is within the range, False otherwise
    """
    min_salary = job.get("min_salary", "")
    max_salary = job.get("max_salary", "")

    if min_salary and max_salary:
        return int(min_salary) <= int(salary) <= int(max_salary)
    
    return True


def filter_by_salary_range(jobs, salary):
    """
        Filters a job list by salary range

        :param jobs: list of jobs
        :param salary: salary to filter by

        :return: list of jobs filtered by salary range
    """
    filtered_jobs = [
        job
        for job in jobs
        if
        job.get("min_salary") and
        job.get("max_salary") and
        matches_salary_range(job, salary)
    ]
    return filtered_jobs
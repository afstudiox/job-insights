import csv
import os
from functools import lru_cache


@lru_cache
def read(path):
    """
    Reads a CSV file and returns a list of dictionaries

    :param path: path to the CSV file

    :return: list of dictionaries
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    with open(path) as file:
        try:
            jobs_load = csv.DictReader(file)
            jobs = [job for job in jobs_load]
            return jobs
        except csv.Error as e:
            raise ValueError(f"Error parsing CSV file: {e}")

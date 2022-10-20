import csv
from functools import lru_cache


@lru_cache
def read(path):

    with open(path) as file:
        jobs_load = csv.DictReader(file)
        jobs = []
        for job in jobs_load:
            jobs.append(job)
        return jobs

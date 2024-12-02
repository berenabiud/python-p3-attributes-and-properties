#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    # Define the approved jobs as a class attribute
    approved_jobs = [
        "Admin", "Customer Service", "Human Resources", "ITC", 
        "Production", "Legal", "Finance", "Sales", 
        "General Management", "Research & Development", "Marketing"
    ]

    def __init__(self, name="Person", job="General Management"):
        self._name = None  # Initialize a private attribute for name
        self._job = None   # Initialize a private attribute for job
        self.name = name   # Use the setter to validate the default name
        self.job = job     # Use the setter to validate the default job

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()  # Convert name to title case
        else:
            print("Name must be string between 1 and 25 characters.")

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value in self.approved_jobs:
            self._job = value
        else:
            print("Job must be in list of approved jobs.")

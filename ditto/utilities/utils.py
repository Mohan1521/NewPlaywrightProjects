"""
Utility functions for Ditto Playwright POM tests.
"""
from faker import Faker

def get_fake_user():
    fake = Faker()
    return {
        "name": fake.first_name(),
        "age": fake.random_int(min=18, max=60),
        "pincode": fake.postcode(),
        "gender": fake.random_element(elements=("Male", "Female")),
    }


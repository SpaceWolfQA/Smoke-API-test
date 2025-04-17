import uuid
from faker import Faker
from config.settings import set

fake = Faker()


def generate_company():
    company = 'qa_smoke_test_' + str(uuid.uuid4())
    set('company', company)
    return company


def generate_email():
    email = f'{fake.first_name().lower()}_{fake.last_name().lower()}@edgecenter.smoketest.com'
    set('email', email)
    return email


def generate_password():
    password = fake.password(16, True, True, True, True)
    return password

from config.settings import set
from faker import Faker

fake = Faker()


def create_metric_payload():
    metric_name = fake.first_name()[:3].upper()
    set('metric_name', metric_name)
    return {
        "int_name": metric_name,
        "ext_name": metric_name
    }

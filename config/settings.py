import os
import json
from dotenv import load_dotenv
from typing import Any, Dict

load_dotenv()

_config: Dict[str, Any] = {}


def set(key: str, value: Any) -> None:
    _config[key] = value


def get(key: str, default: Any = None) -> Any:
    return _config.get(key, default)


url_bill = os.getenv('URL_BILL')
url_iam = os.getenv('URL_IAM')
headers = json.loads(os.getenv('HEADERS'))
max_retries = int(os.getenv('MAX_RETRIES', 5))
wait_sec = int(os.getenv('WAIT_SEC', 5))

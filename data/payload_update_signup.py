from config.settings import get

update_signup_payload = {
    "email": get('email'),
    "companyName": get('company'),
    "reseller": 75755,
    "signup_process": ""
}
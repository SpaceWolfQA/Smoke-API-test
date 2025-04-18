from config.settings import *
from data.payload_new_client import new_client_payload
from data.payload_update_signup import update_signup_payload
from data.payload_cancel_requrring_payments import cancel_recurring_payments_payload
from data.payload_add_bank_transfer import add_bank_transfer_payload
from data.payload_create_contract import create_contract_payload
from data.payload_create_plan import create_plan_payload
from data.payload_edit_plan import edit_plan_payload
from data.payload_copy_plan import copy_plan_payload
from data.payload_create_metric import create_metric_payload
from data.payload_create_feature import create_feature_payload
from data.payload_edit_feature import edit_feature_payload
from data.payload_add_feature import add_feature_payload
from data.payload_edit_plan_feature import edit_plan_feature_payload
from data.payload_update_trial import update_trial_payload
from data.payload_start_trial import start_trial_payload
from data.payload_create_addendum import create_addendum_payload
from data.payload_create_expense import create_expense_payload
from data.payload_create_invoice import create_invoice_payload
from data.payload_delete_client import delete_client_payload
from endpoints.create_new_client import CreateClient
from endpoints.update_client import UpdateClient
from endpoints.get_payer_id import GetPayerID
from endpoints.create_contract import CreateContract
from endpoints.create_plan import CreatePlan
from endpoints.edit_plan import EditPlan
from endpoints.copy_plan import CopyPlan
from endpoints.create_metric import CreateMetric
from endpoints.create_feature import CreateFeature
from endpoints.edit_feature import EditFeature
from endpoints.add_feature_to_plan import AddFeature
from endpoints.edit_plan_feature import EditPlanFeature
from endpoints.get_trial_id import GetTrialID
from endpoints.update_trial import UpdateTrial
from endpoints.start_trial import StartTrial
from endpoints.end_trial import EndTrial
from endpoints.create_addendum import CreateAddendum
from endpoints.create_expense import CreateExpense
from endpoints.create_invoice import CreateInvoice
from endpoints.update_invoice import UpdateInvoice
from endpoints.delete_invoice_item import DeleteInvoiceItem
from endpoints.delete_invoice import DeleteInvoice
from endpoints.delete_plan_feature import DeletePlanFeature
from endpoints.delete_copy_plan import DeleteCopyPlan
from endpoints.delete_plan import DeletePlan
from endpoints.delete_feature import DeleteFeature
from endpoints.delete_metric import DeleteMetric
from endpoints.delete_contract import DeleteContract
from endpoints.delete_client import DeleteClient


def test_create_new_client():
    client = CreateClient()
    client.new_client(
        url_iam=url_iam,
        headers=headers,
        payload=new_client_payload,
        max_retries=max_retries,
        wait_sec=wait_sec
    )
    client.check_creation(url_iam=url_iam, headers=headers, max_retries=max_retries, wait_sec=wait_sec)


def test_update_client():
    update = UpdateClient()
    update.update_signup(
        url_iam=url_iam,
        headers=headers,
        payload=update_signup_payload,
        max_retries=max_retries,
        wait_sec=wait_sec
    )
    update.check_signup(url_iam=url_iam, headers=headers, max_retries=max_retries, wait_sec=wait_sec)

    update.cancel_recurring_payments(
        url_bill=url_bill,
        headers=headers,
        payload=cancel_recurring_payments_payload(),
        max_retries=max_retries,
        wait_sec=wait_sec
    )
    update.check_recurring_payments(url_bill=url_bill, headers=headers, max_retries=max_retries, wait_sec=wait_sec)

    update.delete_yoomoney(url_bill=url_bill, headers=headers, max_retries=max_retries, wait_sec=wait_sec)
    update.add_bank_transfer(
        url_bill=url_bill,
        headers=headers,
        payload=add_bank_transfer_payload(),
        max_retries=max_retries,
        wait_sec=wait_sec
    )
    update.check_payments_methods(url_bill=url_bill, headers=headers, max_retries=max_retries, wait_sec=wait_sec)


def test_payer_id():
    payer_id = GetPayerID()
    payer_id.get_payer_id(url_bill=url_bill, headers=headers, max_retries=max_retries, wait_sec=wait_sec)


def test_create_contract():
    contract = CreateContract()
    contract.create_contract(
        url_bill=url_bill,
        headers=headers,
        payload=create_contract_payload(),
        max_retries=max_retries,
        wait_sec=wait_sec
    )
    contract.check_creation(url_bill=url_bill, headers=headers, max_retries=max_retries, wait_sec=wait_sec)


def test_create_plan():
    plan = CreatePlan()
    plan.create_plan(
        url_bill=url_bill,
        headers=headers,
        payload=create_plan_payload(),
        max_retries=max_retries,
        wait_sec=wait_sec
    )
    plan.check_creation(url_bill=url_bill, headers=headers, max_retries=max_retries, wait_sec=wait_sec)


def test_edit_plan():
    plan = EditPlan()
    plan.edit_plan(
        url_bill=url_bill,
        headers=headers,
        payload=edit_plan_payload(),
        max_retries=max_retries,
        wait_sec=wait_sec
    )
    plan.check_edit(url_bill=url_bill, headers=headers, max_retries=max_retries, wait_sec=wait_sec)


def test_copy_plan():
    plan = CopyPlan()
    plan.copy_plan(
        url_bill=url_bill,
        headers=headers,
        payload=copy_plan_payload(),
        max_retries=max_retries,
        wait_sec=wait_sec
    )
    plan.check_copy_plan(url_bill=url_bill, headers=headers, max_retries=max_retries, wait_sec=wait_sec)


def test_create_metric():
    metric = CreateMetric()
    metric.create_metric(
        url_bill=url_bill,
        headers=headers,
        payload=create_metric_payload(),
        max_retries=max_retries,
        wait_sec=wait_sec
    )
    metric.check_create(url_bill=url_bill, headers=headers, max_retries=max_retries, wait_sec=wait_sec)


def test_create_feature():
    feature = CreateFeature()
    feature.create_feature(
        url_bill=url_bill,
        headers=headers,
        payload=create_feature_payload(),
        max_retries=max_retries,
        wait_sec=wait_sec
    )
    feature.check_create(url_bill=url_bill, headers=headers, max_retries=max_retries, wait_sec=wait_sec)


def test_edit_feature():
    feature = EditFeature()
    feature.edit_feature(
        url_bill=url_bill,
        headers=headers,
        payload=edit_feature_payload(),
        max_retries=max_retries,
        wait_sec=wait_sec
    )
    feature.check_edit(url_bill=url_bill, headers=headers, max_retries=max_retries, wait_sec=wait_sec)


def test_add_feature():
    feature = AddFeature()
    feature.add_feature(
        url_bill=url_bill,
        headers=headers,
        payload=add_feature_payload(),
        max_retries=max_retries,
        wait_sec=wait_sec
    )
    feature.check_add_feature(url_bill=url_bill, headers=headers, max_retries=max_retries, wait_sec=wait_sec)


def test_edit_plan_feature():
    plan_feature = EditPlanFeature()
    plan_feature.edit_plan_feature(
        url_bill=url_bill,
        headers=headers,
        payload=edit_plan_feature_payload(),
        max_retries=max_retries,
        wait_sec=wait_sec
    )
    plan_feature.check_edit(url_bill=url_bill, headers=headers, max_retries=max_retries, wait_sec=wait_sec)


def test_get_trial_id():
    trial_id = GetTrialID()
    trial_id.get_trial_id(url_bill=url_bill, headers=headers, max_retries=max_retries, wait_sec=wait_sec)


def test_update_trial():
    trial = UpdateTrial()
    trial.update_trial(
        url_bill=url_bill,
        headers=headers,
        payload=update_trial_payload(),
        max_retries=max_retries,
        wait_sec=wait_sec
    )
    trial.check_update_trial(url_bill=url_bill, headers=headers, max_retries=max_retries, wait_sec=wait_sec)


def test_statr_trial():
    trial = StartTrial()
    trial.start_trial(
        url_bill=url_bill,
        headers=headers,
        payload=start_trial_payload(),
        max_retries=max_retries,
        wait_sec=wait_sec
    )
    trial.check_start(url_bill=url_bill, headers=headers, max_retries=max_retries, wait_sec=wait_sec)


def test_end_trial():
    trial = EndTrial()
    trial.end_trial(url_bill=url_bill, headers=headers, max_retries=max_retries, wait_sec=wait_sec)
    trial.check_end(url_bill=url_bill, headers=headers, max_retries=max_retries, wait_sec=wait_sec)


def test_create_new_addendum():
    addendum = CreateAddendum()
    addendum.create_addendum(
        url_bill=url_bill,
        headers=headers,
        payload=create_addendum_payload(),
        max_retries=max_retries,
        wait_sec=wait_sec
    )
    addendum.check_activate(url_bill=url_bill, headers=headers, max_retries=max_retries, wait_sec=wait_sec)


def test_create_expense():
    expense = CreateExpense()
    expense.create_expense(
        url_bill=url_bill,
        headers=headers,
        payload=create_expense_payload(),
        max_retries=max_retries,
        wait_sec=wait_sec
    )
    expense.check_create(url_bill=url_bill, headers=headers, max_retries=max_retries, wait_sec=wait_sec)


def test_create_invoice():
    invoice = CreateInvoice()
    invoice.create_invoice(
        url_bill=url_bill,
        headers=headers,
        payload=create_invoice_payload(),
        max_retries=max_retries,
        wait_sec=wait_sec
    )
    invoice.check_create(url_bill=url_bill, headers=headers, max_retries=max_retries, wait_sec=wait_sec)


def test_update_invoice():
    invoice = UpdateInvoice()
    invoice.update_invoice(url_bill=url_bill, headers=headers, max_retries=max_retries, wait_sec=wait_sec)
    invoice.check_update(url_bill=url_bill, headers=headers, max_retries=max_retries, wait_sec=wait_sec)


def test_delete_invoice_item():
    invoice = DeleteInvoiceItem()
    invoice.get_invoice_item_id(url_bill=url_bill, headers=headers)
    invoice.delete_invoice_item(url_bill=url_bill, headers=headers, max_retries=max_retries, wait_sec=wait_sec)
    invoice.check_status_code_is_204()
    invoice.check_deletion(url_bill=url_bill, headers=headers, max_retries=max_retries, wait_sec=wait_sec)


def test_delete_invoice():
    invoice = DeleteInvoice()
    invoice.delete_invoice(url_bill=url_bill, headers=headers, max_retries=max_retries, wait_sec=wait_sec)
    invoice.check_status_code_is_204()
    invoice.check_deletion(url_bill=url_bill, headers=headers, max_retries=max_retries, wait_sec=wait_sec)


def test_delete_plan_feature():
    plan_feature = DeletePlanFeature()
    plan_feature.delete_plan_feature(url_bill=url_bill, headers=headers, max_retries=max_retries, wait_sec=wait_sec)
    plan_feature.check_status_code_is_204()
    plan_feature.check_deletion(url_bill=url_bill, headers=headers, max_retries=max_retries, wait_sec=wait_sec)


def test_delete_copy_plan():
    plan = DeleteCopyPlan()
    plan.delete_copy_plan(url_bill=url_bill, headers=headers, max_retries=max_retries, wait_sec=wait_sec)
    plan.check_status_code_is_204()
    plan.check_deletion(url_bill=url_bill, headers=headers, max_retries=max_retries, wait_sec=wait_sec)


def test_delete_plan():
    plan = DeletePlan()
    plan.delete_plan(url_bill=url_bill, headers=headers, max_retries=max_retries, wait_sec=wait_sec)
    plan.check_status_code_is_204()
    plan.check_deletion(url_bill=url_bill, headers=headers, max_retries=max_retries, wait_sec=wait_sec)


def test_delete_feature():
    feature = DeleteFeature()
    feature.delete_feature(url_bill=url_bill, headers=headers, max_retries=max_retries, wait_sec=wait_sec)
    feature.check_status_code_is_204()
    feature.check_deletion(url_bill=url_bill, headers=headers, max_retries=max_retries, wait_sec=wait_sec)


def test_delete_metric():
    metric = DeleteMetric()
    metric.delete_metric(url_bill=url_bill, headers=headers, max_retries=max_retries, wait_sec=wait_sec)
    metric.check_status_code_is_204()
    metric.check_deletion(url_bill=url_bill, headers=headers, max_retries=max_retries, wait_sec=wait_sec)


def test_delete_contract():
    contract = DeleteContract()
    contract.delete_contract(url_bill=url_bill, headers=headers, max_retries=max_retries, wait_sec=wait_sec)
    contract.check_status_code_is_204()
    contract.check_deletion(url_bill=url_bill, headers=headers, max_retries=max_retries, wait_sec=wait_sec)


def test_delete_client():
    client = DeleteClient()
    client.delete_client(
        url_iam=url_iam,
        headers=headers,
        payload=delete_client_payload(),
        max_retries=max_retries,
        wait_sec=wait_sec
    )
    client.check_status_code_is_200()
    client.check_deletion(url_iam=url_iam, headers=headers, max_retries=max_retries, wait_sec=wait_sec)

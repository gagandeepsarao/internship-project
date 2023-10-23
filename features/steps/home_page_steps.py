from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('Click on “Connect the Company”')
def click_connect_company(context):
    context.app.home_page.click_connect_company()

@then('Switch to the new tab')
def user_switched_to_window(context):
    context.app.home_page.user_switched_to_window()

@then('Verify there are {expected_amount} steps in the description')
def verify_four_steps_description(context, expected_amount):
    count = context.app.home_page.four_steps_description()
    assert str(count) == expected_amount

@then('Verify “Subscription plans” button is clickable')
def verify_subscription_plan_button_clickable(context):
    context.app.home_page.verify_subscription_plan_clickable()





from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import alert_is_present, invisibility_of_element


@given(u'I am on the webpage with the button')
def step_impl(context):
    """absolute path to file required"""
    context.driver.get("../utils/basics.html")


@when(u'I click the button')
def step_impl(context):
    context.delayed_button_page.get_button().click()


@then(u'I should see an alert with my message after 3 seconds')
def step_impl(context):
    # the WebDriverWait below is set to wait 4 seconds, I added a buffer second to prevent flakey tests
    delay_wait: WebDriverWait = WebDriverWait(context.driver, 4).until(alert_is_present())
    assert context.delayed_button_page.get_alert().text == "This shows up after 3 seconds"


@then(u'I should not be able to see the button anymore')
def step_impl(context):
    context.delayed_button_page.get_alert().accept() # need to close the alert before the button will disappear
    # the WebDriverWait below is a useful way of checking that an element has been hidden or deleted
    check_visibility: WebDriverWait = WebDriverWait(context.driver, 1).until(invisibility_of_element(context.delayed_button_page.get_button()))
    assert True

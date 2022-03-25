from behave import given, when, then
from behave.runner import Context
from selenium.webdriver.support.select import Select


@given(u'I am on the Wikipedia home page')
def step_impl(context: Context):
    context.driver.get("https://www.wikipedia.org/")


@when(u'I enter apple into the search bar')
def step_impl(context: Context):
    context.wiki_home.search_bar().send_keys("apple")


@when(u'I select English as my search language')
def step_impl(context: Context):
    select_element: Select = context.wiki_home.language_selector()
    select_element.select_by_value("en")


@when(u'I click the search button')
def step_impl(context):
    context.wiki_home.search_button().click()


@then(u'I should be sent to the apple fruit information page')
def step_impl(context):
    assert context.driver.title == "Apple - Wikipedia"


@when(u'I select Spanish as my search language')
def step_impl(context):
    context.wiki_home.language_selector().select_by_value("es")


@then(u'I should be sent to the Apple tech company information page')
def step_impl(context):
    assert context.driver.title == "Apple - Wikipedia, la enciclopedia libre"

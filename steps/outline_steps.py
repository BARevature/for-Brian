from behave import when, then


@when(u'I type {criteria} into the search bar')
def step_impl(context, criteria: str):
    context.wiki_home.search_bar().send_keys(criteria)


@then(u'I should be sent to a page with {title} as the title')
def step_impl(context, title: str):
    assert context.driver.title == title

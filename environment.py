"""This module is where Behave passes in a context object for setup and teardown"""
from behave.runner import Context
from selenium import webdriver

from page_object_models.delayed_button_page import DelayedButtonPage
from page_object_models.wiki_home import WikiHomePage


def before_all(context: Context):
    context.driver = webdriver.Chrome("utils/chromedriver.exe") # tells behave where the web driver is located
    context.wiki_home = WikiHomePage(context.driver) # gives the context access to the POM
    context.delayed_button_page = DelayedButtonPage(context.driver) # gives the context access to the POM
    context.driver.implicitly_wait(1) # helps prevent flakey tests due to low latency
    print("I run before any steps")


def after_all(context: Context):
    context.driver.quit() # if you don't include this you will need to manually kill the driver process
    print("I run after all the scenarios")

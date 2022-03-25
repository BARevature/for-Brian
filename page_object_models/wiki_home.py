from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select


class WikiHomePage:
    """the methods below are for finding specific elements on the web page and returning them for Selenium"""

    def __init__(self, driver: WebDriver):
        self.driver = driver # this will be provided by the driver in the context object

    def search_bar(self):
        element: WebElement = self.driver.find_element(By.ID, "searchInput")
        return element

    def language_selector(self):
        select: Select = Select(self.driver.find_element(By.ID, "searchLanguage"))
        return select

    def search_button(self):
        element: WebElement = self.driver.find_element(By.XPATH,"/html/body/div[3]/form/fieldset/button")  # '//*[@id="search-form"]/fieldset/button' this is the relative x path
        return element

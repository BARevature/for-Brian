from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By


class DelayedButtonPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_button(self):
        return self.driver.find_element(By.ID, "button")

    def get_alert(self):
        """added this since the delay button creates an alert in the browser"""
        alert: Alert = self.driver.switch_to.alert
        return alert

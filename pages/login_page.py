from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import Page


class LoginPage(Page):
    USERNAME = (By.ID, "email-2")
    PASSWORD = (By.ID,"field")
    LOGIN_BUTTON = (By.LINK_TEXT,"Continue")

    def login(self):
        self.find_element(*self.PASSWORD).send_keys("J@1diamond!")
        self.find_element(*self.USERNAME).send_keys("gagandeepsarao8@gmail.com")
        self.click(*self.LOGIN_BUTTON)

from pages.home_page import HomePage
from pages.main_page import MainPage
from pages.login_page import LoginPage


class Application:

    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.login_page = LoginPage(driver)
        self.home_page = HomePage(driver)

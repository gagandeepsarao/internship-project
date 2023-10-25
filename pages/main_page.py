from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import Page
from support.logger import logger


class MainPage(Page):


    def open_main(self):
        logger.info("Opening https://soft.reelly.io/sign-in")
        self.driver.get('https://soft.reelly.io/sign-in')
        sleep(2)




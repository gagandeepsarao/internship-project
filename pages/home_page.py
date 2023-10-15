from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC


class HomePage(Page):
    SUBSCRIPTION_BUTTON = (By.XPATH,'//div[text()="Get a free subscription"]')
    DESCRIPTION_STEP = (By.XPATH,'//div[@class= "step-text"]')
    SUBSCRIPTION_PLAN = (By.XPATH,'//a[text()="Subscription plans"]')

    def click_subscription_button(self):
        self.click(*self.SUBSCRIPTION_BUTTON)

    def user_switched_to_window(self):
        self.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles
        print(all_windows)
        print(f'Switching to {all_windows[1]}')
        self.driver.switch_to.window(all_windows[1])


    def four_steps_description(self):
        steps = self.driver.find_elements(*self.DESCRIPTION_STEP)
        print(len(steps))
        return len(steps)

    def verify_subscription_plan_clickable(self):
        self.wait_for_element_clickable(*self.SUBSCRIPTION_PLAN)

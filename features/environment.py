from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from app.application import Application
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait




def browser_init(context,scenario_name):
    """
    :param context: Behave context
    """
    ### HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # service = Service(executable_path='/Users/svetlanalevinsohn/careerist/15-python-selenium-automation/chromedriver')
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    ### OTHER BROWSERS ###
    # service = Service(executable_path=r"C:\Users\gagan\Documents\python-selenium-automation\firefoxdriver\geckodriver.exe")
    # context.driver = webdriver.Firefox(service=service)

    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument("window-size=1920,1080")
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(options=options,service=service)
    ### BROWSERSTACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    bs_user = 'gagandeepsarao_QczjXx'
    bs_key = 'D4pK7fSayxnLLfghYVsq'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    options = Options()
    bstack_options = {
        'os': 'Windows',
        'osVersion': '10',
        'browserName': 'Firefox',
        'sessionName': scenario_name
    }
    options.set_capability('bstack:options', bstack_options)
    options.add_argument('--headless')
    options.add_argument("window-size=1920,1080")
    context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)

    context.app = Application(context.driver)




def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context,scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()

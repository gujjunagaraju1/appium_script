from appium import webdriver
from appium.options.android import UiAutomator2Options
from config.config import Config
import pytest


@pytest.fixture(scope="function")
def driver():
    option=UiAutomator2Options()
    option.platform_name=Config.platformName
    option.device_name=Config.deviceName
    option.automation_name=Config.automationName
    option.app_package=Config.appPackage
    option.app_activity=Config.appActivity
    option.auto_grant_permissions=True
    driver=webdriver.Remote("http://127.0.0.1:4723",options=option)
    driver.implicitly_wait(10)
    print("app launched")
    yield driver
    print("app closed")
    driver.terminate_app(Config.appPackage)
    driver.quit()


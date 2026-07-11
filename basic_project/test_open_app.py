from appium import webdriver
from appium.options.android import UiAutomator2Options
from config.config import Config
print(Config.appActivity)
options=UiAutomator2Options()
options.platform_name=Config.platformName
options.device_name=Config.deviceName
options.automation_name=Config.automationName
options.app_package=Config.appPackage
options.app_activity=Config.appActivity
options.auto_grant_permissions=True
driver=webdriver.Remote("http://127.0.0.1:4723",options=options)
print("succeefully")
driver.terminate_app(Config.appPackage)
print("terminated")




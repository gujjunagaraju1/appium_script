from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from config.config import Config
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
import time

def test_login(driver:WebDriver):
    driver.find_element(AppiumBy.ACCESSIBILITY_ID,"English").click()
    driver.find_element(AppiumBy.ACCESSIBILITY_ID,"Continue").click()
    mobile_field = driver.find_element(
    AppiumBy.XPATH,
    "//android.widget.EditText")
    mobile_field.click()
    mobile_field.send_keys(Config.mobileNumber)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID,"Continue").click()
   
    otp = driver.find_element(
    AppiumBy.XPATH,
    "//android.view.View[@content-desc='Enter OTP']/following-sibling::android.widget.EditText"
)
    otp.click()
    time.sleep(1)
    otp.send_keys(Config.otp)
    print(otp.text)
    print(otp.get_attribute("text"))
   
    driver.find_element(AppiumBy.ACCESSIBILITY_ID,"Login").click()
    
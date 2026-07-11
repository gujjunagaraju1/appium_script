from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
import time


def test_login(driver:WebDriver):
    otp="1000"
    driver.find_element(AppiumBy.ACCESSIBILITY_ID,"English").click()
    
    driver.find_element(AppiumBy.XPATH,"//android.widget.EditText").send_keys("9014969320")
    
   # driver.find_element(AppiumBy.ACCESSIBILITY_ID,"I want to receive updates over Whatsapp").click()
    driver.find_element(AppiumBy.ACCESSIBILITY_ID,"Next").click()
    
    print("-------")
    print(driver.page_source)
    print("----------")
    mobile=driver.find_element(AppiumBy.CLASS_NAME,"android.widget.EditText")
    driver.execute_script(
    "mobile: type",
    {"text": "1000"}
)


    
    time.sleep(1)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID,"Next").click()
    time.sleep(1)



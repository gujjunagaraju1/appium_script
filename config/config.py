import os
from dotenv import load_dotenv
load_dotenv(override=True)



class Config:
    #platformName
   
    deviceName=os.getenv("deviceName")
    appPackage=os.getenv("appPackage")
    appActivity=os.getenv("appActivity")
    automationName=os.getenv("automationName")
    platformName=os.getenv("platformName")

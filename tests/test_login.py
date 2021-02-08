import os
from _pytest.main import Session
from appium import webdriver as AppiumDriver
from pages.login import Login
import pytest

# os.system('start /B start cmd.exe @cmd /k appium -p 4728 --nodeconfig /Users/divyasingla/PythonProjects/AppiumPytest/selenium_grid_config/nodeconfig-android1.json')
# @pytest.fixture(scope=Session)

# def setUp():
#     os.system('start /B start cmd.exe @cmd /k appium -p 4728 --nodeconfig /Users/divyasingla/PythonProjects/AppiumPytest/selenium_grid_config/nodeconfig-android1.json')    

@pytest.mark.parametrize("udid, deviceName, systemPort",[('emulator-5554', 'Pixel 3A', '8201'),('emulator-5556', 'Pixel 3 XL', '8202')])
def test_login(udid, deviceName, systemPort):
    Desired_Capabilities = {
        'automationName' : 'UIAutomator2',
        'platformName' : 'Android',
        'app' : os.getcwd() + '/aklogin.apk',
        'platformVersion': '11',
        'udid': udid,
        'deviceName': deviceName,
        'appActivity': 'dev.ankitkumar.kotlinlogin.MainActivity',
        'appPackage': 'dev.ankitkumar.kotlinlogin',
        'newCommandTimeout': 60,
        'systemPort': int(systemPort)
    }
    driver = AppiumDriver.Remote("http://127.0.0.1:4444/wd/hub", desired_capabilities=Desired_Capabilities)
    login = Login(driver)
    login.login_into_app()

  
    
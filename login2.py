
from appium import webdriver as AppiumDriver
from pages.login import Login
import pytest
import os


@pytest.mark.parametrize("udid, deviceName, systemPort",[('emulator-5554', 'Pixel 3A', '8201'),('emulator-5556', 'Pixel 3 XL', '8202')])
def test_login(udid, deviceName, systemPort):
    for i in range(2):
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
        driver = AppiumDriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=Desired_Capabilities)
        login = Login(driver)
        login.login_into_app()  

for i in range(2):
    @pytest.mark.parametrize("udid, deviceName, systemPort",[('emulator-5554', 'Pixel 3A', '8201'),('emulator-5554', 'Pixel 3A', '8201'),('emulator-5556', 'Pixel 3 XL', '8202'),('emulator-5556', 'Pixel 3 XL', '8202')])                     
    def login(udid, deviceName, systemPort):
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
        driver = AppiumDriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=Desired_Capabilities)
        login = Login(driver)
        login.login_into_app() 
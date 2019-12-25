from appium import webdriver


def get_driver(os, version, pack, act):
    capabilities = {
        "platformName": os,
        "platformVersion": version,
        "deviceName": "模拟器",
        "appPackage": pack,
        "appActivity": act
    }
    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=capabilities)

# 导包
import time
from appium import webdriver

# com.android.settings/.Settings
# 驱动
capabilities = {
    "platformName": "Android",
    "platformVersion": "5.1",
    "deviceName": "模拟器",
    "appPackage": "com.android.settings",
    "appActivity": ".Settings"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=capabilities)
# 等待
time.sleep(2)
# 关闭
driver.quit()

from app.xueqiu_frame.page.main_page import MainPage
from appium import webdriver
from app.xueqiu_frame.page.base_page import BasePage


class App(BasePage):
    def start(self):
        if self.driver == None:
            disired_caps = {
                "platformName": "android",
                "platformversion": "6.0",
                "deviceName": "127.0.0.1:7555",
                "appPackage": "com.xueqiu.android",
                "appActivity": "com.xueqiu.android.common.MainActivity",
                "noReset": "true",
                "dontStopAppOnReset": "true",
                "skipDeviceInitialization": "true",
                "skipServerInstallation": "true",
                "unicodeKeyBoard": "true",
                "resetKeyBoard": "true"
            }
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", disired_caps)
            self.driver.implicitly_wait(6)
        else:
            self.driver.launch_app()
        return self

    def stop(self):
        self.driver.close_app()

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()
        return self

    def goto_main_page(self):
        return MainPage(self.driver)

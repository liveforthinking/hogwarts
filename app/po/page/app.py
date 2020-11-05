from app.po.page.base_page import BasePage
from app.po.page.main_page import MainPage
from appium import webdriver


class App(BasePage):
    def start(self):
        if self.driver == None:
            disired_caps = {
                "platformName": "android",
                "platformversion": "6.0",
                "deviceName": "127.0.0.1:7555",
                "appPackage": "com.tencent.wework",
                "appActivity": ".launch.WwMainActivity",
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

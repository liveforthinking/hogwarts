import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from app.xueqiu_frame.conftest import exception_handle


class BasePage:
    _black_list = [(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")]
    _error_max = 3
    _error_count = 0

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    @exception_handle
    def find(self, by, locator=None):
        if locator == None:
            result = self.driver.find_element(*by)
        else:
            result = self.driver.find_element(by, locator)
        return result

    @exception_handle
    def find_and_click(self, by, locator):
        self.driver.find_element(by, locator).click()

    @exception_handle
    def find_by_scroll(self, text):
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        f'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("{text}").instance(0));')

    def get_toast_text(self):
        return self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text

    def parse_yaml(self, path, func_name):
        with open(path) as f:
            data = yaml.load(f)
        for step in data[func_name]:
            if step['action'] == 'click':
                self.find_and_click(step['by'], step['locator'])
            elif step['action'] == 'sendkeys':
                self.find(step['by'], step['locator']).send_keys(step['content'])

from appium.webdriver.common.mobileby import MobileBy

from app.po.page.base_page import BasePage


class ContactEditPage(BasePage):
    def delete_member(self):
        self.find_and_click(MobileBy.XPATH, "//*[@text='删除成员']")
        self.find_and_click(MobileBy.XPATH, "//*[@resource-id='android:id/content']//*[@text='确定']")

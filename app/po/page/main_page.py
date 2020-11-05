from appium.webdriver.common.mobileby import MobileBy
from app.po.page.addresslist_page import AddressListPage
from app.po.page.base_page import BasePage


class MainPage(BasePage):
    def goto_message(self):
        '''
        进入消息
        :return:
        '''

    def goto_addresslist(self):
        '''
        进入通讯录
        :return:
        '''
        self.find_and_click(MobileBy.XPATH, "//*[@text='通讯录']")
        return AddressListPage(self.driver)

    def goto_workplatform(self):
        '''
        进入工作台
        :return:
        '''

    def goto_me(self):
        '''
        进入我
        :return:
        '''

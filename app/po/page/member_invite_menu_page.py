from appium.webdriver.common.mobileby import MobileBy
from app.po.page.base_page import BasePage


class MemberInviteMenuPage(BasePage):
    def add_member_by_invite(self):
        '''
        微信邀请同事
        :return:
        '''
        pass

    def add_member_by_addresslist(self):
        '''
        从微信/手机通讯录中添加
        :return:
        '''
        pass

    def add_member_by_manual(self):
        '''
        手动输入添加
        :return:
        '''
        self.find_and_click(MobileBy.XPATH, "//*[@text='手动输入添加']")
        from app.po.page.contact_add_page import ContactAddPage
        return ContactAddPage(self.driver)

    def get_toast(self):
        return self.get_toast_text()

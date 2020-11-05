from appium.webdriver.common.mobileby import MobileBy
from app.po.page.contact_detail_setting_page import ContactDetailSettingPage
from app.po.page.base_page import BasePage


class ContactDetailBriefInfoProfilePage(BasePage):
    def contact_detail_setting(self):
        # 点击右上角
        self.find_and_click(MobileBy.XPATH, "//*[@text='个人信息']/../../../../../*[@index='1']")
        return ContactDetailSettingPage(self.driver)

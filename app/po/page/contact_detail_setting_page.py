from appium.webdriver.common.mobileby import MobileBy
from app.po.page.base_page import BasePage
from app.po.page.contact_edit_age import ContactEditPage


class ContactDetailSettingPage(BasePage):
    def contact_edit(self):
        # 点击 编辑成员
        self.driver.find_element(MobileBy.XPATH, "//*[@text='编辑成员']").click()
        return ContactEditPage(self.driver)

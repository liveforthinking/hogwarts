from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from app.po.page.base_page import BasePage


class ContactAddPage(BasePage):
    def add_contact(self, username, gender, phonenumber):
        self.find(MobileBy.XPATH,
                  "//*[contains(@text,'姓名')]/../*[@class='android.widget.EditText']").send_keys(username)
        self.find_and_click(MobileBy.XPATH, "//*[contains(@text,'性别')]/../android.widget.RelativeLayout")
        if gender == "男":
            WebDriverWait(self.driver, 10).until(
                expected_conditions.element_to_be_clickable((MobileBy.XPATH, "//*[contains(@text,'男')]")))
            self.find_and_click(MobileBy.XPATH, "//*[contains(@text,'男')]")
        else:
            self.find_and_click(MobileBy.XPATH, "//*[contains(@text,'女')]")
        self.find(MobileBy.XPATH,
                  "//*[contains(@text,'手机') and @clickable='false']/..//*[@class='android.widget.EditText']").send_keys(
            phonenumber)
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='保存']"))
        self.find_and_click(MobileBy.XPATH, "//*[@text='保存']")
        # assert "添加成功" == self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        # return self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        from app.po.page.member_invite_menu_page import MemberInviteMenuPage
        return MemberInviteMenuPage(self.driver)

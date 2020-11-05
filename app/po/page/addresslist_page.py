from appium.webdriver.common.mobileby import MobileBy
from app.po.page.base_page import BasePage
from app.po.page.contact_detail_brief_info_profile_page import ContactDetailBriefInfoProfilePage
from app.po.page.member_invite_menu_page import MemberInviteMenuPage


class AddressListPage(BasePage):
    def add_member(self):
        # 添加滚动查找添加成员，兼容成员比较多的时候要滑屏
        # self.driver.find_element(MobileBy.XPATH,"//*[@text='添加成员']").click()
        self.find_by_scroll("添加成员").click()
        return MemberInviteMenuPage(self.driver)

    def contact_detail_brief_info_profile(self, username):
        # 进入用户个人信息简介页
        self.find_and_click(MobileBy.XPATH, f"//*[@text='{username}']")
        return ContactDetailBriefInfoProfilePage(self.driver)

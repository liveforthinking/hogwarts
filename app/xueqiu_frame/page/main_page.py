from appium.webdriver.common.mobileby import MobileBy
from app.xueqiu_frame.page.base_page import BasePage
from app.xueqiu_frame.page.market_page import MarketPage


class MainPage(BasePage):
    def goto_MarketPage(self):
        '''
        进入行情
        :return:
        '''

        # 伪造一个弹窗
        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']").click()

        self.find_and_click(MobileBy.XPATH, "//*[@text='行情']")
        return MarketPage(self.driver)

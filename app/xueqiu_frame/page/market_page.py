from appium.webdriver.common.mobileby import MobileBy
from app.xueqiu_frame.page.base_page import BasePage
from app.xueqiu_frame.page.search_page import SearchPage


class MarketPage(BasePage):
    def goto_search(self):
        # self.find_and_click(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']")
        self.parse_yaml('../data/market.yaml', 'goto_search')
        return SearchPage(self.driver)

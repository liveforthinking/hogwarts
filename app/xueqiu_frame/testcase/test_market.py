from app.xueqiu_frame.page.app import App
from time import sleep


class TestMarket:
    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main_page()

    def teardown(self):
        sleep(10)
        # self.app.restart()

    def test_market(self):
        self.main.goto_MarketPage().goto_search().search()

from app.xueqiu_frame.page.base_page import BasePage


class SearchPage(BasePage):
    def search(self):
        self.parse_yaml("../data/search.yaml", "search")

from app.po.page.app import App


class TestAddressBook:
    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main_page()

    def teardown(self):
        self.app.stop()

    def test_contact_add(self):
        username = "username_009"
        gender = "女"
        phonenumber = "13500000009"
        result = self.main.goto_addresslist() \
            .add_member() \
            .add_member_by_manual() \
            .add_contact(username, gender, phonenumber).get_toast()
        assert result == "添加成功"

    def test_contact_delete(self):
        username = "username_009"
        self.main.goto_addresslist() \
            .contact_detail_brief_info_profile(username) \
            .contact_detail_setting().contact_edit() \
            .delete_member()

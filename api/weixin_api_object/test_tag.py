import datetime
import json

import pytest
import requests

# done: 与底层具体的实现框架代码耦合严重，无法适应变化，比如公司切换了协议，比如使用pb dubbo
# done: 代码冗余，需要封装
# done: 无法清晰的描述业务
# done: 使用jsonpath表达更灵活的递归查找
from jsonpath import jsonpath
from api.weixin_api_object.tag import Tag



class TestTag:
    def setup_class(self):
        self.tag = Tag()
        # 保存添加的tag_id, 用于数据清理
        self.tag_id_list_todo_del = []

    def teardown_class(self):
        # 数据清理
        if self.tag_id_list_todo_del != []:
            r = self.tag.delete(tag_id_list=self.tag_id_list_todo_del)
            assert not jsonpath(r.json(), f"$..[?(@.id=='{self.tag_id_list_todo_del[0]}')]")

    def test_get_tag(self):
        '''
        获取企业标签库
        :param tag_id:
        :param tag_name:
        :return:
        '''
        r = self.tag.list()

    @pytest.mark.parametrize("tag_id, tag_name", [
        ['etrlrmDQAAoLkW2g38X2HsrTGjBQw0CA', 'tag1_new_'],
    ])
    def test_edit_tag(self, tag_id, tag_name):
        '''
        编辑企业客户标签
        :param tag_id:
        :param tag_name:
        :return:
        '''
        tag_name = tag_name + str(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
        r = self.tag.list()
        r = self.tag.update(
            id=tag_id,
            tag_name=tag_name
        )
        r = self.tag.list()
        assert jsonpath(r.json(), f"$..[?(@.name=='{tag_name}')]")[0]['name'] == tag_name

    @pytest.mark.parametrize("group_name, tag_name", [
        ['tag_group1', 'add_tag1'],
        ['tag_group1', 'add_tag2'],
        ['tag_group1', 'add_tag3']
    ])
    def test_add_tag(self,group_name,tag_name):
        '''
        添加企业客户标签
        :param group_name:
        :param tag_name:
        :return:
        '''
        self.tag.add(group_name=group_name,tag_name=tag_name)
        r = self.tag.list()
        assert tag_name in jsonpath(r.json(), "$..name")

        # 把新增的tag_id保存到列表里，然后在teardwon里删除
        tag_id = jsonpath(r.json(), f"$..[?(@.name=='{tag_name}')]")[0]['id']
        self.tag_id_list_todo_del.append(tag_id)


    @pytest.mark.parametrize("tag_id_list", [
        [["etrlrmDQAAWY78yG7wYYbLwZJo0OwkKQ","etrlrmDQAA3mVhGuPy7Dd7IdrjyAhZjw"]]
    ])
    def test_del_tag(self,tag_id_list):
        '''
        删除企业客户标签
        :param tag_id:
        :param group_id:
        :return:
        '''
        r = self.tag.delete(tag_id_list=tag_id_list)
        assert not jsonpath(r.json(), f"$..[?(@.name=='{tag_id_list[0]}')]")


    def test_tag_list_fail(self):
        pass
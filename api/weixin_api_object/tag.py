import datetime
import json
from typing import List

import requests


class Tag:

    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        corpid = 'ww3c7cefe514396514'
        corpsecret = '2Xv-jU_GpDPyAkV2Ke69xg8itWXnzoxWcDNHZeYMW6c'

        r = requests.get(
            'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            params={'corpid': corpid, 'corpsecret': corpsecret}

        )
        print(json.dumps(r.json(), indent=2))
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

        token = r.json()['access_token']
        return token

    def add(self):
        pass

    def list(self):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
            params={"access_token": self.token},
            json={
                'tag_id': []
            }
        )

        print(json.dumps(r.json(), indent=2))
        return r

    def update(self, id, tag_name):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
            params={"access_token": self.token},
            json={
                'id': id,
                'name': tag_name
            }
        )
        print(json.dumps(r.json(), indent=2))
        return r

    def add(self, group_name, tag_name):
        '''
        添加企业客户标签
        :param group_name:
        :param tag_name:
        :return:
        '''
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
                          params={"access_token": self.token},
                          json={
                              "group_name": group_name,
                              "tag": [{
                                  "name": tag_name
                              }
                              ]
                          }
                          )
        print(json.dumps(r.json(), indent=2))
        return r

    def delete(self,tag_id_list: List = None,group_id_list: List = None):
        '''
        删除企业客户标签
        :param tag_id:
        :param group_id:
        :return:
        '''
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
                          params={"access_token": self.token},
                          json={
                              "tag_id": tag_id_list,
                              "group_id": group_id_list
                          }
                          )
        print(json.dumps(r.json(), indent=2))
        return r

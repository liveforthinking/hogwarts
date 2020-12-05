from hamcrest import *
from jsonpath import jsonpath
import requests


class TestRequests:
    def test_request(self):
        r = requests.get("http://httpbin.ceshiren.com/get")
        print(r.content)
        print(r.text)
        print(r.json())
        assert r.status_code == 200

    def test_query(self):
        payload = {
            "name": "Joshua",
            "gendar": "Male"
        }
        r = requests.get("http://httpbin.ceshiren.com/get", params=payload)
        print(r.text)
        assert r.status_code == 200

    def test_post(self):
        payload = {
            "name": "Joshua",
            "gendar": "Male"
        }
        r = requests.post("http://httpbin.ceshiren.com/post", data=payload)
        print(r.text)
        assert r.status_code == 200

    def test_json(self):
        r = requests.get("https://ceshiren.com/categories.json")
        assert r.status_code == 200
        # assert r.json()["category_list"]["categories"][0]["color"] == "0088CC"
        print(jsonpath(r.json(), '$..name'))

    def test_hamcrest(self):
        r = requests.get("https://ceshiren.com/categories.json")
        assert r.status_code == 200
        assert_that(r.status_code, equal_to(200))

      
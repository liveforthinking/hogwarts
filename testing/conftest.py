# conftest是共享公共的fixture的，自动import的方法

# @pytest.fixture(autouse=True,scope='function')
# #autous为True时，自动应用到每个方法里面,默认为False；scope默认就是function级别的，还有class/module/package/session

# 如果项目有多个conftest文件，调用的是最近的那个

import pytest

from pythoncode.caculator import Caculator


@pytest.fixture(scope='module')
def get_calc():
    calc = Caculator()
    print("【开始计算】")
    yield calc
    print("【计算结束】")


@pytest.fixture(scope='function', params=['Joshua', 'Tom'])
def login(request):
    # 相当于setup
    username = request.param
    print("登入")
    yield username
    # 相当于teardown
    print(("登出"))


@pytest.fixture()
def conn_db():
    print("连接数据库")
    yield
    print("关闭数据库")

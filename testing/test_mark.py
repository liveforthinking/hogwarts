import pytest


@pytest.mark.hogwarts
def test_env(env):
    print(f'你在命令行输入env的值是：{env}')

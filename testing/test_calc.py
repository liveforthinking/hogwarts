import pytest
from pythoncode.caculator import Caculator


class TestCaculator:

    def setup_class(self):
        print("setup_class...")

    def teardown_class(self):
        print("teardown_class...")

    def setup_method(self):
        self.calc = Caculator()
        print("setup_method...")

    def teardown_method(self):
        print("\nteardown_method...")

    @pytest.mark.parametrize('a,b,expect', [(1, 2, 3), (3, 3, 6), (5, 8, 13)],
                             ids=['test_add1', 'test_add2', 'test_add3'])
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        assert result == expect

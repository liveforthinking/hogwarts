import pytest
from pythoncode.caculator import Caculator


class TestCaculator:

    def setup_class(self):
        print("setup_class...")

    def teardown_class(self):
        print("teardown_class...")

    def setup_method(self):
        self.calc = Caculator()
        print("【开始计算】")

    def teardown_method(self):
        print("【计算结束】")

    @pytest.mark.parametrize('a,b,expect', [(1, 2, 3), (1, 1.4, 2.4), (8.8, 0.2, 9), (20, -12, 8),
                                            (9223372036854775807, 1, 9223372036854775808)],
                             ids=['int+int', 'int+float', 'float+float', 'integer+iegative', 'BigNumber'])
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        assert result == expect

    @pytest.mark.parametrize('x,div,expect',
                             [(1, 2, 0.5), (2, 0.5, 4), (8.8, 8.8, 1), (20, -2, -10), (1, 0, ZeroDivisionError)],
                             ids=['int/int', 'int/float', 'float/float', 'integer/iegative', 'Zero Division'])
    def test_div(self, x, div, expect):
        if div != 0:
            result = self.calc.div(x, div)
            assert result == expect
        if div == 0:
            with pytest.raises(ZeroDivisionError) as except_info:
                self.calc.div(x, div)
            assert except_info.type == expect

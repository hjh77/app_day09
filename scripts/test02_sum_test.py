import pytest
from base.getData import GetData


def get_sum_data():
    sum_list = []
    data = GetData().get_yaml_data("data4.yaml")
    for i in data.values():
        sum_list.append(tuple(i.values()))
    return sum_list


class TestSum:
    @pytest.mark.parametrize("a,b,c", get_sum_data())
    def test_sum(self, a, b, c):
        print(a, b, c)
        assert a + b == c

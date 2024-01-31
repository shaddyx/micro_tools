import dataclasses

from micro_tools import list_utils


@dataclasses.dataclass
class _TestEl:
    a: int
    b: str


def test_unique():
    lst = [1, 2, 3, 3, 5, 5, 1, 6]
    res = list_utils.unique(lst)
    assert res == [1, 2, 3, 5, 6]


def test_unique_with_comparator():
    def comparator(lst, x):
        for k in lst:
            if k[0] == x[0]:
                return False
        return True

    lst = [[1], [2], [3], [3], [5], [5], [1], [6]]
    res = list_utils.unique(lst, comparator=comparator)
    assert res == [[1], [2], [3], [5], [6]]


def test_unique_by_key():
    lst = [
        _TestEl(1, "1"),
        _TestEl(2, "2"),
        _TestEl(1, "3")
    ]
    res = list_utils.unique_by_key(lst, key_func=lambda x: x.a)
    assert len(res) == 2
    assert lst[0].b == '1'
    assert lst[1].b == '2'


def test_group_by():
    lst = [
        _TestEl(1, "1"),
        _TestEl(2, "2"),
        _TestEl(1, "3")
    ]
    res = list_utils.group_by(lst, group_by_func=lambda x: x.a)
    assert 1 in res
    assert 2 in res
    assert len(res) == 2
    assert len(res[1]) == 2
    assert len(res[2]) == 1

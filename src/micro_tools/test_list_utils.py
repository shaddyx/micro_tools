import types

from micro_tools import list_utils


def test_unique():
    res = list_utils.unique([1, 1, 2, 4, 3, 5, 6, 3, 2])
    assert res == [1, 2, 4, 3, 5, 6]


def test_unique_by_key():
    res = list_utils.unique_by_key([
        {
            "a": 1,
            "b": 5
        },
        {
            "a": 2,
            "b": 7
        },
        {
            "a": 1,
            "b": 7
        }
    ], lambda x: x["a"])
    assert res == [{'a': 1, 'b': 5}, {'a': 2, 'b': 7}]


def test_unique_by_key_gen():
    res = list_utils.unique_by_key_gen([
        {
            "a": 1,
            "b": 5
        },
        {
            "a": 2,
            "b": 7
        },
        {
            "a": 1,
            "b": 7
        }
    ], lambda x: x["a"])
    assert isinstance(res, types.GeneratorType)
    assert list(res) == [{'a': 1, 'b': 5}, {'a': 2, 'b': 7}]


def test_group_by():
    res = list_utils.group_by([
        {
            "a": 1,
            "b": 5
        },
        {
            "a": 2,
            "b": 7
        },
        {
            "a": 1,
            "b": 7
        }
    ], lambda x: x["a"])
    assert res == {1: [{'a': 1, 'b': 5}, {'a': 1, 'b': 7}], 2: [{'a': 2, 'b': 7}]}

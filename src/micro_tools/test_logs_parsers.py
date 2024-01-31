from micro_tools import logs_parsers


def test_find_value_between():
    res = logs_parsers.find_value_between("asdf erw: 12345 erwq", "asdf erw: ", " erwq")
    assert res == '12345'

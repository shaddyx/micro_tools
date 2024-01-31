import micro_tools.logs_parsers as logs_parsers

def test_find_value():
    res = logs_parsers.find_value("some data: vvva ttt:1234", "data", delimiter=": ", terminators=[" "])
    assert res == "vvva"

def test_find_value_ends_with_eol():
    res = logs_parsers.find_value("some data: vvvattt", "data", delimiter=": ", terminators=[" "])
    assert res == "vvvattt"
def test_find_value_unsuccessfull():
    res = logs_parsers.find_value("some data: vvva ttt:1234", "datay", delimiter=": ", terminators=[" "])
    assert res == None
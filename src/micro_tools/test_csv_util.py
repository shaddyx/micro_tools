import os

import tempfile

from micro_tools import csv_util


def test_get_cols():
    res = csv_util.get_cols({
        "a": 1,
        "b": 2
    })
    assert res == ['a', 'b']


def test_write_csv():
    f = tempfile.mktemp()
    csv_util.write_csv(f, [{
        "a": 1,
        "b": 2
    },
        {
            "a": 3,
            "c": 4
        }
    ], write_header=False)
    assert open(f).read() == "1,2\n3,\n"
    os.remove(f)


def test_write_csv_with_header():
    f = tempfile.mktemp()
    csv_util.write_csv(f, [{
        "a": 1,
        "b": 2
    },
        {
            "a": 3,
            "c": 4
        }
    ], write_header=True)
    assert open(f).read() == "a,b\n1,2\n3,\n"
    os.remove(f)

def test_write_csv_with_header_asterisk_delimiter():
    f = tempfile.mktemp()
    csv_util.write_csv(f, [{
        "a": 1,
        "b": 2
    },
        {
            "a": 3,
            "c": 4
        }
    ], write_header=True, delimiter='*')
    assert open(f).read() == "a*b\n1*2\n3*\n"
    os.remove(f)



def test_read_csv_with_no_header():
    f = tempfile.mktemp()
    csv_util.write_csv(f, [{
        "a": 1,
        "b": 2
    },
        {
            "a": 3,
            "c": 4
        }
    ], write_header=True)
    result = list(csv_util.read_csv(f, read_headers=False))
    assert result == [['a', 'b'], ['1', '2'], ['3', '']]
    os.remove(f)

def test_read_csv_with_no_header_semicolon_delimiter():
    f = tempfile.mktemp()
    csv_util.write_csv(f, [{
        "a": 1,
        "b": 2
    },
        {
            "a": 3,
            "c": 4
        }
    ], write_header=True, delimiter=';')
    result = list(csv_util.read_csv(f, read_headers=False, delimiter=';'))
    assert result == [['a', 'b'], ['1', '2'], ['3', '']]
    os.remove(f)


def test_read_csv_with_header():
    f = tempfile.mktemp()
    csv_util.write_csv(f, [{
        "a": 1,
        "b": 2
    },
        {
            "a": 3,
            "c": 4
        }
    ], write_header=True)
    result = list(csv_util.read_csv(f, read_headers=True))
    assert result == [{'a': '1', 'b': '2'}, {'a': '3', 'b': ''}]
    os.remove(f)

import os

from micro_tools import env_helper


def test_has_value():
    env_helper.del_value("AAAAA")
    assert not env_helper.has_value("AAAAA")
    os.environ["AAAAA"] = "123123"
    assert env_helper.has_value("AAAAA")
    env_helper.del_value("AAAAA")


def test_get_value():
    os.environ["AAAAB"] = "123123"
    assert env_helper.get_value("AAAAB") == "123123"
    env_helper.del_value("AAAAB")

import os


def has_value(name: str) -> bool:
    return name in os.environ


def get_value(name: str, default=None):
    return os.environ[name] if has_value(name) else default


def del_value(name: str):
    if name in os.environ:
        del os.environ[name]

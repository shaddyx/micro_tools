import dataclasses
import time

from micro_tools.sqlte_cache import SqliteCache, sqlite_cache_decorator

__cache = SqliteCache()


@dataclasses.dataclass
class __TestData:
    s: str
    d: int


class __Semaphore:
    s = False


def test_get():
    d = __TestData("123", 345)
    __cache.set("testKey", d)
    res = __cache.get("testKey")
    assert d == res

    res = __cache.get("testKey1")
    assert res is None

    __cache.set("testKey", None)
    res = __cache.get("testKey")
    assert res is None

def test_multiple_vals():
    for k in range(1, 1000):
        __cache.set(f"v_{k}", k)
    for k in range(1, 1000):
        assert k == __cache.get(f"v_{k}")


def test_sqlite_cache_decorator():
    d = __TestData("123", 345)

    @sqlite_cache_decorator(expire_seconds=1)
    def func(a, b):
        __Semaphore.s = True
        return a + b

    __Semaphore.s = False
    res = func(1, 2)
    assert res == 3
    assert __Semaphore.s

    __Semaphore.s = False
    res = func(1, 2)
    assert res == 3
    assert not __Semaphore.s

    time.sleep(1)
    func(1, 2)
    assert __Semaphore.s


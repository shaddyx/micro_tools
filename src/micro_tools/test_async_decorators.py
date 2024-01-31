import time

from micro_tools.async_decorator import Async, await_all_async


@Async()
def some_func(k):
    time.sleep(0.3)
    return "result of " + str(k)
def test_async():
    futures = [some_func(k) for k in range(10)]
    res = await_all_async(futures)
    assert res == ['result of 0', 'result of 1', 'result of 2', 'result of 3', 'result of 4', 'result of 5', 'result of 6', 'result of 7', 'result of 8', 'result of 9']


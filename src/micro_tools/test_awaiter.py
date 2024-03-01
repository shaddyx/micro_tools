import time

from micro_tools.awaiter import Awaiter

def test_with_params():
    class _TestStorage:
        value = 0

    def try_func():
        _TestStorage.value += 1
        print("try: " + str(_TestStorage.value))
        raise Exception("1111")
    t1 = time.time()
    try:
        Awaiter(5, 0.1).with_exponential_backoff(1.5).with_delay_func(lambda x: time.sleep(x)).exec(try_func)
        assert False
    except Exception:
        pass

    t2 = time.time()
    assert _TestStorage.value == 5
    assert (t2 - t1) >= 0.5
    assert (t2 - t1) <= 1

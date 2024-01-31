from concurrent.futures import ThreadPoolExecutor, Future
from functools import wraps


def Async(max_threads: int = 10):
    executor = ThreadPoolExecutor(max_workers=max_threads)
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return executor.submit(func, *args, **kwargs)

        return wrapper

    return decorator


def await_all_async(async_futures: list[Future]) -> list:
    return [future.result() for future in async_futures]

import typing


class Awaiter:

    def __init__(self, tries=1, delay: float = 0):
        self.exponential_backoff = None
        self.retries = tries
        self.delay = delay
        self.delay_func: typing.Optional[typing.Callable[[float], None]] = None

    def with_delay_func(self, delay_func):
        self.delay_func = delay_func
        return self

    def with_exponential_backoff(self, base: float):
        self.exponential_backoff = base
        return self

    def exec(self, fn, *args, **kwargs):
        try_number = 0
        while True:
            try:
                return fn(*args, **kwargs)
            except Exception as e:
                try_number += 1
                if try_number >= self.retries:
                    raise e
                if self.delay_func is not None:
                    self.delay_func(self.delay)
                if self.exponential_backoff is not None:
                    self.delay *= self.exponential_backoff

    async def a_exec(self, fn, *args, **kwargs):
        try_number = 0
        while True:
            try:
                return await fn(*args, **kwargs)
            except Exception as e:
                try_number += 1
                if try_number >= self.retries:
                    raise e
                if self.delay_func is not None:
                    await self.delay_func(self.delay)
                    if self.exponential_backoff is not None:
                        self.delay *= self.exponential_backoff

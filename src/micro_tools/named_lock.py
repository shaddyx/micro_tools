import threading


class _UnLocker:
    def __init__(self, parent: "NamedPessimisticLock", name: str) -> None:
        self.name = name
        self.parent = parent
        super().__init__()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.parent.release(self.name)


class NamedPessimisticLock:

    def __init__(self):
        self._locks = {}
        self._global_lock = threading.Lock()

    def acquire(self, name: str):
        self._global_lock.acquire()
        try:
            if name not in self._locks:
                self._locks[name] = threading.Lock()
            self._locks[name].acquire()
            return _UnLocker(self, name)
        finally:
            self._global_lock.release()

    def release(self, name: str):
        self._global_lock.acquire()
        try:
            if name in self._locks:
                self._locks[name].release()
                del self._locks[name]
        finally:
            self._global_lock.release()

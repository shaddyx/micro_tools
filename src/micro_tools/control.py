class Once:
    def __init__(self):
        self._called = False

    def check(self):
        if not self._called:
            self._called = True
            return True
        return False

    def reset(self):
        self._called = False


class Multiple:
    def __init__(self, value):
        self._value = value + 1
        self._initial_value = value + 1

    def check(self):
        if self._value == 0:
            return False
        self._value -= 1
        return self._value == 0

    def reset(self):
        self._value = self._initial_value

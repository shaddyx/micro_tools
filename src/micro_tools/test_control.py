from micro_tools import control


def test_check():
    a = control.Once()
    assert a.check()
    assert not a.check()
    assert not a.check()


def test_check_multiple():
    m = control.Multiple(3)
    assert not m.check()
    assert not m.check()
    assert not m.check()
    assert m.check()
    assert not m.check()


def test_reset():
    m = control.Multiple(3)
    assert not m.check()
    assert not m.check()
    assert not m.check()
    assert m.check()
    m.reset()
    assert not m.check()
    assert not m.check()
    assert not m.check()
    assert m.check()

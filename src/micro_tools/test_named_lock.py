from micro_tools.named_lock import NamedPessimisticLock


def test_acquire():
    l = NamedPessimisticLock()
    with l.acquire("test"):
        assert "test" in l._locks
    assert "test" not in l._locks


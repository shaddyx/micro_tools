from micro_tools import date_util


def test_ts_to_iso():
    res = date_util.ts_to_iso(1678633390430)
    assert res == "2023-03-12T15:03:10.430000+00:00"


def test_iso_to_ts():
    assert date_util.iso_to_ts("2023-03-12T15:03:10.430000+00:00") == 1678633390430
    assert date_util.iso_to_ts("2023-03-12T15:03:10.430000+20:00") == 1678561390430
    assert date_util.iso_to_ts("2023-01-06T15:05:32.688Z") == 1673017532688


def test_iso_to_ts_with_no_t():
    assert date_util.iso_to_ts("2023-03-12 17:03:10") == 1678640590000
    assert date_util.iso_to_ts("2023-03-12 15:03:10.430000+00:00") == 1678633390430
    assert date_util.iso_to_ts("2023-03-12 15:03:10.430000+20:00") == 1678561390430


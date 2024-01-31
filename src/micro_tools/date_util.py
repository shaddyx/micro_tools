import time
from datetime import datetime, timezone


def ts_to_iso(ts: int, tz=timezone.utc) -> str:
    dt = datetime.fromtimestamp(int(ts) / 1000, tz=tz)
    return dt.isoformat()


def iso_to_ts(iso: str) -> int:
    iso = iso.strip()
    if iso[-1] == "Z":
        iso = iso[:-1]
    if "+" not in iso and "-" not in iso[-6:]:
        iso += "+00:00"
    dt = datetime.fromisoformat(iso)
    return int(datetime.timestamp(dt) * 1000)


def current_time_millis() -> int:
    return round(time.time() * 1000)

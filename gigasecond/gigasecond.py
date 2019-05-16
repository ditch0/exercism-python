from datetime import datetime, timedelta

_GIGASECOND = timedelta(seconds=1_000_000_000)


def add_gigasecond(moment: datetime) -> datetime:
    return moment + _GIGASECOND

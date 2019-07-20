from datetime import datetime

from dateutil.parser import parse

def test_parser():
    assert parse('23APR2019') == datetime(2019, 4, 23)

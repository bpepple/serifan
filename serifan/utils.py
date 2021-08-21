from datetime import datetime
from typing import List


def list_strings_to_dates(lst):
    # One of the string dates in the api has a period at the end.
    return [datetime.strptime(d.strip("."), "%Y-%m-%d").date() for d in lst["dates"]]

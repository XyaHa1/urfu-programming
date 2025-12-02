import datetime
from collections import Counter
from typing import List


def most_common_months(dates: List[str], n) -> List[int]:
    months = []
    for date_str in dates:
        dt = datetime.datetime.fromisoformat(date_str)
        months.append(dt.month)

    counter = Counter(months)
    most_common = counter.most_common(n)
    return [month for month, _ in most_common]

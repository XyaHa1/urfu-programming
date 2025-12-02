from collections import defaultdict
from typing import List, Tuple


def fill_specializations(specializations: List[Tuple[str, str]]):
    result = defaultdict(list)
    for spec, name in specializations:
        result[spec].append(name)
    return dict(result)

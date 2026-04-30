from typing import List
from enum import Enum


class Date(Enum):
    MIN_MONTH = 1
    MAX_MONTH = 12

    MIN_YEAR = 1
    MAX_YEAR = 9999

class DateFormat(Enum):
    EU = "EU"  # DDMMYYYY
    US = "US"  # MMDDYYYY

class NumberOfDays(Enum):
    MIN_DAYS = 0
    MAX_DAYS = 3651694


months_with_days = [
    0,  # placeholder for 0 index
    31, # January
    28, # February
    31, # March
    30, # April
    31, # May
    30, # June
    31, # July
    31, # August
    30, # September
    31, # October
    30, # November
    31, # December
    ]


def validate_date_string(date_str: str) -> None:
    if not date_str.isdigit():
        raise ValueError("Expected: digits")

    if len(date_str) < 8:
        if NumberOfDays.MIN_DAYS.value <= int(date_str) < NumberOfDays.MAX_DAYS.value:
            return
        raise ValueError("Expected: valid date")

    year = int(date_str[-4:])
    if Date.MIN_YEAR.value > year:
        raise ValueError("Expected: 1 <= year <= 9999")
    

def validate_number_of_days(days: int, format: str) -> None:
    if not isinstance(days, int):
        raise ValueError("Expected: integer")
    if not NumberOfDays.MIN_DAYS.value <= days <= NumberOfDays.MAX_DAYS.value:
        raise ValueError("Expected: 0 <= days <= 3651694")
    if format not in (DateFormat.EU.value, DateFormat.US.value):
        raise ValueError("Expected: EU or US")


def to_days(date_str: str) -> List[int]:
    variants = parse_date_string(date_str)

    if len(variants) == 1 and all(v is None for v in variants[0][1:]):
        # if the input is a number of days, we can just return it as is, since it already represents the number of days since epoch
        return [variants[0][0]]

    is_leap = is_leap_year(variants[0][2])

    result = []
    for v in variants:
        curr_days_to_era = 0
        for month in range(1, v[1]):
            curr_days_to_era += months_with_days[month]
            if month == 2 and is_leap:
                curr_days_to_era += 1
        curr_days_to_era += v[0] - 1  # add days of current month
        curr_days_to_era += (v[2] - 1) * 365  # add days of previous years

        curr_days_to_era += (v[2] - 1) // 4  # add leap days
        curr_days_to_era -= (v[2] - 1) // 100  # remove non-leap centuries
        curr_days_to_era += (v[2] - 1) // 400  # add back leap centuries

        result.append(curr_days_to_era)
    
    if len(result) == 2 and result[0] == result[1]:
        return [result[0]]
    
    return result

        
def from_days(days: int, format: str = "EU") -> str:
    validate_number_of_days(days, format)
    
    year = 1
    while True:
        days_in_year = 366 if is_leap_year(year) else 365
        if days < days_in_year:
            break
        days -= days_in_year
        year += 1

    month = 1
    is_leap = is_leap_year(year)
    for i in range(1, 13):
        days_in_month = months_with_days[i]
        if i == 2 and is_leap:
            days_in_month += 1
        if days < days_in_month:
            month = i
            break
        days -= days_in_month

    day = days + 1
    if format == DateFormat.EU.value:
        # EU: DDMMYYYY
        return f"{day:02d}{month:02d}{year:04d}"
    elif format == DateFormat.US.value:
        # US: MMDDYYYY
        return f"{month:02d}{day:02d}{year:04d}"


def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def parse_format(date_str: str, format: DateFormat) -> str:    
    if format == DateFormat.EU.value:
        month_index = (2, 4)
        days_index = (0, 2)
    elif format == DateFormat.US.value:
        month_index = (0, 2)
        days_index = (2, 4)
    else:
        raise ValueError("Expected: EU or US")
    
    year = int(date_str[-4:])
    is_leap = is_leap_year(year)


    result = ()
    if Date.MIN_MONTH.value <= (month := int(date_str[month_index[0]:month_index[1]])) <= Date.MAX_MONTH.value:
        exp_days = months_with_days[month]
        if month == 2 and is_leap:
            exp_days += 1
        if exp_days >= (days := int(date_str[days_index[0]:days_index[1]])) >= 1:
            result = (days, month, year)

    if year >= Date.MAX_YEAR.value:
        if result and (result[1] != Date.MIN_MONTH.value or result[0] != 1):
            raise ValueError("Expected: 01.01.0001 <= date <= 01.01.9999")

    return result


def parse_date_string(date_str: str) -> List[tuple[int, int, int]]:
    validate_date_string(date_str)

    if len(date_str) < 8:
        return [(int(date_str), None, None)]

    result = []
    for format in (DateFormat.US.value, DateFormat.EU.value):
        parsed = parse_format(date_str, format)
        if parsed:
            result.append(parse_format(date_str, format))
    
    if not result:
        raise ValueError("Expected: valid date. Expected formats: DDMMYYYY, MMDDYYYY")
    
    return result
    

if __name__ == "__main__":
    # print(to_days("01019999"))
    # print(from_days(738878, "EU")) # → "25122023"
    # print(from_days(738878, "US")) # → "12252023"
    invalid_dates = [
            "32122023",
            "31042023",
            "00122023",
            "12002023",
            "12332023",
            "abcdefgh",
            "",
            "00000000",
            "-738524"
        ]
    for date in invalid_dates:
        try:
            print(to_days(date))
        except ValueError as e:
            print(f"Invalid date: {date}. Error: {e}")
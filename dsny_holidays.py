from datetime import timedelta


def holiday_registry():
    """
    Provides a decorator which can be used to "register" holiday functions for easy iteration later
    """
    all_holidays = []

    def registrar(func):
        all_holidays.append(func)
        return func

    registrar.all_holidays = all_holidays
    return registrar


HOLIDAY_CHECKERS = holiday_registry()


@HOLIDAY_CHECKERS
def _is_new_years_day(collection_date):
    # Jan 1. Happy New Year!
    if collection_date.month == 1:
        if collection_date.day == 1:
            return True, 'New Years Day'
        # Observed on Monday the 2nd if NYD falls on a Sunday
        elif collection_date.day == 2 and collection_date.weekday() == 0:
            return True, 'New Years Day'

    elif all([collection_date.month == 12, collection_date.day == 31, collection_date.weekday() == 4]):
        # Observed on Friday the 31 if NYD falls on a Saturday
        return True, 'New Years Day'

    return False, 'New Years Day'


@HOLIDAY_CHECKERS
def _is_mlk_day(collection_date):
    # MLK Day is the third Monday of January each year
    if collection_date.month == 1:
        if collection_date.weekday() == 0:
            # Date must be between the 15th and 21st
            return 15 <= collection_date.day <= 21, 'Martin Luther King Day'

    return False, 'Martin Luther King Day'


@HOLIDAY_CHECKERS
def _is_lincoln_bday(collection_date):
    # Feb 12 each year
    if collection_date.month == 2:
        if collection_date.day == 12:
            return True, "Abraham Lincoln's Birthday"
        elif collection_date.day == 11 and collection_date.weekday() == 4:
            return True, "Abraham Lincoln's Birthday"
        elif collection_date.day == 13 and collection_date.weekday() == 0:
            return True, "Abraham Lincoln's Birthday"

    return False, "Abraham Lincoln's Birthday"


@HOLIDAY_CHECKERS
def _is_presidents_day(collection_date):
    # Presidents' Day is the third Monday of February each year
    if collection_date.month == 2:
        if collection_date.weekday() == 0:
            # Date must be between the 15th and 21st
            return 15 <= collection_date.day <= 21, "Presidents' Day"

    return False, "Presidents' Day"


@HOLIDAY_CHECKERS
def _is_memorial_day(collection_date):
    # Memorial Day is the last Monday in May each year
    if collection_date.month == 5:
        if collection_date.weekday() == 0:
            # Date must be between the 25th and 31st
            return collection_date.day >= 25, 'Memorial Day'

    return False, 'Memorial Day'


@HOLIDAY_CHECKERS
def _is_independence_day(collection_date):
    # July 4
    if collection_date.month == 7:
        if collection_date.day == 4:
            return True, 'Independence Day'
        # 4oJ is Saturday, holiday observed on Friday
        elif collection_date.day == 3 and collection_date.weekday() == 4:
            return True, 'Independence Day'
        # 4oJ is Sunday, holiday observed on Monday
        elif collection_date.day == 5 and collection_date.weekday() == 0:
            return True, 'Independence Day'

    return False, 'Independence Day'


@HOLIDAY_CHECKERS
def _is_labor_day(collection_date):
    # Labor Day is the first Monday of September each year
    if collection_date.month == 9:
        if collection_date.weekday() == 0:
            # Date must be between the 1st and 7th
            return 1 <= collection_date.day <= 7, 'Labor Day'

    return False, 'Labor Day'


@HOLIDAY_CHECKERS
def _is_columbus_day(collection_date):
    # Columbus Day is the second Monday of October each year
    if collection_date.month == 10:
        if collection_date.weekday() == 0:
            # Date must be between the 8th and 14th
            return 8 <= collection_date.day <= 14, "Indigenous Peoples' Day"

    return False, "Indigenous Peoples' Day"


@HOLIDAY_CHECKERS
def _is_election_day(collection_date):
    # Election Day is the first Tuesday after the first Monday in November
    if collection_date.month == 11:
        # weekday 1 is Tuesday
        if collection_date.weekday() == 1:
            # Date must be between the 2nd and 8th
            return 2 <= collection_date.day <= 8, 'Election Day'

    return False, 'Election Day'


def _election_day_was_earlier_in_week(collection_date):
    for days_ago in range(collection_date.weekday(), 0, -1):
        is_election_day, _ = _is_election_day(collection_date - timedelta(days_ago))
        if is_election_day:
            return True

    return False


@HOLIDAY_CHECKERS
def _is_veterans_day(collection_date):
    """
    Veterans Day is on Nov 11. If Saturday, observed Friday. If Sunday, observed Monday.
    NOT observed if election day is same week.
    """
    if collection_date.month == 11:
        # Check if this is Veterans Day or the Friday before Veterans Day
        if collection_date.day == 11 or (collection_date.day == 10 and collection_date.weekday() == 4):
            # Check earlier in the week for election day
            if not _election_day_was_earlier_in_week(collection_date):
                return True, 'Veterans Day'

        # Check whether this is the Monday after Veterans Day
        if collection_date.day == 12 and collection_date.weekday() == 0:
            return True, 'Veterans Day'

    return False, 'Veterans Day'


@HOLIDAY_CHECKERS
def _is_thanksgiving_day(collection_date):
    # Thanksgiving Day is the fourth Thursday in November each year
    if collection_date.month == 11:
        # weekday 3 is Thursday
        if collection_date.weekday() == 3:
            # Date must be between the 22nd and 28th
            return 22 <= collection_date.day <= 28, 'Thanksgiving Day'

    return False, 'Thanksgiving Day'


@HOLIDAY_CHECKERS
def _is_christmas_day(collection_date):
    # December 25
    if collection_date.month == 12:
        if collection_date.day == 25:
            return True, 'Christmas Day'
        elif collection_date.day == 24 and collection_date.weekday() == 4:
            return True, 'Christmas Day'
        elif collection_date.day == 26 and collection_date.weekday() == 0:
            return True, 'Christmas Day'

    return False, 'Christmas Day'


def is_dsny_holiday(collection_date):
    for day_checker in HOLIDAY_CHECKERS.all_holidays:
        is_holiday, holiday_name = day_checker(collection_date)
        if is_holiday:
            return True, holiday_name

    return False, ''

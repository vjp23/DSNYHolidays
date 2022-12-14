# DSNY Holidays
Python code to determine whether a given date is a New York Department of Sanitation (DSNY) holiday.

Note that this code will NOT indicate whether DSNY is picking up on a given day, as there are other factors that they use to determine this. For example, if there's a blizzard preventing collection between two holidays, there may be collection on the second holiday to avoid a backlog.

With that said, the DSNY holiday calendar is nontrivial, so I hope that this will be of some use. 

I expect that this will be primarily useful for New York City residents.

## Usage

```
from datetime import date
from dsny_holidays import is_dsny_holiday


new_years_day = date(2021, 1, 1)
is_holiday, holiday_name = is_dsny_holiday(new_years_day)

print(is_holiday)
>> True

print(holiday_name)
>> New Years Day
```

### References
https://dsnyfamily.com/dsny-holidays/

https://www1.nyc.gov/assets/dsny/site/services/waste-page/holiday-schedule

### TODO
1. Add a function to return the next pickup date that is NOT a holiday following a specified pickup date, given a pickup schedule and a collection type (refuse vs recycling vs, if possible, organics)
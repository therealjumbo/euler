#!/usr/bin/python3

import datetime

# start on the first day of the 20th century
cur_date = datetime.date(year=1901, month=1, day=1)
# end on the last day of the 20th century, inclusive
end_date = datetime.date(year=2000, month=12, day=31)

count = 0
while(cur_date <= end_date):
    if (cur_date.day == 1) and (cur_date.weekday() == 6):
        count += 1

    cur_date += datetime.timedelta(days=1)

print(count)

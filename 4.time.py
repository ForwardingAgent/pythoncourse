def add_time(start, duration, day=None):
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    st = start[:-3].split(':')
    du = duration.split(':')
    am_pm = start[-3:]
    hours = int(st[0]) + int(du[0])
    min = int(st[1]) + int(du[1])
    next_day = 0
    days_plus = None
    if min > 60:
        hours_up = min // 60
        hours += hours_up
        min = min % 60
    if min < 10:
        min = '0' + str(min)
    if hours >= 12:
        if hours > 12:
            hours_above = hours % 12 # 12
            if hours_above == 0 and int(min) > 0:
                hours_above = 12
                next_day = 1
            if int(du[0]) >= 24:
                days_plus = (int(du[0]) // 24) + next_day
                min_plus = (int(du[0]) / 24)
                min_plus = round(min_plus, 2) % 1 * 100 // 1
                if int(min_plus) + int(min) >= 60:
                    days_plus += 1
            #hours_above = hours % 12
            #if hours_above > 6:
            #    days_plus += 1
            hours = hours_above
        if (int(du[0]) + int(du[1])) == 24:
            if am_pm == ' AM':
                am_pm = ' AM (next day)'
            else:
                am_pm = ' PM (next day)'
        elif 12 < (int(st[0]) +int(du[0])) < 24:
            if am_pm == ' AM':
                am_pm = ' PM'
            else:
                am_pm = ' AM (next day)'
        else:
            if am_pm == ' AM':
                am_pm = ' PM'
            else:
                am_pm = ' AM'
    if day is not None and days_plus == 1:
        new_time = (f'{hours}:{min}{am_pm[:3]}, {week[week.index(day.title()) + 1]}{am_pm[3:]}')
    elif day is not None and days_plus != None:
      if days_plus > 7:
        new_time = (f'{hours}:{min}{am_pm[:3]}, {week[week.index(day.title()) + (days_plus % 7 - 7)]} ({days_plus} days later)')
      else:
        new_time = (f'{hours}:{min}{am_pm[:3]}, {week[week.index(day.title()) + days_plus]} ({days_plus} days later)')
    elif day is None and days_plus is None:
        new_time = (f'{hours}:{min}{am_pm}')
    elif day is None and days_plus == 1:
        new_time = (f'{hours}:{min}{am_pm}')
    elif days_plus is None:
        new_time = (f'{hours}:{min}{am_pm}, {day.title()}')
    elif day is None:
        new_time = (f'{hours}:{min}{am_pm} ({days_plus} days later)')
    else:
        new_time = (f'{hours}:{min}{am_pm}, {day.title()} ({days_plus} days later)')
    return new_time

#print(add_time("3:00 PM", "3:10"))
# Returns: 6:10 PM

#print(add_time("11:30 AM", "2:32", "Monday"))
# Returns: 2:02 PM, Monday

#print(add_time("11:43 AM", "00:20"))
# Returns: 12:03 PM

#print(add_time("10:10 PM", "3:30"))
# Returns: 1:40 AM (next day)

#print(add_time("11:43 PM", "24:20", "tueSday"))
# Returns: 12:03 AM, Thursday (2 days later)

#print(add_time("6:30 PM", "205:12"))
# Returns: 7:42 AM (9 days later)
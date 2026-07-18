
import datetime as dt

current = dt.datetime.now()
# print(type(current))
# print(current.day)
# print(current.date())
# print(current.time())
# print(current.minute)

set_date = dt.datetime(2027, 10, 10, 10, 30)
# print(set_date)

# print(set_date.year - current.year)
print(current + dt.timedelta(days=25))

# converting string to datetime

# Token	Meaning	Example
# %Y	Year (4 digits)	2026
# %y	Year (2 digits)	26
# %m	Month (zero-padded)	07
# %-m*	Month (no leading zero, Unix only)	7
# %B	Full month name	July
# %b / %h	Abbreviated month name	Jul
# %d	Day of month (zero-padded)	12
# %-d*	Day of month (no leading zero, Unix only)	7
# %A	Full weekday name	Sunday
# %a	Abbreviated weekday name	Sun
# %w	Weekday as number (0=Sunday)	0
# %H	Hour (24-hour, zero-padded)	14
# %I	Hour (12-hour, zero-padded)	02
# %p	AM/PM	PM
# %M	Minute (zero-padded)	05
# %S	Second (zero-padded)	09
# %f	Microsecond (zero-padded, 6 digits)	123456
# %z	UTC offset	+0100
# %Z	Time zone name	WAT
# %j	Day of year (001–366)	194
# %U	Week number (Sunday first day)	27
# %W	Week number (Monday first day)	27
# %c	Locale’s date and time	Sun Jul 12 14:05:09 2026
# %x	Locale’s date	07/12/26
# %X	Locale’s time	14:05:09
# %%	Literal %	%



# str_date = "2009/09/23"
# date_obj = dt.datetime.strptime(str_date, "%Y/%m/%d")
# print(date_obj)

# dob = input("DOB YYYY/MM/DD: ")
# date_obj = dt.datetime.strptime(dob, "%Y/%m/%d")
# print(f"Age: {current.year - date_obj.year}yrs")


# converting datetime to string

# print(current.strftime('%d/%m/%Y, %H:%M:%S%p'))


#  build an alarm/schedule app



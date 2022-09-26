# Utilities for calculation of NPMRDS travel-time reliability metrics
#
import datetime

tstamp = "1/2/2019 10:15"

# Parse 'date' part of measurement_tstamp field
tmp = tstamp.split(' ')
datepart = tmp[0]
timepart = tmp[1]
tmp2 = datepart.split('/')
mo = int(tmp2[0])
dy = int(tmp2[1])
yr = int(tmp2[2])
# Determine day-of-week
dtemp = datetime.date(yr, mo, dy)
# The following call returns 0 - 6, for Mon - Sun
dowtmp = dtemp.weekday()
day_of_week = 'weekend' if (dowtmp == 5 or dowtmp == 6) else 'weekday'

# Parse 'time' component of measurement_tstamp field
tm = s2[1].split(':')
hour = int(tm[0])


# Enums for NHPP_Periods:
nhpp_none = 0
nhpp_weekday_6_10 = 1
nhpp_weekday_10_4 = 2
nhpp_weekday_4_8 =  3
nhpp_weekend_6_8 =  4

# Determine NHPP_Period: the value returned depends upon day_of_week and hour.
# Note that 'hour' values are given using the 24-hour (not 12-hour) clock.
def get_nhpp_period(day_of_week, hour):
	retval = 0
	if day_of_week == 'weekend' and hour >=6 and hour < 20:
		retval = nhpp_weekend_6_8
	elif hour >=6 and hour < 10:
		retval = nhpp_weekday_6_10
	elif hour >= 10 and hour < 16:
		retval = nhpp_weekday_10_4
	elif hour >= 16 and hour < 20:
		retval = nhpp_weekday_4_8
	else:
		retval = nhpp_none
	# endif
	return retval
# end_def get_nhpp_period()
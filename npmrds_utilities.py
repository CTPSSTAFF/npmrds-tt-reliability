# Utilities for calculation of NPMRDS travel-time reliability metrics
#
import datetime

tstamp = "2019-01-02 10:15"

# Parse 'date' part of measurement_tstamp field
tmp = tstamp.split(' ')
datepart = tmp[0]
timepart = tmp[1]
tmp2 = datepart.split('-')
mo = int(tmp2[1])
dy = int(tmp2[2])
yr = int(tmp2[0])
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
def get_nhpp_period(dow, hour):
	retval = 0
	if (dow == 5 or dow == 6):
		if hour >=6 and hour < 20:
			retval = nhpp_weekend_6_8
		else:
			retval = nhpp_none
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


ritis_df['datepart'] = ritis_df.apply(lambda row : row['measurement_tstamp'].split(' ')[0], axis=1)
ritis_df['timepart'] = ritis_df.apply(lambda row : row['measurement_tstamp'].split(' ')[1], axis=1)
ritis_df['mo'] = ritis_df.apply(lambda row : int(row['datepart'].split('-')[1]), axis=1)
ritis_df['dy'] = ritis_df.apply(lambda row : int(row['datepart'].split('-')[2]), axis=1)
ritis_df['dow'] = ritis_df.apply(lambda row : datetime.date(2019, row['mo'], row['dy']).weekday(), axis=1)
ritis_df['hour'] = ritis_df.apply(lambda row: int(row['timepart'].split(':')[0]), axis=1)
ritis_df['nhpp_period'] = ritis_df.apply(lambda row : get_nhpp_period(row['dow'], row['hour']), axis=1)


g50 = ritis_df.groupby('tmc_code')['travel_time_seconds'].quantile(q=0.5)
g80 = ritis_df.groupby('tmc_code')['travel_time_seconds'].quantile(q=0.8)

# import pandas as pd
#
# df = pd.read_csv('chicago.csv',
#                  usecols=['Start Time', 'End Time', 'Trip Duration', 'Start Station', 'End Station', 'User Type'])
#
# # print(df)
# # print(df['Start Time'].to_datetime())
#
# df['Start Time'] = pd.to_datetime(df['Start Time'])
#
# print(df['Start Time'].dt.day_name())
# print(df['Start Time'].dt.month)
# print(df['Start Time'].dt.hour)
#
import datetime
import time
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']
# print(MONTHS[5])

num = 5

print(datetime.datetime.strptime(str(num),'%m').strftime('%B'))
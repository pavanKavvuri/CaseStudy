import pandas as pk
import numpy as np

# df = pk.read_excel("/home/tcs/Desktop/pavan_guest/neway.xlsx", sheetname=0)   #dat.dropna(how='any')
df = pk.read_excel(
    '/home/pavan/PAVANKUMAR/MachineLearning/CaseStudy/ML_DATA/v4/k5/FinalFiles/Data_Sorted_nan_dupl.xlsx', sheetname=0)
D = []
WeekList = []
WeekLabels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

CinList = df.CheckInDate.unique()


D.append(df.CheckInDate.unique().dt.weekday.values)
# print df.CheckOutDate.dt.weekday
print len(D[0])


def f(l):
    WeekList.append(WeekLabels[l])

map(f, D[0])

print WeekList

'''

df.CheckinTime = pk.to_datetime(df['CheckinTime'])
df.CheckoutTime = pk.to_datetime(df['CheckoutTime'])


h = np.timedelta64(1, 'h')

Duration = lambda x: round((np.datetime64(df.CheckoutTime[x]) - np.datetime64(df.CheckinTime[x]))/h)

CheckInHour = lambda x: df.CheckinTime[x].hour
CheckInDate = lambda x: df.CheckinTime[x].date()

CheckOutHour = lambda x: df.CheckoutTime[x].hour
CheckOutDate = lambda x: df.CheckoutTime[x].date()



CinDat = map(CheckInDate, range(0,len(df)))

CinHr = map(CheckInHour, range(0,len(df)))

CoutDat = map(CheckOutDate, range(0,len(df)))

CoutHr = map(CheckOutHour, range(0, len(df)))



jk = {'CheckInDate': pk.Series(CinDat), 'CheckinTime': pk.Series(CinHr), 'CheckOutDate': pk.Series(CoutDat), 'CheckOutTime': pk.Series(CoutHr)}
L = pk.DataFrame(jk)

print L


'''






# writer = pk.ExcelWriter('/home/pavan/PAVANKUMAR/MachineLearning/CaseStudy/ML_DATA/v4/k5/FinalFiles/Data_Sorted_nan_dupl.xlsx', engine='xlsxwriter' )
# L.to_excel(writer, 'SortedFile')
# writer.save()

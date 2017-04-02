import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import time
from dateutil import parser

q = []

weeklyList = []
checkList = []
newDays = []
tDay = []
hrs = []

c1 = []
c2 = []

h = np.timedelta64(1, 'h')

# datasheet = pd.read_excel("/home/tcs/Desktop/pavan_guest/MLCP_Test2/local_Data/mlcpdb_Data2.xlsx", sheetname=0)
df_new = pd.read_excel("/home/pavan/PAVANKUMAR/MachineLearning/CaseStudy/ML_DATA/v4/k1/MLCP_Sorted.xlsx", sheetname=0)
# df_sorted =  df_new.sort('CheckinTime',  ascending=True)


'''
for i in range(0, len(df_sorted)):
	q.append(dt.datetime.strptime(df_sorted.CheckinTime[i], '%Y-%m-%d %H:%M:%S').date())
	
'''


def finDay_now(u, i):
    while(i < 20):

        checkList = df_new.EnterDate[df_new.EnterDate == u].index.tolist()
        if len(checkList):
            newDays.append((checkList[0]))
            tDay.append(u)

        u = u + dt.timedelta(days=1)

        i += 1


def drange(start, stop, step):
    while start < stop:
        yield start
        start += step


def fin_weekDay(w):
    weekDay = parser.parse(w.strftime('%Y-%m-%d')).strftime("%A")
    return weekDay


z = df_new.EnterDate[0]
z_ahead = z + dt.timedelta(days=1)
newDays.append(0)
tDay.append(z)

finDay_now(z_ahead, 0)

print(newDays)
print(tDay)



for d in range(0, len(newDays) - 1):
    r1 = newDays[d]
    r2 = newDays[d + 1]

    c1 = (df_new.CheckinTime[r1:r2] - tDay[d]) / h
    c2 = (df_new.CheckoutTime[r1:r2] - tDay[d]) / h

    for t in range(0, 24, 1):

        q = 0
        for j in drange(r1, r2, 1):

            try:

                if (t >= c1[j]) & (t < c2[j]):
                    q += 1
            except:

                print('Some error occured')

        if q > 0:
            hrs.append(q)

        elif q == 0:
            hrs.append(0)

print hrs[:]
























































'''
df13 = pd.DataFrame({'EnterDate' : df_sorted['EnterDate'],'CheckinTime':df_sorted['CheckinTime'], 'CheckoutTime': df_sorted['CheckoutTime']})
writer = pd.ExcelWriter('/home/tcs/Desktop/pavan_guest/MLCP_Test2/local_Data/MLCP_Sorted.xlsx', engine='xlsxwriter' )
df13.to_excel(writer, 'mlcp2_sortedFile')
writer.save()
'''

'''
def myFun():

	z = df_new.EnterDate[0]
	print(z)
	z_ahead = z + dt.timedelta(days=1)
	print(z_ahead)
	checkList = df_new.EnterDate[df_new.EnterDate == z_ahead].index.tolist()
	newDays.append((checkList) )
	tDay.append(z)

newDays.append(0)
myFun()

print(newDays)
print(tDay)
'''

import pandas as pd
import numpy as np
import datetime as dt
import time
import matplotlib.pyplot as plt
from itertools import cycle
from dateutil import parser
from operator import add

# from datetime import datetime

# startTime = datetime.now()
weeklyList = []
checkList = []
newDays = []
tDay = []
hrs = []

c1 = []
c2 = []

q = 0
q_next = 0
dayList = []
day_after_List = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]



# lst = ['Thu','Fri','Sat','Sun','Mon','Tue', 'Wed']
#

h = np.timedelta64(1, 'h')

sheet1 = pd.read_excel("/home/pavan/PAVANKUMAR/MachineLearning/CaseStudy/ML_DATA/v4/k1/neway.xlsx", sheetname=0)


# print (sheet1.CheckinTime)


def finDay_now(u, i):
    # print (u)
    while (i < 14):
        checkList = sheet1.EnterDate[sheet1.EnterDate == u].index.tolist()
        tDay.append(u)
        # newDays.append(checkList[0]+2)
        # print ((checkList[0]+2))
        newDays.append((checkList[0]) - 1)
        u = u + dt.timedelta(days=1)

        i += 1


def drange(start, stop, step):
    while start < stop:
        yield start
        start += step


# print (sheet1.CheckinTime[1560])
# print (sheet1.CheckinTime[1561])
z = sheet1.EnterDate[0]
z1 = z.strftime('%Y-%m-%d')
jj = parser.parse(z1).strftime("%A")
print(jj)
z_ahead = z + dt.timedelta(days=1)
# print z_ahead
newDays.append(0)
tDay.append(z)

finDay_now(z_ahead, 0)
# print (newDays[:])
# print (tDay[:])
'''
r1 = newDays[4]
r2 = newDays[4 + 1] +1
k1 = sheet1.CheckinTime[r1:r2]
print (k1)
'''


# print (len(newDays))

# i for i in list1 if i > 2 and i < 9
def fin_weekDay(w):
    weekDay = parser.parse(w.strftime('%Y-%m-%d')).strftime("%A")
    return weekDay
    # pool = cycle(weekDay)


for d in range(0, len(newDays) - 1):
    r1 = newDays[d]
    r2 = newDays[d + 1]

    # print (r1, r2)

    # k1 = (sheet1.CheckinTime[r1:r2] - tDay[d])
    # k2 = (sheet1.CheckoutTime[r1:r2] - tDay[d])

    c1 = (sheet1.CheckinTime[r1:r2] - tDay[d]) / h
    c2 = (sheet1.CheckoutTime[r1:r2] - tDay[d]) / h
    # print (r1, r2)
    # print (tDay[d])
    # print (c1[:])
    # print (c2[:])



    for t in range(0, 48, 1):

        q = 0
        q_next = 0

        for j in drange(r1, r2, 1):

            try:
                if t < 24:
                    if (t >= c1[j]) & (t < c2[j]):
                        # print(t,j)
                        # time.sleep(2)
                        q += 1

                elif t >= 24:
                    if (t >= c1[j]) & (t < c2[j]):
                        # print(t,j)
                        # time.sleep(2)
                        q_next += 1
                        q = q_next

            except:
                # print(t,j)
                # time.sleep(2)
                print('Something went wrong')

        if q > 0:
            hrs.append(q)

        elif q == 0:
            hrs.append(0)

    #print len(hrs)
    dayList.append(map(add, hrs[0:24], day_after_List))  #hrs[0:24]
    day_after_List = hrs[24:49]
    #print dayList
    #print day_after_List
    del hrs[:]

dayList = reduce(add, dayList)
print dayList
plt.plot(dayList)
plt.show()


    #print(q, q_next)

    # weeklyList.append((fin_weekDay(tDay[d]), hrs[:]))

    # print hrs[:]
    # del hrs[:]

# print (weeklyList)



#print hrs[:]

# plt.xticks(my_xticks)
# plt.plot(hrs[:])
# plt.show()


# print (hrs[:25])

# del c1[:]
# del c2[:]


'''
df13 = pd.DataFrame({'EnterDate' : test['Enter Date'] ,'CheckinTime':test['CheckinTime'], 'CheckoutTime': test['CheckoutTime']})
writer = pd.ExcelWriter('/home/pavan/PAVANKUMAR/MachineLearning/CaseStudy/ML_DATA/v4/mlcp_Filter_1.xlsx', engine='xlsxwriter' )
df13.to_excel(writer, 'pavan')
writer.save()
'''
import pandas as pd
import numpy as np
import datetime as dt
from operator import add
import matplotlib.pyplot as plt

start = dt.datetime.now()

WeekLabels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
z = np.zeros(48)
# sumArray = np.zeros([48, ])
# print z

# df_new = pd.read_excel("/home/tcs/Desktop/pavan_guest/MakeNew/NewOne_2.xlsx", sheetname=0)
df_new = pd.read_excel("/home/tcs/Music/pavan_new/MNist-master/NewOne_2.xlsx", sheetname=0)

dy = pd.read_excel("/home/tcs/Music/pavan_new/MNist-master/DayFile.xlsx", sheetname=0)

dayList = []
one_day_b4_List = np.zeros([24, ])
two_day_b4_List = np.zeros([24, ])

# print df_new.Duration
Q = []

L = []
new_d = df_new['Date'].unique()


# print  len(new_d)



def drange(start, stop, step):
    while start < stop:
        yield start
        start += step


# q = df_new[df_new.Date == new_d[1]].index.tolist()
# print q


for i in range(0, len(new_d)):
    z = np.zeros(100)
    q = df_new[df_new.Date == new_d[i]].index.tolist()

    for j in range(q[0], q[-1] + 1):
        x_, y_ = df_new.CheckinTime[j], df_new.Duration[j]
        z[x_:x_ + y_] = map(lambda x: z[x] + 1, range(x_, x_ + y_))
    L.append(z)

    dayList.append(map(add, map(add, L[i][0:24], one_day_b4_List), two_day_b4_List))
    one_day_b4_List = L[i][24:48]
    two_day_b4_List = L[i][48:72]
    # print (dayList)
    # print (one_day_b4_List)
    # print (two_day_b4_List)
    # break

myList = dayList
dayList = reduce(add, dayList)

kk = dy.groupby("WeekDay")

# L = kk.get_group('Friday')
# print L.index
# print myList[0]
# print myList[4]
# print
# qw = np.column_stack((myList[0], myList[3]))

# qq = map(lambda c : myList[c], [0,3])
fg = 0
fig = plt.figure()
for label in WeekLabels:
    L = kk.get_group(label)
    qq = np.column_stack(map(lambda c: myList[c], L.index))
    fg += 1

    zz = np.mean(qq, axis=1)

    ax1 = fig.add_subplot(3, 3, fg)
    ax1.set_axis_bgcolor("lightslategray")
    ax1.xaxis.label.set_color('g')
    ax1.yaxis.label.set_color('g')
    plt.plot(zz, color='w')
    plt.xlabel(label)
    plt.ylabel('Mean of Cars')

plt.show()

print dt.datetime.now() - start

plt.plot(dayList, color='r')
plt.xlabel('Hours')
plt.ylabel('Number of Cars')
x = list(drange(24, 3123, 24))
plt.xticks(x, dy.WeekDay.values, rotation='vertical')
plt.show()




'''
L = kk.get_group(label)
	qq = np.column_stack(map(lambda c : myList[c], L.index))

	print qq
	zz = np.mean(qq, axis=1)
	print zz

	plt.plot(zz, color = 'r')
	plt.xlabel(label)
	plt.ylabel('Mean of Cars')
	
	plt.show()
'''

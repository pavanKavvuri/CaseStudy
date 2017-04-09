import pandas as pk
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt

startTime = dt.datetime.now()

WeekLabels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


# df = pk.read_excel("/home/tcs/Desktop/pavan_guest/neway.xlsx", sheetname=0)   #dat.dropna(how='any')
df = pk.read_excel('/home/pavan/PAVANKUMAR/MachineLearning/CaseStudy/ML_DATA/v4/k5/FinalFiles/Data_Sorted_nan.xlsx',
                   sheetname=0)
# print df
CinBsyList = []
CoutBsyList = []
n = []

Cin_Uniq = df['CheckInDate'].unique()
#print Cin_Uniq

Cout_Uniq = df['CheckOutDate'].unique()


# ds = df[df.CheckOutDate == Cout_Uniq[0]]
# q = ds[ds.CheckOutTime == 17]
# print len(q)


def F(h):

    ds = df[df.CheckInDate == h]
    Z = (map(lambda y: CinBsyList.append(len(ds[ds.CheckinTime == y])), range(0, 25)))



def G(k):

    ds = df[df.CheckOutDate == k]
    Z = (map(lambda y: CoutBsyList.append(len(ds[ds.CheckOutTime == y])), range(0, 25)))


map(F, Cin_Uniq)
map(G, Cout_Uniq)

#print n

#print 'CinBsyList'
#print CinBsyList
print
#print 'CoutBsyList'
#print CoutBsyList

Cinchunk = [CinBsyList[x:x+24] for x in range(0, len(CinBsyList), 24)]
#print Cinchunk

Coutchunk = [CoutBsyList[x:x+24] for x in range(0, len(CoutBsyList), 24)]
#print Coutchunk

dy = pk.read_excel("/home/pavan/PAVANKUMAR/MachineLearning/CaseStudy/ML_DATA/v4/k5/FinalFiles/DayFile.xlsx", sheetname=0)

dy2 = pk.read_excel("/home/pavan/PAVANKUMAR/MachineLearning/CaseStudy/ML_DATA/v4/k5/FinalFiles/DayFile_Cout.xlsx", sheetname=0)


kk = dy.groupby("WeekDay")
pp = dy2.groupby('CoutWeekDay')


fg = 0
fig1 = plt.figure()
#fig2 = plt.figure()

for label in WeekLabels:

    L = kk.get_group(label)
    M = pp.get_group(label)
    qq = np.column_stack(map(lambda c: Cinchunk[c], L.index))
    nn = np.column_stack(map(lambda d: Coutchunk[d], M.index))
    fg += 1
    #print qq


    zz = np.mean(qq, axis=1)
    tt = np.mean(nn, axis=1)
    #print tt

    ax1 = fig1.add_subplot(3, 3, fg)
    ax1.set_axis_bgcolor("lightslategray")
    ax1.xaxis.label.set_color('g')
    ax1.yaxis.label.set_color('g')
    plt.plot(zz, color='w')
    plt.xlabel(label)
    plt.ylabel('Mean of Cars')

'''
    ax2 = fig2.add_subplot(3, 3, fg)
    ax2.set_axis_bgcolor("lightslategray")
    ax2.xaxis.label.set_color('g')
    ax2.yaxis.label.set_color('g')
    plt.plot(tt, color='w')
    plt.xlabel(label)
    plt.ylabel('Mean of Cars')
    plt.show()
'''


plt.show()




# map(lambda y: n.append(len(ds[ds.CheckOutTime == y])), range(0,25))


# t = list(map(lambda x: list(map(lambda y: n.append(x + y), Y)),X))


'''

def myFun(j):
    x_ = df.CheckinTime[j]
    z[x_] = z[x_] + 1
    return z


def YFun(k):
    x_ = df.CheckOutTime[k]
    z[x_] = z[x_] + 1
    return z


for rin in range(0, len(Cin_Uniq)):
    z = np.zeros(24)
    qin = df[df.CheckInDate == Cin_Uniq[rin]].index.tolist()
    # print q

    WER = map(myFun, qin)
    CinBsyList.append(WER[0])
    del WER[:]
    # break

print 'Busiest CheckinList is :'
print CinBsyList

for rout in range(0, len(Cout_Uniq)):
    z = np.zeros(24)
    qout = df[df.CheckOutDate == Cout_Uniq[rout]].index.tolist()
    # print qout

    WER = map(YFun, qout)
    CoutBsyList.append(WER[0])
    del WER[:]

print 'Busiest CheckouList is :'
print CoutBsyList

EndTime = dt.datetime.now() - startTime
print EndTime

'''
#/home/pavan/PycharmProjects/CaseStudy/check_2.py
import pandas as pk
import numpy as np
import datetime as dt

startTime = dt.datetime.now()

# df = pk.read_excel("/home/tcs/Desktop/pavan_guest/neway.xlsx", sheetname=0)   #dat.dropna(how='any')
df = pk.read_excel('/home/pavan/PAVANKUMAR/MachineLearning/CaseStudy/ML_DATA/v4/k5/FinalFiles/Data_Sorted_nan.xlsx',
                   sheetname=0)
# print df
CinBsyList = []
CoutBsyList = []

# z = np.zeros(24)

# qr = df.sort_values('CheckOutDate')

Cin_Uniq = df['CheckInDate'].unique()

Cout_Uniq = df['CheckOutDate'].unique()

'''
Cout_Uniq = qr['CheckOutDate'].unique()

q = qr[qr.CheckOutDate == Cin_Uniq[1]].index.tolist()
print q
print Cout_Uniq[1]
'''
# ds = df[df.CheckOutDate == Cout_Uniq[0]]
# q = ds[ds.CheckOutTime == 17].index.tolist()
# print len(q)
L = []


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
    #print q

    WER = map(myFun, qin)
    CinBsyList.append(WER[0])
    del WER[:]
    #break

print 'Busiest CheckinList is :'
print CinBsyList


for rout in range(0, len(Cout_Uniq)):
    z = np.zeros(24)
    qout = df[df.CheckOutDate == Cout_Uniq[rout]].index.tolist()
    #print qout

    WER = map(YFun, qout)
    CoutBsyList.append(WER[0])
    del WER[:]


print 'Busiest CheckouList is :'
print CoutBsyList

EndTime = dt.datetime.now()-startTime
print EndTime


'''

for r in range(len(Cin_Uniq)):

    z = np.zeros(24)
    q = df[df.CheckInDate == Cin_Uniq[r]].index.tolist()

    for j in range(q[0], q[-1]+1):

        x_ = df.CheckinTime[j]
        z[x_] = z[x_] +1
        
        
    L.append(z)
    
print len(L)


for s in range(len(Cout_Uniq)):

    f = np.zeros(24)
    q = df[df.CheckOutDate == Cin_Uniq[s]].index.tolist()

    for j in range(q[0], q[-1]+1):

        x_ = df.CheckoutTime[j]
        f[x_] = f[x_] +1
        
        
    L.append(z)
    
'''
# map(lambda y: z[df.CheckinTime[]] + 1 ,  range(q[0], q[-1]+1))

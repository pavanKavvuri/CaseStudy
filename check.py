import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import time
from dateutil import parser
import types


q = 0

#df_new = pd.read_excel("/home/pavan/PAVANKUMAR/MachineLearning/CaseStudy/ML_DATA/v4/k1/MLCP_Sorted.xlsx", sheetname=0)

df_new11 = pd.read_excel("/home/pavan/PAVANKUMAR/MachineLearning/CaseStudy/ML_DATA/v4/k1/mlcp_test_1.xlsx", sheetname=0)

#print (df_new.CheckoutTime[:])
q =  str(df_new11.book_timeout[0:1])

print df_new11.book_timeout[0:1]
print q[5]


print (type(q[5]))


'''
z = df_new.EnterDate[0]
z_ahead = z + dt.timedelta(days=2)


checkList = df_new.EnterDate[df_new.EnterDate == z_ahead].index.tolist()
print (checkList[0])

#print (df_new.EnterDate[2313],df_new.EnterDate[2314], df_new.EnterDate[3109], df_new.EnterDate[3110])






for x in range(len(df_new)):

    if pd.isnull(df_new.CheckoutTime[x]) :
        q+= 1

print q
'''
import pandas as pk

df = pk.read_excel(
    '/home/pavan/PAVANKUMAR/MachineLearning/CaseStudy/ML_DATA/v4/k5/FinalFiles/Data_Sorted_nan_dupl.xlsx', sheetname=0)


WeekLabels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


CinList = df.CheckInDate.unique()

CoutList = df.CheckOutDate.unique()


print (len(CinList), len(CoutList))

D = []
Q = []

df_ex = pk.DataFrame({"CoutList": CoutList})

D.append(df_ex['CoutList'].dt.weekday)
print len(D[0])

df_ex1 = pk.DataFrame({"CoutList": CoutList, 'DAYNO': D[0]})


def S(g):
    Q.append(WeekLabels[g])

map(S, D[0])



df_ex2 = pk.DataFrame({"CoutList": CoutList, 'CoutWeekDay': Q})

print df_ex2


writer = pk.ExcelWriter('/home/pavan/PAVANKUMAR/MachineLearning/CaseStudy/ML_DATA/v4/k5/FinalFiles/DayFile_Cout.xlsx', engine='xlsxwriter' )
df_ex2.to_excel(writer, 'DayFile_2')
writer.save()

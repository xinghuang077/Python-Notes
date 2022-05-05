import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

readExcel = pd.read_excel('ETROC2_clockTree_M6_1umINVD2_M4.xlsx')
#print(readExcel.columns)
# print(readExcel[['Tap']])
# print(readExcel[['Tap', 'c0_27_1v2_tt']])

#x = readExcel['Tap']
# print(x)

#c0 = readExcel['c0_27_1v2_tt']
# print(type(c0))
# print(len(c0))


#Col_B_Data = []
#SUM = 0
#for index in range(len(c0)):
    # Col_B_Data += [c0.iloc[index]] 
#    SUM += c0.iloc[index]
#    print(SUM)
#    Col_B_Data += [SUM]
#    
#print(Col_B_Data)

fig,ax = plt.subplots()

CornerNum1 = readExcel['Conner NO.']
Delay1 = readExcel['Delay']
Skew1 = readExcel['Skew']
DutyCycle1 = readExcel['DutyCycle']
RiseFall1 = readExcel['RiseTime']
Power1 = readExcel['Power']


CornerNum2 = readExcel['Conner NO._M5']
Delay2 = readExcel['Delay_M5']
Skew2 = readExcel['Skew_M5']
DutyCycle2 = readExcel['DutyCycle_M5']
RiseFall2 = readExcel['RiseTime_M5']
Power2 = readExcel['Power_M5']

plt.plot(CornerNum1, DutyCycle1, 'o', color='red')
plt.plot(CornerNum2, DutyCycle2, '^', color='blue')
plt.xticks(np.arange(0,30,1))
plt.xlabel("Corner of Simulation")
plt.ylabel("DutyCycle [%]")
plt.title("DutyCycle Study of 16 x 16 Clock Tree")
values = ['ss-45_1V08',	'ss-45_1V2', 'ss-45_1V32','ss-20_1V08', 'ss-20_1V2', 'ss-20_1V32', 'ss55_1V08', 'ss55_1V2',	'ss55_1V32', 'tt-45_1V08', 'tt-45_1V2', 'tt-45_1V32', 'tt-20_1V08', 'tt-20_1V2', 'tt-20_1V32', 'tt27_1V08', 'tt27_1V2', 'tt27_1V32', 'tt55_1V08', 'tt55_1V2', 'tt55_1V32', 'ff-45_1V08', 'ff-45_1V2', 'ff-45_1V32', 'ff-20_1V08', 'ff-20_1V2', 'ff-20_1V32', 'ff55_1V08', 'ff55_1V2', 'ff55_1V32'] 
plt.xticks(CornerNum1,values)
plt.xticks(rotation=70)

plt.ylim(49.8, 51)

#fig.autofmt_xdate(rotation=45)
#plt.grid(axis='x',linestyle='-.')
#plt.grid(axis='y',linestyle='dashed')
plt.grid('on',linestyle = 'dashed')
#plt.legend()
plt.legend(['Trace M6, 1 um width, shielded by M4', 'Trace M5, 1 um width, shielded by M3 and M7'], loc='best', fancybox=True, shadow=True, frameon = 'on', edgecolor='black')

plt.savefig('./DutyCycleSim.png')

plt.show()
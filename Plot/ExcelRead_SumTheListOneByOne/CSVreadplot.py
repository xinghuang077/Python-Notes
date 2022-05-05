import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

readExcel = pd.read_excel('PS_ALTIROC_CORNERS.xlsx')
print(readExcel.columns)
# print(readExcel[['Tap']])
# print(readExcel[['Tap', 'c0_27_1v2_tt']])

x = readExcel['Tap']
# print(x)

c0 = readExcel['c0_27_1v2_tt']
# print(type(c0))
# print(len(c0))

c1 = readExcel['c1_n30_1v32_ff']


c0_time = []
SUM0 = 0
for index in range(len(c0)):
    # c0_time += [c0.iloc[index]] 
    SUM0 += c0.iloc[index]
    # print(SUM0)
    c0_time += [SUM0]
print(c0_time)

# c1_time = []
# SUM1 = 0
# for index in range(len(c1)):
#     # c0_time += [c0.iloc[index]] 
#     SUM1 += c1.iloc[index]
#     # print(SUM1)
#     c1_time += [SUM1]
# print(c1_time)

plt.plot(x, c0_time, '-o', color='red')
# plt.plot(x, c1_time, '*')
plt.show()
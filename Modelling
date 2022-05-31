import math

import pandas as pd
import matplotlib.pyplot as plt


url1 = "https://raw.githubusercontent.com/EQWorks/ws-data-pandas/main/data/DataSample.csv"
DataSample = pd.read_csv(url1)

POI1x = 53.546167
POI2x = 53.526167
POI3x = 45.521629
POI4x = 45.224830

POI1y = -113.485734
POI2y = -113.489734
POI3y = -73.566024
POI4y = -63.232729

dstList = []

POI1Total = 0
POI2Total = 0
POI3Total = 0
POI4Total = 0

num1 = 0
num2 = 0
num3 = 0
num4 = 0

dst1Lst = []
dst2Lst = []
dst3Lst = []
dst4Lst = []


for i in range(len(DataSample)):

    x = DataSample.loc[i]["Latitude"]
    y = DataSample.loc[i]["Longitude"]

    dst1 = math.sqrt((x-POI1x)**2 + (y-POI1y)**2)
    dst2 = math.sqrt((x - POI2x) ** 2 + (y - POI2y) ** 2)
    dst3 = math.sqrt((x - POI3x) ** 2 + (y - POI3y) ** 2)
    dst4 = math.sqrt((x - POI4x) ** 2 + (y - POI4y) ** 2)





    if dst1 <= dst2 and dst1 <= dst3 and dst1 <= dst4:
        POI1Total += dst1
        num1 = num1 + 1
        dst1Lst.append(dst1)
    elif dst2 <= dst1 and dst2 <= dst3 and dst2 <= dst4:
        POI2Total += dst2
        num2 = num2 + 1
        dst2Lst.append(dst2)
    elif dst3 <= dst1 and dst3 <= dst2 and dst3 <= dst4:
        POI3Total += dst3
        num3 = num3 + 1
        dst3Lst.append(dst3)
    else:
        POI4Total += dst4
        num4 = num4 + 1
        dst4Lst.append(dst4)

max = 0
min = 0

AllNums = [num1,num2,num3,num4]
AllNums.sort()

NumsScale = AllNums[3] - AllNums [0]

scale1 = ((num1*20)/NumsScale) - 10
scale2 = ((num2*20)/NumsScale) - 10
scale3 = ((num3*20)/NumsScale) - 10
scale4 = ((num4*20)/NumsScale) - 10

plt.grid()
plt.plot(1, scale1, marker="o", markersize=20, color="red")
plt.plot(2, scale2, marker="o", markersize=20, color="green")
plt.plot(3, scale3, marker="o", markersize=20, color="blue")
plt.plot(4, scale4, marker="o", markersize=20, color="purple")
plt.show()

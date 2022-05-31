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

print("For POI1:")
print("average:")
avg1 = POI1Total/num1
print(avg1)
print("Standard Deviation:")
std1 = 0
for k in dst1Lst:
    std1 += (k-avg1)**2
print(math.sqrt(std1/num1))


print("For POI2:")
print("average:")
avg2 = POI2Total/num2
print(avg2)
print("Standard Deviation:")
std2 = 0
for k in dst2Lst:
    std2 += (k-avg2)**2
print(math.sqrt(std2/num2))


print("For POI3:")
print("average:")
avg3 = POI3Total/num3
print(avg3)
print("Standard Deviation:")
std3 = 0
for k in dst3Lst:
    std3 += (k-avg3)**2
print(math.sqrt(std3/num3))



print("For POI4:")
print("average:")
avg4 = POI4Total/num4
print(avg4)
print("Standard Deviation:")
std4 = 0
for k in dst4Lst:
    std4 += (k-avg4)**2
print(math.sqrt(std4/num4))

fig, ax = plt.subplots()
circle1 = plt.Circle((POI1x, POI1y), avg1, color='pink')
circle2 = plt.Circle((POI2x, POI2y), avg2, color='blue')
circle3 = plt.Circle((POI3x, POI3y), avg3, color='green')
circle4 = plt.Circle((POI4x, POI4y), avg4, color='purple')

plt.scatter(POI1x, POI1y, color="pink")
plt.scatter(POI2x, POI2y, color="blue")
plt.scatter(POI3x, POI3y, color="green")
plt.scatter(POI4x, POI4y, color="purple")

ax.add_artist(circle1)
ax.add_artist(circle2)
ax.add_artist(circle3)
ax.add_artist(circle4)



plt.show()

print("For POI1:")
print("Radius: " + str(avg1))
print("Density: " + str(num1/(math.pi*avg1**2)))

print("For POI2:")
print("Radius: " + str(avg2))
print("Density: " + str(num2/(math.pi*avg2**2)))

print("For POI3:")
print("Radius: " + str(avg3))
print("Density: " + str(num3/(math.pi*avg3**2)))

print("For POI4:")
print("Radius: " + str(avg4))
print("Density: " + str(num4/(math.pi*avg4**2)))




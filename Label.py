import math

import pandas as pd
from scipy.spatial import distance


url1 = "https://raw.githubusercontent.com/EQWorks/ws-data-pandas/main/data/DataSample.csv"
DataSample = pd.read_csv(url1)

POI1 = math.sqrt(53.546167**2+(-113.485734)**2)
POI2 = math.sqrt(53.546167 ** 2 + (-113.485634) ** 2)
POI3 = math.sqrt(45.521629 ** 2 + (-73.566024) ** 2)
POI4 = math.sqrt(45.224830 ** 2 + (-63.232729) ** 2)
dstList = []

for i in range(len(DataSample)):

    x = math.sqrt(DataSample.loc[i]["Latitude"] ** 2 + DataSample.loc[i]["Longitude"] ** 2)
    dst1 = distance.euclidean(POI1, x)
    dst2 = distance.euclidean(POI2, x)
    dst3 = distance.euclidean(POI3, x)
    dst4 = distance.euclidean(POI3, x)

    if dst1 < dst2 and dst1 < dst3 and dst1 < dst4:
        dstList.append(dst1)
    elif dst2 < dst1 and dst2 < dst3 and dst2 < dst4:
        dstList.append(dst2)
    elif dst3 < dst1 and dst3 < dst2 and dst3 < dst4:
        dstList.append(dst3)
    else:
        dstList.append(dst4)


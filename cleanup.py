import pandas as pd


url1 = "https://raw.githubusercontent.com/EQWorks/ws-data-pandas/main/data/DataSample.csv"
DataSample = pd.read_csv(url1)


for i in range(len(DataSample)):
    for j in range(len(DataSample)):
        if DataSample.loc[i][" TimeSt"] == DataSample.loc[j][" TimeSt"] and  DataSample.loc[i]["Country"] == DataSample.loc[j]["Country"] and  DataSample.loc[i]["Province"] == DataSample.loc[j]["Province"] and  DataSample.loc[i]["City"] == DataSample.loc[j]["City"]:
            print(DataSample.loc[i])

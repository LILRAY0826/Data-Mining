import pandas as pd

# Load Data
dataframe = pd.read_csv("heart.csv")

# Data Preprocessing
# Age 5 Labels 28~37 = 0, 38~47 = 1, 48~57 = 2, 58~67 = 3,68~77 = 4
for i in range (0, 5):
    dataframe["Age"] = dataframe["Age"].replace([28 + i*10], i)
    dataframe["Age"] = dataframe["Age"].replace([29 + i*10], i)
    dataframe["Age"] = dataframe["Age"].replace([30 + i*10], i)
    dataframe["Age"] = dataframe["Age"].replace([31 + i*10], i)
    dataframe["Age"] = dataframe["Age"].replace([32 + i*10], i)
    dataframe["Age"] = dataframe["Age"].replace([33 + i*10], i)
    dataframe["Age"] = dataframe["Age"].replace([34 + i*10], i)
    dataframe["Age"] = dataframe["Age"].replace([35 + i*10], i)
    dataframe["Age"] = dataframe["Age"].replace([36 + i*10], i)
    dataframe["Age"] = dataframe["Age"].replace([37 + i*10], i)

# Sex 2 Labels
dataframe.loc[dataframe.Sex=="F", "Sex"] = 0
dataframe.loc[dataframe.Sex=="M", "Sex"] = 1

# ChestPainType 4 Labels
dataframe.loc[dataframe.ChestPainType=="ATA", "ChestPainType"] = 0
dataframe.loc[dataframe.ChestPainType=="NAP", "ChestPainType"] = 1
dataframe.loc[dataframe.ChestPainType=="ASY", "ChestPainType"] = 2
dataframe.loc[dataframe.ChestPainType=="TA", "ChestPainType"] = 3

# RestingBP 4 Labels 0~49 = 0, 50~99 = 1, 100~149 = 2, 150~200 = 3
for i in range (0, 4):
    for j in range (0, 50):
        dataframe["RestingBP"] = dataframe["RestingBP"].replace([j + i*50], i)
dataframe["RestingBP"] = dataframe["RestingBP"].replace([200], 3)


# Cholesterol 7 Labels
for i in range (0, 7):
    for j in range (0, 100):
        dataframe["Cholesterol"] = dataframe["Cholesterol"].replace([j + i*100], i)

# RestingECG 3 Labels
dataframe.loc[dataframe.RestingECG=="Normal", "RestingECG"] = 0
dataframe.loc[dataframe.RestingECG=="ST", "RestingECG"] = 1
dataframe.loc[dataframe.RestingECG=="LVH", "RestingECG"] = 2

# MaxHR 3 Labels
for i in range (0, 6):
    for j in range (0, 25):
        dataframe["MaxHR"] = dataframe["MaxHR"].replace([60+j + i*25], i)

# ExerciseAngina 2 Labels
dataframe.loc[dataframe.ExerciseAngina=="N", "ExerciseAngina"] = 0
dataframe.loc[dataframe.ExerciseAngina=="Y", "ExerciseAngina"] = 1

# Oldpeak -3~7 = 10~19 10 Labels
for i in range (-2, 8):
    dataframe.loc[dataframe.Oldpeak < i, "Oldpeak"] = 10 + i+2
for i in range (0, 10):
    dataframe.loc[dataframe.Oldpeak==10+i, "Oldpeak"] = 0+i

# ST_Slope 3 Labels
dataframe.loc[dataframe.ST_Slope=="Up", "ST_Slope"] = 0
dataframe.loc[dataframe.ST_Slope=="Flat", "ST_Slope"] = 1
dataframe.loc[dataframe.ST_Slope=="Down", "ST_Slope"] = 2
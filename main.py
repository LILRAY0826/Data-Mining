import Function
import pandas as pd

dataframe = pd.read_csv("heart.csv")

GainRatio = {"Age" : Function.GainRatio("Age"),
             "Sex" : Function.GainRatio("Sex"),
             "ChestPainType" : Function.GainRatio("ChestPainType"),
             "RestingBP" : Function.GainRatio("RestingBP"),
             "Cholesterol" : Function.GainRatio("Cholesterol"),
             "FastingBS" : Function.GainRatio("FastingBS"),
             "RestingECG" : Function.GainRatio("RestingECG"),
             "MaxHR" : Function.GainRatio("MaxHR"),
             "ExerciseAngina" : Function.GainRatio("ExerciseAngina"),
             "Oldpeak" : Function.GainRatio("Oldpeak"),
             "ST_Slope" : Function.GainRatio("ST_Slope")}

new_dataframe = dataframe.loc[dataframe["ST_Slope"] == "Up"]
print(new_dataframe.drop(columns=["ST_Slope"]))
#print(GainRatio.keys())
#print(max(GainRatio.values()))

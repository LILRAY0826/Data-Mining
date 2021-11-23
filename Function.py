import pandas as pd
import numpy as np

# Information Gain = I(a, b)
def Information_Gain(a, b):
    if a == 0 and b!= 0:
        return -(b/(a+b) * np.log2(b/(a+b)))
    elif b == 0 and a!= 0:
        return -(a/(a+b) * np.log2(a/(a+b)))
    elif a == 0 and b == 0:
        return 0
    else:
        return -(a / (a + b) * np.log2(a / (a + b)) + b / (a + b) * np.log2(b / (a + b)))

# Gain(Attribute)
def Gain(attribute):
    return Info_all() - Info(attribute)

# Info(D)
def Info_all():
    no_disease = 0
    yes_disease = 0
    dataframe = pd.read_csv("heart.csv")
    for i in range (0, dataframe.shape[0]):
        if dataframe["HeartDisease"][i] == 0:
            no_disease += 1
        if dataframe["HeartDisease"][i] == 1:
            yes_disease += 1
    return Information_Gain(no_disease, yes_disease)

# Info(Attribute)
def Info(attribute):
    dataframe = pd.read_csv("heart.csv")

    if attribute == "Age":
        result = 0
        for j in range(0, 5):
            no_disease = 0
            yes_disease = 0
            counter = 0
            for i in range(0, dataframe.shape[0]):
                if 28 + (j * 10) <= dataframe["Age"][i] < 38 + (j * 10):
                    counter += 1
                    if dataframe["HeartDisease"][i] == 0:
                        no_disease += 1
                    if dataframe["HeartDisease"][i] == 1:
                        yes_disease += 1
            result += counter / dataframe.shape[0] * Information_Gain(no_disease, yes_disease)

    elif attribute == "Sex":
        result = 0
        no_disease = 0
        yes_disease = 0
        counter = 0
        for i in range(0, dataframe.shape[0]):
            if dataframe["Sex"][i] == "F":
                counter += 1
                if dataframe["HeartDisease"][i] == 0:
                    no_disease += 1
                if dataframe["HeartDisease"][i] == 1:
                    yes_disease += 1
        result += counter / dataframe.shape[0] * Information_Gain(no_disease, yes_disease)

        for i in range(0, dataframe.shape[0]):
            if dataframe["Sex"][i] == "M":
                counter += 1
                if dataframe["HeartDisease"][i] == 0:
                    no_disease += 1
                if dataframe["HeartDisease"][i] == 1:
                    yes_disease += 1
        result += counter / dataframe.shape[0] * Information_Gain(no_disease, yes_disease)

    elif attribute == "ChestPainType":
        type = ["ATA", "NAP", "ASY", "TA"]
        result = 0
        for j in range(0, 4):
            no_disease = 0
            yes_disease = 0
            counter = 0
            for i in range(0, dataframe.shape[0]):
                if dataframe["ChestPainType"][i] == type[j]:
                    counter += 1
                    if dataframe["HeartDisease"][i] == 0:
                        no_disease += 1
                    if dataframe["HeartDisease"][i] == 1:
                        yes_disease += 1
            result += counter / dataframe.shape[0] * Information_Gain(no_disease, yes_disease)

    elif attribute == "RestingBP":
        result = 0
        for j in range(0, 3):
            no_disease = 0
            yes_disease = 0
            counter = 0
            for i in range(0, dataframe.shape[0]):
                if 0 + (j * 100) <= dataframe["RestingBP"][i] < 100 + (j * 100):
                    counter += 1
                    if dataframe["HeartDisease"][i] == 0:
                        no_disease += 1
                    if dataframe["HeartDisease"][i] == 1:
                        yes_disease += 1
            result += counter / dataframe.shape[0] * Information_Gain(no_disease, yes_disease)

    elif attribute == "Cholesterol":
        result = 0
        for j in range(0, 7):
            no_disease = 0
            yes_disease = 0
            counter = 0
            for i in range(0, dataframe.shape[0]):
                if 0 + (j * 100) <= dataframe["Cholesterol"][i] < 100 + (j * 100):
                    counter += 1
                    if dataframe["HeartDisease"][i] == 0:
                        no_disease += 1
                    if dataframe["HeartDisease"][i] == 1:
                        yes_disease += 1
            result += counter / dataframe.shape[0] * Information_Gain(no_disease, yes_disease)

    elif attribute == "FastingBS":
        result = 0
        no_disease = 0
        yes_disease = 0
        counter = 0
        for i in range(0, dataframe.shape[0]):
            if dataframe["FastingBS"][i] == 0:
                counter += 1
                if dataframe["HeartDisease"][i] == 0:
                    no_disease += 1
                if dataframe["HeartDisease"][i] == 1:
                    yes_disease += 1
        result += counter / dataframe.shape[0] * Information_Gain(no_disease, yes_disease)

        for i in range(0, dataframe.shape[0]):
            if dataframe["FastingBS"][i] == 1:
                counter += 1
                if dataframe["HeartDisease"][i] == 0:
                    no_disease += 1
                if dataframe["HeartDisease"][i] == 1:
                    yes_disease += 1
        result += counter / dataframe.shape[0] * Information_Gain(no_disease, yes_disease)

    elif attribute == "RestingECG":
        type = ["Normal", "ST", "LVH"]
        result = 0
        for j in range(0, 3):
            no_disease = 0
            yes_disease = 0
            counter = 0
            for i in range(0, dataframe.shape[0]):
                if dataframe["RestingECG"][i] == type[j]:
                    counter += 1
                    if dataframe["HeartDisease"][i] == 0:
                        no_disease += 1
                    if dataframe["HeartDisease"][i] == 1:
                        yes_disease += 1
            result += counter / dataframe.shape[0] * Information_Gain(no_disease, yes_disease)

    elif attribute == "MaxHR":
        result = 0
        for j in range(6, 21):
            no_disease = 0
            yes_disease = 0
            counter = 0
            for i in range(0, dataframe.shape[0]):
                if 0 + (j * 10) <= dataframe["MaxHR"][i] < 10 + (j * 10):
                    counter += 1
                    if dataframe["HeartDisease"][i] == 0:
                        no_disease += 1
                    if dataframe["HeartDisease"][i] == 1:
                        yes_disease += 1
            result += counter / dataframe.shape[0] * Information_Gain(no_disease, yes_disease)

    elif attribute == "ExerciseAngina":
        result = 0
        no_disease = 0
        yes_disease = 0
        counter = 0
        for i in range(0, dataframe.shape[0]):
            if dataframe["ExerciseAngina"][i] == "N":
                counter += 1
                if dataframe["HeartDisease"][i] == 0:
                    no_disease += 1
                if dataframe["HeartDisease"][i] == 1:
                    yes_disease += 1
        result += counter / dataframe.shape[0] * Information_Gain(no_disease, yes_disease)

        for i in range(0, dataframe.shape[0]):
            if dataframe["ExerciseAngina"][i] == "Y":
                counter += 1
                if dataframe["HeartDisease"][i] == 0:
                    no_disease += 1
                if dataframe["HeartDisease"][i] == 1:
                    yes_disease += 1
        result += counter / dataframe.shape[0] * Information_Gain(no_disease, yes_disease)

    elif attribute == "Oldpeak":
        result = 0
        for j in range(-3, 7):
            no_disease = 0
            yes_disease = 0
            counter = 0
            for i in range(0, dataframe.shape[0]):
                if j <= dataframe["Oldpeak"][i] < j + 1:
                    counter += 1
                    if dataframe["HeartDisease"][i] == 0:
                        no_disease += 1
                    if dataframe["HeartDisease"][i] == 1:
                        yes_disease += 1
            result += counter / dataframe.shape[0] * Information_Gain(no_disease, yes_disease)

    elif attribute == "ST_Slope":
        type = ["Up", "Flat", "Down"]
        result = 0
        for j in range(0, 3):
            no_disease = 0
            yes_disease = 0
            counter = 0
            for i in range(0, dataframe.shape[0]):
                if dataframe["ST_Slope"][i] == type[j]:
                    counter += 1
                    if dataframe["HeartDisease"][i] == 0:
                        no_disease += 1
                    if dataframe["HeartDisease"][i] == 1:
                        yes_disease += 1
            result += counter / dataframe.shape[0] * Information_Gain(no_disease, yes_disease)

    return result

# SplitInfo(Attribute)
def SplitInfo(attribute):
    dataframe = pd.read_csv("heart.csv")

    if attribute == "Age":
        result = 0
        for j in range(0, 5):
            counter = 0
            for i in range(0, dataframe.shape[0]):
                if 28 + (j * 10) <= dataframe["Age"][i] < 38 + (j * 10):
                    counter += 1
            if counter == 0:
                result += 0
            else:
                result += -(counter / dataframe.shape[0] * np.log2(counter / dataframe.shape[0]))

    elif attribute == "Sex":
        result = 0
        counter = 0
        for i in range(0, dataframe.shape[0]):
            if dataframe["Sex"][i] == "F":
                counter += 1
        result += -(counter / dataframe.shape[0] * np.log2(counter / dataframe.shape[0]))

        for i in range(0, dataframe.shape[0]):
            if dataframe["Sex"][i] == "M":
                counter += 1
        result += -(counter / dataframe.shape[0] * np.log2(counter / dataframe.shape[0]))

    elif attribute == "ChestPainType":
        type = ["ATA", "NAP", "ASY", "TA"]
        result = 0
        for j in range(0, 4):
            counter = 0
            for i in range(0, dataframe.shape[0]):
                if dataframe["ChestPainType"][i] == type[j]:
                    counter += 1
            result += -(counter / dataframe.shape[0] * np.log2(counter / dataframe.shape[0]))

    elif attribute == "RestingBP":
        result = 0
        for j in range(0, 3):
            counter = 0
            for i in range(0, dataframe.shape[0]):
                if 0 + (j * 100) <= dataframe["RestingBP"][i] < 100 + (j * 100):
                    counter += 1
            result += -(counter / dataframe.shape[0] * np.log2(counter / dataframe.shape[0]))

    elif attribute == "Cholesterol":
        result = 0
        for j in range(0, 7):
            counter = 0
            for i in range(0, dataframe.shape[0]):
                if 0 + (j * 100) <= dataframe["Cholesterol"][i] < 100 + (j * 100):
                    counter += 1
            result += -(counter / dataframe.shape[0] * np.log2(counter / dataframe.shape[0]))

    elif attribute == "FastingBS":
        result = 0
        counter = 0
        for i in range(0, dataframe.shape[0]):
            if dataframe["FastingBS"][i] == 0:
                counter += 1
        result += -(counter / dataframe.shape[0] * np.log2(counter / dataframe.shape[0]))

        for i in range(0, dataframe.shape[0]):
            if dataframe["FastingBS"][i] == 1:
                counter += 1
        result += -(counter / dataframe.shape[0] * np.log2(counter / dataframe.shape[0]))

    elif attribute == "RestingECG":
        type = ["Normal", "ST", "LVH"]
        result = 0
        for j in range(0, 3):
            counter = 0
            for i in range(0, dataframe.shape[0]):
                if dataframe["RestingECG"][i] == type[j]:
                    counter += 1
            result += -(counter / dataframe.shape[0] * np.log2(counter / dataframe.shape[0]))

    elif attribute == "MaxHR":
        result = 0
        for j in range(0, 3):
            counter = 0
            for i in range(0, dataframe.shape[0]):
                if 60 + (j * 50) <= dataframe["MaxHR"][i] < 110 + (j * 50):
                    counter += 1
            result += -(counter / dataframe.shape[0] * np.log2(counter / dataframe.shape[0]))

    elif attribute == "ExerciseAngina":
        result = 0
        counter = 0
        for i in range(0, dataframe.shape[0]):
            if dataframe["ExerciseAngina"][i] == "N":
                counter += 1
        result += -(counter / dataframe.shape[0] * np.log2(counter / dataframe.shape[0]))

        for i in range(0, dataframe.shape[0]):
            if dataframe["ExerciseAngina"][i] == "Y":
                counter += 1
        result += -(counter / dataframe.shape[0] * np.log2(counter / dataframe.shape[0]))

    elif attribute == "Oldpeak":
        result = 0
        for j in range(-3, 7):
            counter = 0
            for i in range(0, dataframe.shape[0]):
                if j <= dataframe["Oldpeak"][i] < j + 1:
                    counter += 1
            result += -(counter / dataframe.shape[0] * np.log2(counter / dataframe.shape[0]))

    elif attribute == "ST_Slope":
        type = ["Up", "Flat", "Down"]
        result = 0
        for j in range(0, 3):
            counter = 0
            for i in range(0, dataframe.shape[0]):
                if dataframe["ST_Slope"][i] == type[j]:
                    counter += 1
            result += -(counter / dataframe.shape[0] * np.log2(counter / dataframe.shape[0]))

    return result

# GainRatio(Attribute)
def GainRatio(attribute):
    return Gain(attribute)/SplitInfo(attribute)
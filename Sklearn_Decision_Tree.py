from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
import pandas as pd
import graphviz

# Load Data
dataframe = pd.read_csv("heart.csv")

# Data Preprocessing
# Sex
dataframe.loc[dataframe.Sex=="F", "Sex"] = 0
dataframe.loc[dataframe.Sex=="M", "Sex"] = 1

# ChestPainStyle
dataframe.loc[dataframe.ChestPainType=="ATA", "ChestPainType"] = 0
dataframe.loc[dataframe.ChestPainType=="NAP", "ChestPainType"] = 1
dataframe.loc[dataframe.ChestPainType=="ASY", "ChestPainType"] = 2
dataframe.loc[dataframe.ChestPainType=="TA", "ChestPainType"] = 3

# RestingECG
dataframe.loc[dataframe.RestingECG=="Normal", "RestingECG"] = 0
dataframe.loc[dataframe.RestingECG=="ST", "RestingECG"] = 1
dataframe.loc[dataframe.RestingECG=="LVH", "RestingECG"] = 2

# ExerciseAngina
dataframe.loc[dataframe.ExerciseAngina=="N", "ExerciseAngina"] = 0
dataframe.loc[dataframe.ExerciseAngina=="Y", "ExerciseAngina"] = 1

# ST_Slope
dataframe.loc[dataframe.ST_Slope=="Up", "ST_Slope"] = 0
dataframe.loc[dataframe.ST_Slope=="Flat", "ST_Slope"] = 1
dataframe.loc[dataframe.ST_Slope=="Down", "ST_Slope"] = 2

# Split Data
total_score = 0
for i in range (0, 10):
    # 10-Fold Cross-Validation
    train_data, test_data = train_test_split(dataframe, train_size=0.9, random_state=i)
    train_data_target = train_data["HeartDisease"]
    train_data_attribute = train_data.drop(columns=["HeartDisease"])
    test_data_target = test_data["HeartDisease"]
    test_data_attribute = test_data.drop(columns=["HeartDisease"])

    # Train Model
    classifier = DecisionTreeClassifier(max_depth=10, random_state=0)
    classifier.fit(train_data_attribute, train_data_target)

    # Predict Model
    test_target_predict_result = classifier.predict(test_data_attribute)
    total_score += accuracy_score(test_data_target, test_target_predict_result)
    dot_data = tree.export_graphviz(classifier, out_file=None,
                                    feature_names=["Age", "Sex", "ChestPainType", "RestingBP", "Cholesterol", "FastingBS", "RestingECG", "MaxHR", "ExerciseAngina", "Oldpeak", "ST_Slope"],
                                    class_names=["0", "1"],
                                    filled=True, rounded=True, leaves_parallel=True)
    graph = graphviz.Source(dot_data)
    graph.view(filename="mypicture", directory="Tree Graph")

score = total_score/10
print('{:.2f}%'.format(score * 100))


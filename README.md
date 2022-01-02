# Data Mining Project - Disease Predicting

## Content
1. **Age :**
    The age of a person, ranging from 28 to 77 years old.
2. **Sex :**
    Is the person Male or Female?
3. **ChestPainType :**
    There are four types in this label : **ATA**, **NAP**, **ASY**, **TA**.
4. **RestingBP :**
    Ranging from 0 to 200.
5. **Cholesterol :**
    Ranging from 0 to 603.
7. **FastingBS :**
    Does the person get FastingBS? (0 or 1) 	
9. **RestingECG :**
    There are three types in this label : **Normal**, **ST**, **LVH**.
11. **MaxHR :**	
    Ranging from 60 to 202.
13. **ExerciseAngina :**
    Does the person get ExerciseAngina? (Yes or No)	
15. **Oldpeak :**	
    Ranging from -2.6 to 6.2.
17. **ST_Slope :**
    There are three types in this label : **Up**, **Flat**, **Down**.	
19. **HeartDisease :**
    Is the person illness? (Yes or No)
## Problem Describe
Use above contents to predict the class label **HeartDisease**, there are two major steps in our process.
* **Data Pre-Processing**
* **Model Construction**
    * Decision Tree
    * Multinominal Naive Bayes
    * Gaussian Naive Bayes
## Data Pre-Processing
We classify all data into Nominal, regardless of **Nominal, **Binary**, **Ordinal**, **Numeric**, and because we want to get better results and avoid overfitting, we do a test on the number of groups of **Numeric** type data to do the grouping.

| Label | Candidate | Best |
| -------- | -------- | -------- |
| Age | 5/10/20 | 5 |
| RestingBP | 4/10/20 | 4 |
| Cholesterol  | 7/14/28 | 7 |
| MaxHR | 2/3/6 | 6 |
| Oldpeak | 2/5/10 | 10 |

``` python
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
```
## Model Construction
1. **Decision Tree**
    Because we want to get the best classifier, we will build it with different parameters. The following table shows the parameter settings we experimented with when using sklearn.tree.DecisionTreeClassifier.

    | Parameter | Candidate | Best |
    | -------- | -------- | -------- |
    | criterion     | gini / entropy     | gini     |
    | splitter     | best / random     | best    |
    | max_depth     | 5/10/20/None     | 10    |
    | min_sample_split     | 2/3/4    | 2    |
    | min_sample_leaf     | 1/2/3    | 1     |

2. **Naives Bayes**
    * **Multinomial Naives Bayes**
    * **Gaussian Naives Bayes**
    
    In the Sklearn Bayes Classifier library, compared to the Decision Tree, there are fewer or worse parameters that can be adjusted, so we use the default parameters in the library to make predictions.
    
3. **Acuracy**
    * **Decision Tree :** 85.43%
    * **Multinomial Naives Bayes :** 86.85%
    * **Gaussian Naives Bayes :** 88.26%

``` python
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
import Data_Preprocessing
import Naive_Bayes_Classifier
import GaussianNB
import MultinomialNB
import graphviz

total_score_Naive_Bayes = 0
total_score_GaussianNB = 0
total_score_MultinomialNB = 0
total_score_DecisionTree = 0

# Bayes Classifier
for i in range(0, 10):
    # 10-Fold Cross-Validation
    train_data, test_data = train_test_split(Data_Preprocessing.dataframe, train_size=0.9, random_state=i)
    train_data.reset_index(inplace=True, drop=True)
    test_data.reset_index(inplace=True, drop=True)
    train_data_target = train_data["HeartDisease"]
    train_data_attribute = train_data.drop(columns=["HeartDisease"])
    test_data_target = test_data["HeartDisease"]
    test_data_attribute = test_data.drop(columns=["HeartDisease"])

    # Naive_Bayes_Classifier
    # predict_result_Naive_Bayes = Naive_Bayes_Classifier.predict(train_data, test_data)
    # total_score_Naive_Bayes += Naive_Bayes_Classifier.accuracy(predict_result_Naive_Bayes, test_data_target)

    # GaussianNB
    predict_result_GaussianNB = GaussianNB.predict(train_data, test_data)
    total_score_GaussianNB += GaussianNB.accuracy(predict_result_GaussianNB, test_data_target)

    # MultinomialNB
    predict_result_MultinomialNB = MultinomialNB.predict(train_data, test_data)
    total_score_MultinomialNB += MultinomialNB.accuracy(predict_result_MultinomialNB, test_data_target)

    # Decision Tree
    # Train Model
    classifier = DecisionTreeClassifier(max_depth=10, random_state=0)
    classifier.fit(train_data_attribute, train_data_target)

    # Predict Model
    test_target_predict_result = classifier.predict(test_data_attribute)
    total_score_DecisionTree += accuracy_score(test_data_target, test_target_predict_result)
    dot_data = tree.export_graphviz(classifier, out_file=None,
                                    feature_names=["Age", "Sex", "ChestPainType", "RestingBP", "Cholesterol",
                                                   "FastingBS", "RestingECG", "MaxHR", "ExerciseAngina", "Oldpeak",
                                                   "ST_Slope"],
                                    class_names=["0", "1"],
                                    filled=True, rounded=True, leaves_parallel=True)
    graph = graphviz.Source(dot_data)
    graph.view(filename="Decision Mode Tree " + str(i), directory="Tree Graph")


# score_Naive_Bayes = total_score_Naive_Bayes/10
# print('Naive_Bayes : {:.2f}%'.format(score_Naive_Bayes * 100))
score_GaussianNB = total_score_GaussianNB/10
print('GaussianNB : {:.2f}%'.format(score_GaussianNB * 100))
score_Naive_MultinomialNB = total_score_MultinomialNB/10
print('MultinomialNB : {:.2f}%'.format(score_Naive_MultinomialNB * 100))
score_DecisionTree = total_score_DecisionTree/10
print('Decision Tree : {:.2f}%'.format(score_DecisionTree * 100))
```

## Summary
Based on the results, we ranked the performance of the models in terms of accuracy:
* **Gaussian Naives Bayes :** 88.26%
* **Multinomial Naives Bayes :** 86.85%
* **Decision Tree :** 85.43%

It can be seen from the above that Decision Tree has the lowest accuracy rate, probably because Decision Tree itself is not suitable for data with a large number of categories, plus the instability is high, a little disturbance, a little change in value, the decision tree will change, and this time there are more than 900 pieces of data, for the amount of information required less Bayesian classifier, but has the advantage.

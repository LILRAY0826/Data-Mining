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
    classifier = DecisionTreeClassifier(max_depth=10, random_state=0, criterion="gini", splitter="best", min_samples_split=2, min_samples_leaf=1)
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
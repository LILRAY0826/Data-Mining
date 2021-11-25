from sklearn.model_selection import train_test_split
import Data_Preprocessing
import Naive_Bayes_Classifier

# Split Data
total_score = 0
for i in range (0, 10):
    print("Training : {:d} times.".format(i+1))
    # 10-Fold Cross-Validation
    train_data, test_data = train_test_split(Data_Preprocessing.dataframe, train_size=0.9, random_state=i)
    train_data.reset_index(inplace=True, drop=True)
    test_data.reset_index(inplace=True, drop=True)
    test_data_target = test_data["HeartDisease"]

    predict_result = Naive_Bayes_Classifier.predict(train_data, test_data)
    total_score += Naive_Bayes_Classifier.accuracy(predict_result, test_data_target)

score = total_score/10
print('{:.2f}%'.format(score * 100))

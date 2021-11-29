from sklearn.naive_bayes import GaussianNB

def predict(train_data, test_data):
    model = GaussianNB()
    attribute_train = train_data.drop(columns = ["HeartDisease"])
    label_train = train_data["HeartDisease"]
    model.fit(attribute_train, label_train)
    attribute_test = test_data.drop(columns = ["HeartDisease"])

    return model.predict(attribute_test)

def accuracy (predict_label, test_label):
    counter = 0
    for i in range (0, test_label.shape[0]):
        if predict_label[i] == test_label[i]:
            counter += 1
    return counter/test_label.shape[0]


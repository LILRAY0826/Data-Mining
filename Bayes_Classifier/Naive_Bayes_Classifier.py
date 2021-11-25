# Define Function of Calculating Both of Attribute Possibility
def possibility (dataframe, attribute, labels):
    yes_possibility = []
    no_possibility =[]
    for i in range (0, labels):
        yes_counter = 0
        no_counter = 0
        for j in range (0, dataframe.shape[0]):
            if dataframe[attribute][j] == i and dataframe["HeartDisease"][j] == 1:
                yes_counter += 1
            else:
                no_counter += 1
        yes_solo_possibility = yes_counter/dataframe.shape[0]
        no_solo_possibility = no_counter/dataframe.shape[0]
        yes_possibility.append(yes_solo_possibility)
        no_possibility.append(no_solo_possibility)
    return yes_possibility, no_possibility

def Yes_Attribute_Possibility (train_dataframe, test_dataframe, attribute, labels):
    yes_all_attribute_possibility = []
    yes_solo_attribute_possibility, no_solo_attribute_possibility = possibility(train_dataframe, attribute, labels)
    for j in range(0, test_dataframe.shape[0]):
        for i in range(0, labels):
            if test_dataframe[attribute][j] == i:
                yes_all_attribute_possibility.append(yes_solo_attribute_possibility[i])
    return yes_all_attribute_possibility

def No_Attribute_Possibility (train_dataframe, test_dataframe, attribute, labels):
    no_all_attribute_possibility = []
    yes_solo_attribute_possibility, no_solo_attribute_possibility = possibility(train_dataframe, attribute, labels)
    for j in range(0, test_dataframe.shape[0]):
        for i in range(0, labels):
            if test_dataframe[attribute][j] == i:
                no_all_attribute_possibility.append(no_solo_attribute_possibility[i])
    return no_all_attribute_possibility

def predict (train_dataframe, test_dataframe):
    # Calculate Both of Possibility of HeartDisease
    yes_disease = 0
    no_disease = 0
    for j in range(0, train_dataframe.shape[0]):
        if train_dataframe["HeartDisease"][j] == 1:
            yes_disease += 1
        else:
            no_disease += 1
    possibility_of_yes_heart_disease = yes_disease / len(train_dataframe)
    possibility_of_no_heart_disease = no_disease / len(train_dataframe)

    yes_possibility = possibility_of_yes_heart_disease
    no_possibility = possibility_of_no_heart_disease
    Attribute = ["Age", "Sex", "ChestPainType", "RestingBP", "Cholesterol", "FastingBS", "RestingECG", "MaxHR", "ExerciseAngina", "Oldpeak", "ST_Slope"]
    Labels = [5, 2, 4, 4, 7, 2, 3, 3, 2, 10, 3]
    Class_Labels = []
    for i in range(0, test_dataframe.shape[0]):
        for j in range(0, len(Attribute)):
            yes_possibility_array = Yes_Attribute_Possibility(train_dataframe, test_dataframe, Attribute[j], Labels[j])
            no_possibility_array = No_Attribute_Possibility(train_dataframe, test_dataframe, Attribute[j], Labels[j])
            yes_possibility *= yes_possibility_array[i]
            no_possibility *= no_possibility_array[i]
        if yes_possibility > no_possibility:
            class_label = 1
        else:
            class_label = 0
        Class_Labels.append(class_label)
        print("="*i + "[{:d}/{:d} epoch]".format(i+1, test_dataframe.shape[0]))
    return Class_Labels

def accuracy (predict_result, test_data_target):
    counter = 0
    for i in range (0, test_data_target.shape[0]):
        if predict_result[i] == test_data_target[i]:
            counter += 1
    return counter/test_data_target.shape[0]

def split_data(data_set):
    """
    Splits the data set into training X and Y.
    :param data_set:
    :return: X, Y
    """
    X = []
    Y = []
    for line in data_set:
        X.append(line[:14])
        Y.append(line[14])
    return X, Y

def get_data(string_list):
    """
    Convert a list of strings to a list of lists.
    :param string_list: A list of strings.
    :return: A list of lists.
    """
    data = []
    for string in string_list:
        line = string.split(',')
        int_list = [int(i) for i in line]
        data.append(int_list)
    return data

if __name__ == "__main__":
    from sklearn.ensemble import RandomForestClassifier
    from sklearn import metrics
    import pandas as pd

    clf = RandomForestClassifier(n_estimators = 200)
    with open("preprocessed_train_data.data", "r") as data_train_file:
        ini_train_data = data_train_file.readlines()
    train_data = get_data(ini_train_data)
    X_train, y_train = split_data(train_data)
    clf.fit(X_train, y_train)
    print("MODEL TRAINING COMPLETED")

    # Test the model
    data_test_file = open("preprocessed_test_data.data", "r")
    ini_test_data = data_test_file.readlines()
    test_data = get_data(ini_test_data)
    X_test, y_test = split_data(test_data)
    y_pred = clf.predict(X_test)
    print("MODEL PREDICTION COMPLETED")


    print("MODEL ACCURACY: ", metrics.accuracy_score(y_test, y_pred))

# attributes
attributes = [
    ["continuous"],
    ["Private", "Self-emp-not-inc", "Self-emp-inc", "Federal-gov", "Local-gov", "State-gov", "Without-pay", "Never-worked"],
    ["continuous"],
    ["Bachelors", "Some-college", "11th", "HS-grad", "Prof-school", "Assoc-acdm", "Assoc-voc", "9th", "7th-8th", "12th", "Masters", "1st-4th", "10th", "Doctorate", "5th-6th", "Preschool"],
    ["continuous"],
    ["Married-civ-spouse", "Divorced", "Never-married", "Separated", "Widowed", "Married-spouse-absent", "Married-AF-spouse"],
    ["Tech-support", "Craft-repair", "Other-service", "Sales", "Exec-managerial", "Prof-specialty", "Handlers-cleaners", "Machine-op-inspct", "Adm-clerical", "Farming-fishing", "Transport-moving", "Priv-house-serv", "Protective-serv", "Armed-Forces"],
    ["Wife", "Own-child", "Husband", "Not-in-family", "Other-relative", "Unmarried"],
    ["White", "Asian-Pac-Islander", "Amer-Indian-Eskimo", "Other", "Black"],
    ["Female", "Male"],
    ["continuous"],
    ["continuous"],
    ["continuous"],
    ["United-States", "Cambodia", "England", "Puerto-Rico", "Canada", "Germany", "Outlying-US(Guam-USVI-etc)", "India", "Japan", "Greece", "South", "China", "Cuba", "Iran", "Honduras", "Philippines", "Italy", "Poland", "Jamaica", "Vietnam", "Mexico", "Portugal", "Ireland", "France", "Dominican-Republic", "Laos", "Ecuador", "Taiwan", "Haiti", "Columbia", "Hungary", "Guatemala", "Nicaragua", "Scotland", "Thailand", "Yugoslavia", "El-Salvador", "Trinadad&Tobago", "Peru", "Hong", "Holand-Netherlands"],
    [">50K", "<=50K"]
]

attributes_count = len(attributes)

# replace string values with integers in the datasets
def normalize(data_set):
    for i in range(len(data_set)):
        for j in range(attributes_count):

            string = data_set[i][j]

            if j == 14:
                if ">" in string:
                    data_set[i][j] = 1
                elif "<" in string:
                    data_set[i][j] = 0
                else:
                    print("Found weird data")
            else:
                if "continuous" not in attributes[j]:
                    data_set[i][j] = attributes[j].index(string)
                else:
                    data_set[i][j] = int(string)

# removing data with missing values
def remove_missing_values(ini_data):
    data = []
    for row in ini_data:
        if('?' not in row):
            row = row.split(',')
            data.append(row)
    return data

def write_file(filename, data_set):
    with open(filename, 'w') as f:
        for row in data_set:
            for i in range(len(row)):
                f.write(str(row[i]))
                if i != len(row)-1 : f.write(',')
            f.write("\n")

if __name__ == "__main__":

    data_train_file = open("adult.data", "r")
    ini_train_data = data_train_file.readlines()
    train_data = remove_missing_values(ini_train_data)
    print(train_data[:5])
    data_train_file.close()
    print("train set length : ", len(train_data))
    normalize(train_data)
    write_file("preprocessed_train_data.data", train_data)

    data_test_file = open("adult.test", "r")
    ini_test_data = data_test_file.readlines()
    test_data = remove_missing_values(ini_test_data)
    data_test_file.close()
    print("test set length  : ", len(test_data))
    normalize(test_data)
    write_file("preprocessed_test_data.data", test_data)


import csv


def print_2d_list(arr: list[list]) -> None:
    for row in arr:
        print(row)


Y = []
X = []

with open("iris.csv", newline="") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=" ", quotechar="|")
    for row in spamreader:
        for element in row:
            element = element.split(",")
            Y.append(element.pop())
            X.append(element)
col_names = X.pop(0)
col_names.append(Y.pop(0))

print_2d_list(X)
print(Y)

print(col_names)


# Implementing a simple imuter that replaces all empty data cells by the mean of the col that the cell is present in.

mean = []

for col in range(1, len(X[0])):
    sum = 0
    n = 0
    for row in X:
        try:
            sum += int(row[col])
            n = n + 1
        except ValueError:
            continue
    mean.append(sum / n)

for col in range(1, len(X[0])):
    for row in X:
        if row[col] == "":
            row[col] = mean[col - 1]

print_2d_list(X)

print(mean)

Y_one_hot = []
for i in range(len(Y)):
    if Y[i] == '"Setosa"':
        Y_one_hot.append(-1)
    elif Y[i] == '"Versicolor"':
        Y_one_hot.append(0)
    elif Y[i] == '"Virginica"':
        Y_one_hot.append(1)

print(Y_one_hot)


# from sklearn.model_selection import train_test_split
import random

X_train, Y_train = [], []

# X_train, X_test, Y_train, Y_test = train_test_split(
#     X, Y, test_size=0.2, random_state=1
# )  # train_test_split is used to split the given datasets into training and testing dataset of given sizes.
init_len = len(X)
while len(X) > 0.8 * (init_len):
    index = random.randint(0, len(X))
    X_train.append(X.pop(index))
    Y_train.append(Y_one_hot.pop(index))

print(init_len)
print(len(X_train))


# from sklearn.preprocessing import StandardScaler

# sc = StandardScaler()
# X_train[:, 3:] = sc.fit_transform(X_train[:, 3:])
# Feature scaling is used to get all the numerical variables into same range so that it takes less time to train the model.
# # Standard Scaling makes the range (-3, 3)
# # Normalized Scaling makes the range (0, 1)
# X_test[:, 3:] = sc.transform(X_test[:, 3:])

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Read data from the file
def read_data(filename):
    with open(filename, 'r') as file:
        data = []
        for line in file:
            row = list(map(float, line.strip().split(',')))
            data.append(row)
    return np.array(data)

# Load data and separate features and labels
filename = "testing_dataset_frequency.txt"
data = read_data(filename)
X = data[:, :-1] # Features (all columns except the last one)
y = data[:, -1] # Labels (the last column)

# Split the dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create and train the kNN classifier
k = 3
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)

# Make predictions on the test set
y_pred = knn.predict(X_test)

# Evaluate the classifier
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import LabelEncoder

INPUT_FILE = "testing_dataset.txt"

# Assuming you have a DataFrame 'df' with columns "Data" and "Type"
# where "Data" is a string, and "Type" is the label
df = pd.read_csv(INPUT_FILE, header=None, names=["Data", "Type"], delimiter="|")


# Encoding the "Data" strings using LabelEncoder
data = df["Data"].apply(lambda x: [float(num) for num in x.split()]).tolist()
labels = df["Type"].values

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.3, random_state=42)

# KNN algorithm with K=3
k = 3
knn = KNeighborsClassifier(n_neighbors=k)

# Train the model using the training data
knn.fit(X_train, y_train)

# Predict the labels of the test set
y_pred = knn.predict(X_test)

# Calculate confusion matrix
cm = confusion_matrix(y_test, y_pred)

# Calculate TP, FP, TN, and FN for each class
# TP = np.diag(cm)
# FP = np.sum(cm, axis=0) - TP
# FN = np.sum(cm, axis=1) - TP
# TN = np.sum(cm) - (FP + FN + TP)

# Print the TP, FP, TN, and FN for each class
# for i, (tp, fp, tn, fn) in enumerate(zip(TP, FP, TN, FN)):
#     print(f"Class {i}: TP={tp}, FP={fp}, TN={tn}, FN={fn}")


# Print the confusion matrix and classification report
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
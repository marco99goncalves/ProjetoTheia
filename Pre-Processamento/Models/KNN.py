from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd

MAX_NUMBER = 345
JUST_CHECK_ATTACKS = True

INPUT_FILE = "testing_dataset_frequency.txt"

column_names = [f'a{i}' for i in range(MAX_NUMBER)] + ['Type']

df = pd.read_csv(INPUT_FILE, header=None, names=column_names, delimiter=" ")

if JUST_CHECK_ATTACKS:
    df.replace('AU', 'A', inplace=True)
    df.replace('HFTP', 'A', inplace=True)
    df.replace('HSSH', 'A', inplace=True)
    df.replace('J', 'A', inplace=True)
    df.replace('M', 'A', inplace=True)
    df.replace('WS', 'A', inplace=True)
    df.replace('TR', 'V', inplace=True)

target = df["Type"]
features = df.drop(["Type"], axis=1)

target = target.values
features = features.values

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.3, random_state=42)

model = KNeighborsClassifier()

# Train the model using the training data
model.fit(X_train, y_train)

# Predict the labels of the test set
y_pred = model.predict(X_test)

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

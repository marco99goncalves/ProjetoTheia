from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd
import time
import matplotlib.pyplot as plt
from sklearn import metrics
import numpy as np

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

model = RandomForestClassifier(n_estimators=100, bootstrap=False, max_features='sqrt', max_depth = 50)

# Train the model using the training data
st = time.time()
model.fit(X_train, y_train)
et = time.time()
print("Training Phase: " + str(et - st))

# Predict the labels of the test set
st = time.time()
y_pred = model.predict(X_test)
et = time.time()
print("Testing Phase: " + str(et - st))

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


y_test = np.array([(1 if xi == "A" else 0) for xi in y_test])
y_pred = np.array([(1 if xi == "A" else 0) for xi in y_pred])

fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred)
auc = metrics.roc_auc_score(y_test, y_pred)

#create ROC curve
plt.plot(fpr,tpr,label="AUC="+str(auc))
plt.ylabel('Taxa Verdadeiros Positivos')
plt.xlabel('Taxa Falsos Positivos')
plt.legend(loc=4)
plt.show()
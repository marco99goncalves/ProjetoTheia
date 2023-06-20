import pandas as pd
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, Conv1D, MaxPooling1D, Flatten, Dropout, Conv2D, Embedding
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import LabelEncoder
import time
import argparse
import os
import matplotlib.pyplot as plt
from sklearn import metrics
import numpy as np

os.environ['CUDA_VISIBLE_DEVICES'] = "1"

INPUT_FILE = "testing_dataset.txt"

parser = argparse.ArgumentParser(description="Argument parser for the window size of the LSTM model")
parser.add_argument("-w", "--window", type=int, help="Window size", required=True)
args = parser.parse_args()

column_names = [f'a{i}' for i in range(args.window+1)] + ['Type']

df = pd.read_csv(INPUT_FILE, header=None, names=column_names, delimiter=" ")

df = df.drop([f"a{args.window}"], axis=1)


df.replace('AU', 1, inplace=True)
df.replace('HFTP', 1, inplace=True)
df.replace('HSSH', 1, inplace=True)
df.replace('J', 1, inplace=True)
df.replace('M', 1, inplace=True)
df.replace('WS', 1, inplace=True)
df.replace('TR', 0, inplace=True)
df.replace('V', 0, inplace=True)

features = df.drop(["Type"], axis=1)
target = df["Type"]

#features = features.values
#target = target.values

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.3, random_state=42)

#-----------------------------------------------------------------------------------------------
#-----------------------------------CRIAÇÃO DAS CAMADAS DO MODELO------------------------------------------
# ??????????????????????????????????????????????????????????????????????????
embedding_dim = 32
max_length=args.window  #tamanho da sequencia

# create the model
model = Sequential()
model.add(Embedding(341, embedding_dim, input_length=max_length))
model.add(Flatten())
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

print(model.summary())

# Train the model using the training data
st = time.time()
model.fit(X_train, y_train, epochs=30, batch_size=1, verbose=1)
et = time.time()
print("Training Phase: " + str(et - st))

# Predict the labels of the test set
st = time.time()
y_pred = model.predict(X_test)
et = time.time()
print("Testing Phase: " + str(et - st))

prediction=[None]*len(y_pred)

for i in range(len(y_pred)):
    if y_pred[i] >= 0.5:
        prediction[i] = 1
    if y_pred[i] < 0.5:
        prediction[i] = 0

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
print(confusion_matrix(y_test, prediction))
print("\nClassification Report:")
print(classification_report(y_test, prediction))

fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred)
auc = metrics.roc_auc_score(y_test, y_pred)

#create ROC curve
plt.plot(fpr,tpr,label="AUC="+str(auc))
plt.ylabel('Taxa Verdadeiros Positivos')
plt.xlabel('Taxa Falsos Positivos')
plt.legend(loc=4)
plt.show()
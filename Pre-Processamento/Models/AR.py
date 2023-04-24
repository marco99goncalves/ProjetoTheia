import pandas as pd
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, Conv1D, MaxPooling1D, Flatten, Dropout, Conv2D, Embedding
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import LabelEncoder

INPUT_FILE = "testing_dataset.txt"

df = pd.read_csv(INPUT_FILE, header=None, names=["Data", "Type"], delimiter="|")

encoder = LabelEncoder()
data = encoder.fit_transform(df["Data"])

labels = df["Type"].values

data = data.reshape(-1, 1)  # Reshape the data for compatibility with KNeighborsClassifier

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.3, random_state=42)

#-----------------------------------------------------------------------------------------------
#-----------------------------------CRIAÇÃO DAS CAMADAS DO MODELO------------------------------------------
# ??????????????????????????????????????????????????????????????????????????
embedding_dim = 32
max_length=10  #tamanho da sequencia

# create the model
model = Sequential()
model.add(Embedding(341, embedding_dim, input_length=max_length))
model.add(Flatten())
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

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
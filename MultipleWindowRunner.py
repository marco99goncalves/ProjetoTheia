import os
import time

models = ["KNN.py", "NaiveBayes.py", "RF.py", "SVM.py"]
windows = ["2", "10"]

st = time.time()

for model in models:
    for window in windows:
        print(f"======Running Window Size of {window}======")
        os.system(f"python3 Pre-Processamento/Pipeline.py -w {window} -p")
        os.system(f"python3 Pre-Processamento/Models/{model} -w {window}")
        print("=======================================")
et = et.time()
print("Ran all windows in: " + str(et - st))
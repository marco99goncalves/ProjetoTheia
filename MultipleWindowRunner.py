import os
import time

models = ["AR.py"]
windows = ["2", "10"]

st = time.time()

for window in windows:
    os.system(f"python3 Pre-Processamento/Pipeline.py -w {window} -p")
    for model in models:
        print(f"======Running Window Size of {window}======")
        os.system(f"python3 Pre-Processamento/Models/{model} -w {window}")
        print("=======================================")
et = time.time()
print("Ran all windows in: " + str(et - st))
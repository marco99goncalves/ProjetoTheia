import os
import time

st = time.time()
for w in range(2, 11+1):
    print(f"======Running Window Size of {w}======")
    os.system(f"python3 Pre-Processamento/Pipeline.py -w {w} -p")
    os.system(f"python3 Pre-Processamento/Models/AR.py -w {w}")
    print("=======================================")
et = et.time()
print("Ran all windows in: " + str(et - st))
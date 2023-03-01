import os
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
import shutil

# Define the size of the sliding window
WINDOW_SIZE = 3
OUTPUT_FOLDER = "Outputs"
INPUT_FOLDER = "Inputs"
STEP_SIZE = 2

# Create a directory to store the output files if it doesn't already exist
if not os.path.exists(OUTPUT_FOLDER):
    os.mkdir(OUTPUT_FOLDER)

# Loop through all files in the Inputs directory
for filename in os.listdir(INPUT_FOLDER):
    # Read the input file into a list of strings
    with open(os.path.join(INPUT_FOLDER, filename), "r") as input_file:
        lines = input_file.readlines()

    data = lines[0].strip().split(" ")

    lp = 0
    windows = []
    while lp < len(data):  # Apply the sliding window
        w = data[lp:lp+WINDOW_SIZE]  # Get the numbers from the range [lp, lp+WINDOW_SIZE[
        if len(w) < WINDOW_SIZE and STEP_SIZE == 1:  # We don't allow windows < WINDOW_SIZE unless STEP_SIZE is bigger than 1
            break

        windows.append(w)
        lp += STEP_SIZE

    # Write each window to a separate file in the Outputs directory
    output_filename = os.path.join(OUTPUT_FOLDER, f"{os.path.splitext(filename)[0]}.txt")
    with open(output_filename, "w") as output_file:
        for i, window in enumerate(windows):
            output_file.write(" ".join(window) + "\n")  # Convert an array of WINDOW_SIZE numbers to a space separated string

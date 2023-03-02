import os
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
import shutil

# Define the size of the sliding window
WINDOW_SIZE = 3
OUTPUT_FILE = "dataset_merged_windowed.txt"
MERGED_DATASET_FILE = "dataset_merged.txt"
STEP_SIZE = 2

# Loop through all files in the Inputs directory
with open(MERGED_DATASET_FILE, "r") as merged_dataset_file:
    lines = merged_dataset_file.readlines()

output_lines = list()
for line in lines:
    #  Read the line and clean it for easier processing
    data, type = line.split("|")
    data = data.strip().split(" ")
    type = type.strip()

    lp = 0
    while lp < len(data):  # Apply the sliding window
        w = data[lp:lp+WINDOW_SIZE]  # Get the numbers from the range [lp, lp+WINDOW_SIZE[
        if len(w) < WINDOW_SIZE and STEP_SIZE == 1:  # We don't allow windows < WINDOW_SIZE unless STEP_SIZE is bigger than 1
            break

        windowed_line = " ".join(w) + " | " + type + "\n"  # Merge the line again
        output_lines.append(windowed_line)
        lp += STEP_SIZE

with open(OUTPUT_FILE, "w") as output_file:  # Write the output to the file
    output_file.writelines(output_lines)

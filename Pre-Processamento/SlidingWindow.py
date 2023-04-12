import os
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
import shutil
import pandas as pd

# Define the size of the sliding window
OUTPUT_FILE = "dataset_merged_windowed.txt"
MERGED_DATASET_FILE = "dataset_merged.txt"


def sliding_window(numbers, W):
    """
    Apply sliding window of size W on a list of numbers.
    """
    series = pd.Series(numbers)
    return series.rolling(window=W, min_periods=W)


def run(WINDOW_SIZE = 3):
    # Loop through all files in the Inputs directory
    with open(MERGED_DATASET_FILE, "r") as merged_dataset_file:
        lines = merged_dataset_file.readlines()

    output_lines = list()
    for line in lines:
        #  Read the line and clean it for easier processing
        split_line = line.strip().split(" ")
        data = split_line[:-1]
        data_type = split_line[-1:][0]

        # Example usage
        windowed = sliding_window(data, WINDOW_SIZE)

        for i, w in enumerate(windowed):
            if len(w) >= WINDOW_SIZE:
                output_lines.append(" ".join(w.to_list()) + " | " + data_type + "\n")

    with open(OUTPUT_FILE, "w") as output_file:  # Write the output to the file
        output_file.writelines(output_lines)

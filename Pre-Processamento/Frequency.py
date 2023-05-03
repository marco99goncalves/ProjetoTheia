import os
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
import shutil

# Define the size of the sliding window
WINDOWED_FILE = "dataset_merged_windowed.txt"
FREQUENCY_FILE = "frequency.txt"
MAX_NUMBER = 345  # Confirm with professor

def run():
    # Loop through all files in the Inputs directory
    with open(WINDOWED_FILE, "r") as windowed_file:
        lines = windowed_file.readlines()

    output_lines = list()
    for line in lines:
        new_line = line.split("|")
        #  Read the line and clean it for easier processing
        data = new_line[0].strip().split(" ")
        data_type = new_line[1].strip()

        count_array = [0] * (MAX_NUMBER)
        for num in data:
            try:
                count_array[int(num)] += 1
            except:
                print(num)

        frequency_line = ""
        for num in count_array:
            frequency_line += str(num) + " "
        frequency_line += data_type + "\n"

        output_lines.append(frequency_line)

    with open(FREQUENCY_FILE, "w") as output_file:  # Write the output to the file
        output_file.writelines(output_lines)

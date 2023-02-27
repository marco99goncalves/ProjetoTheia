import os
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
import shutil

# Define the size of the sliding window
WINDOW_SIZE = 3
OUTPUT_FOLDER = "Outputs"
INPUT_FOLDER = "Inputs"
STEP_SIZE = 1


def strided_app(a, L, S):  # Window len = L, Stride len/stepsize = S
    nrows = ((a.size - L) // S) + 1
    n = a.strides[0]
    return np.lib.stride_tricks.as_strided(a, shape=(nrows, L), strides=(S * n, n))


# Create a directory to store the output files if it doesn't already exist
if not os.path.exists(OUTPUT_FOLDER):
    os.mkdir(OUTPUT_FOLDER)

# Loop through all files in the Inputs directory
for filename in os.listdir(INPUT_FOLDER):
    # Read the input file into a list of strings
    with open(os.path.join(INPUT_FOLDER, filename), "r") as input_file:
        lines = input_file.readlines()

    data = lines[0].strip().split(" ")
    # windows = sliding_window_view(data, window_shape=WINDOW_SIZE)[::OVERLAP]
    # windows = strided_app(data, L=WINDOW_SIZE, S=OVERLAP)
    # print(windows)

    lp = 0
    windows = []
    while lp < len(data):
        w = data[lp:lp+WINDOW_SIZE]
        if len(w) < WINDOW_SIZE and STEP_SIZE == 1:  # We don't allow windows < WINDOW_SIZE unless STEP_SIZE is bigger than 1
            break

        windows.append(w)
        lp += STEP_SIZE

    print(windows)

    # Apply a sliding window of size WINDOW_SIZE to the data
    # windows = [" ".join(data[i:i + WINDOW_SIZE]) for i in range(0, len(data) - WINDOW_SIZE + 2, STEP_SIZE)]
    #
    # output_folder = os.path.join(OUTPUT_FOLDER, os.path.splitext(filename)[0])  # "OUTPUT_FOLDER/[current_input]/"
    #
    # if os.path.exists(output_folder):  # If the folder already exists, remove it, since we don't want to mix outputs
    #     shutil.rmtree(output_folder)
    # os.makedirs(output_folder)
    #
    # # Write each window to a separate file in the Outputs directory
    # for i, window in enumerate(windows):
    #     output_filename = os.path.join(OUTPUT_FOLDER, os.path.splitext(filename)[0], f"{i}.txt")
    #     with open(output_filename, "w") as output_file:
    #         output_file.write(window)

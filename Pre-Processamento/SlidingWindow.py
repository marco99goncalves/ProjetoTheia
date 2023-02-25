import os

# Define the size of the sliding window
WINDOW_SIZE = 10
OUTPUT_FOLDER = "Outputs";

# Create a directory to store the output files if it doesn't already exist
if not os.path.exists(OUTPUT_FOLDER):
    os.mkdir(OUTPUT_FOLDER)

# Loop through all files in the Inputs directory
for filename in os.listdir("Inputs"):
    # Read the input file into a list of strings
    with open(os.path.join("Inputs", filename), "r") as input_file:
        lines = input_file.readlines()
    
    data = lines[0].split(" ");

    # Apply a sliding window of size WINDOW_SIZE to the data
    windows = ["".join(data[i:i+WINDOW_SIZE]) for i in range(len(data)-WINDOW_SIZE+1)]

    os.makedirs(os.path.join(OUTPUT_FOLDER, os.path.splitext(filename)[0]))

    # Write each window to a separate file in the Outputs directory
    for i, window in enumerate(windows):
        output_filename = os.path.join(OUTPUT_FOLDER, os.path.splitext(filename)[0], f"{i}.txt")
        with open(output_filename, "w") as output_file:
            output_file.write(window)

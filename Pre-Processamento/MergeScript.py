import os

INPUT_FOLDER = "Inputs"
STEP_SIZE = 2

f = open("dataset_merged.txt", "w")

# Loop through all files in the Inputs directory
lines = list()
for root, dir, files in os.walk(INPUT_FOLDER):
    for file in files:
        cur_file_path = os.path.join(root, file)

        with open(cur_file_path, "r") as input_file:
            line = input_file.readline().strip().split(" ")  # Gives the current files content in list form

        if cur_file_path.lower().find("attack") != -1:
            file_type = "A"
        elif cur_file_path.lower().find("training") != -1:
            file_type = "T"
        else:
            file_type = "V"

        file_lower = file.lower()
        if file_type == "A":  # Get the attack type
            if file_lower.find("adduser") != -1:
                file_type = "AU"
            elif file_lower.find("hydra-ftp") != -1:
                file_type = "HFTP"
            elif file_lower.find("hydra-ssh") != -1:
                file_type = "HSSH"
            elif file_lower.find("java") != -1:
                file_type = "J"
            elif file_lower.find("meterpreter") != -1:
                file_type = "M"
            else:
                file_type = "WS"

        lines.append(" ".join(line) + " " + file_type + "\n")

f.writelines(lines)
f.close()
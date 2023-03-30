import pandas as pd

INPUT_MERGED_FILE = "dataset_merged_windowed.txt"
ATTACK_TYPES = 6

df = pd.read_csv(INPUT_MERGED_FILE, header=None, names=["Data", "Type"], delimiter="|")

df = df.drop_duplicates(); # Removes duplicate lines, since they offer no information


# ATTACKS
add_user_rows = df[df['Type'].str.eq('AU')]
add_user_rows_sampled = add_user_rows.sample(frac=0.1666667) # Sample a x% of rows randomly,  random_state=seed sets the seed

hydra_ftp_rows = df[df['Type'].str.eq('HFTP')]
hydra_ftp_rows_sampled = hydra_ftp_rows.sample(frac=0.1666667)

hydra_ssh_rows = df[df['Type'].str.eq('HSSH')]
hydra_ssh_sampled = hydra_ssh_rows.sample(frac=0.1666667)

java_rows = df[df['Type'].str.eq('J')]
java_rows_sampled = java_rows.sample(frac=0.1666667)

meterpreter_rows = df[df['Type'].str.eq('M')]
meterpreter_rows_sampled = meterpreter_rows.sample(frac=0.1666667)

web_shell_rows = df[df['Type'].str.eq('WS')]
web_shell_rows_sampled = web_shell_rows.sample(frac=0.1666667)


# TRAINING AND VALIDATION

training_rows = df[df['Type'].str.eq('T')]
training_rows_sampled = training_rows.sample(frac=0.25)

validation_rows = df[df['Type'].str.eq('V')]
validation_rows_sampled = validation_rows.sample(frac=0.25)


# TODO Confirm with professor if we should make this more modular
final_df = pd.concat([add_user_rows_sampled, hydra_ftp_rows_sampled, hydra_ssh_sampled, java_rows_sampled, meterpreter_rows_sampled, web_shell_rows_sampled, training_rows_sampled, validation_rows_sampled], axis=0)
import pandas as pd
import csv

INPUT_MERGED_FILE = "dataset_merged_windowed.txt"
OUTPUT_FILE = "dataset_subset.txt"

def run(attack, validation, training):
    df = pd.read_csv(INPUT_MERGED_FILE, header=None, names=["Data", "Type"], delimiter="|")
    df = df.drop_duplicates() # Removes duplicate lines, since they offer no information

    # ATTACKS
    add_user_rows = df[df["Type"].str.contains("AU")]
    add_user_rows_sampled = add_user_rows.sample(frac=attack) # Sample a x% of rows randomly,  random_state=seed sets the seed

    hydra_ftp_rows = df[df['Type'].str.contains('HFTP')]
    hydra_ftp_rows_sampled = hydra_ftp_rows.sample(frac=attack)

    hydra_ssh_rows = df[df['Type'].str.contains('HSSH')]
    hydra_ssh_sampled = hydra_ssh_rows.sample(frac=attack)

    java_rows = df[df['Type'].str.contains('J')]
    java_rows_sampled = java_rows.sample(frac=attack)

    meterpreter_rows = df[df['Type'].str.contains('M')]
    meterpreter_rows_sampled = meterpreter_rows.sample(frac=attack)

    web_shell_rows = df[df['Type'].str.contains('WS')]
    web_shell_rows_sampled = web_shell_rows.sample(frac=attack)


    # TRAINING AND VALIDATION

    training_rows = df[df['Type'].str.contains('TR')]
    training_rows_sampled = training_rows.sample(frac=training)

    validation_rows = df[df['Type'].str.contains('V')]
    validation_rows_sampled = validation_rows.sample(frac=validation)

    final_df = pd.concat([add_user_rows_sampled, hydra_ftp_rows_sampled, hydra_ssh_sampled, java_rows_sampled, meterpreter_rows_sampled, web_shell_rows_sampled, training_rows_sampled, validation_rows_sampled], axis=0)
    final_df.to_csv(OUTPUT_FILE, index=False, header=False, sep='|', quoting=csv.QUOTE_NONE)

if __name__ == "__main__":
    run(0.1666667, 0.25, 0.25)

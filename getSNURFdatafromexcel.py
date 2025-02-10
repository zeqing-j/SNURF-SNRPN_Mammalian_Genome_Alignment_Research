#get information from excel after get unique SNURFs
import pandas as pd

def extract_uorf_data(transcript_file, excel_file, output_file):
    # Load the Excel file
    df = pd.read_excel(excel_file)

    # Open the transcript file and output file
    with open(transcript_file, 'r') as tf, open(output_file, 'w') as of:
        lines = tf.readlines()

        # Process transcript_file by groups of 3 lines
        for i in range(0, len(lines), 3):
            transcript_name = lines[i].strip()
            short_uorf = lines[i + 1].strip()
            long_uorf = lines[i + 2].strip()

            # Search for short uORF in the Excel file
            short_row = df[
                (df["5' UTR Name"] == transcript_name) &
                (df["ORF Type"].str.split(" ").str[0] == "uORF") &
                (df["ORF Sequence"].str.upper() == short_uorf.upper())
            ]

            # Search for long uORF in the Excel file
            long_row = df[
                (df["5' UTR Name"] == transcript_name) &
                (df["ORF Type"].str.split(" ").str[0] == "uORF") &
                (df["ORF Sequence"].str.upper() == long_uorf.upper())
            ]

            # Extract and write short uORF details if found
            if not short_row.empty:
                short_start = short_row.iloc[0]["Start Index"]
                short_end = short_row.iloc[0]["End Index"]
                short_percentage = short_row.iloc[0]["Total Percentage"]
                of.write(f"{transcript_name} {short_uorf} {short_start} {short_end} {short_percentage}\n")

            # Extract and write long uORF details if found
            if not long_row.empty:
                long_start = long_row.iloc[0]["Start Index"]
                long_end = long_row.iloc[0]["End Index"]
                long_percentage = long_row.iloc[0]["Total Percentage"]
                of.write(f"{transcript_name} {long_uorf} {long_start} {long_end} {long_percentage}\n")

# Define file paths
transcript_file = "/ocean/projects/bio200049p/zjiang2/Files/spring25/unique_transcripts.txt"  # Replace with the path to the transcript file
excel_file = "/ocean/projects/bio200049p/zjiang2/Files/spring24/new_species_match_analysis_plus_percent.xlsx"  # Replace with the path to the Excel file
output_file = "/ocean/projects/bio200049p/zjiang2/Files/spring25/SNURFuniquedata.txt"  # Replace with the desired output file path

# Run the script
extract_uorf_data(transcript_file, excel_file, output_file)

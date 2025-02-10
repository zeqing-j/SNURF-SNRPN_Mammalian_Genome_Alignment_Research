# to find the indexes of short uORF, long uORF in the excel file after finding the SNURF-like sequences
import os
import pandas as pd

def process_files_and_excel(directory, excel_file, output_file):
    # Read the Excel file
    df = pd.read_excel(excel_file)

    # Create or overwrite the output text file
    with open(output_file, 'w') as output:
        # Iterate over each file in the directory
        for file_name in os.listdir(directory):
            # Check if it matches the files in the Excel file's first column
            matching_rows = df[df.iloc[:, 0] == file_name]

            if not matching_rows.empty:
                # Filter rows based on the ORF type and sequence length criteria
                for _, row in matching_rows.iterrows():
                    orf_type = row['ORF type']
                    orf_type_split = orf_type.split(" ")[0]
                    orf_sequence = row['ORF Sequence']
                    sequence_length = len(orf_sequence)

                    if (
                        orf_type_split == "uORF" and
                        (sequence_length < 30 or 45 <= sequence_length <= 300)
                    ):
                        # Extract required fields
                        utr_name = row["5' UTR Name"]
                        start_index = row["Start Index"]
                        end_index = row["End Index"]
                        total_percentage = row["Total Percentage"]

                        # Write to the output file
                        output.write(f"{utr_name} {orf_type} {orf_sequence} {start_index} {end_index} {total_percentage}\n")

if __name__ == "__main__":
    # Define paths
    directory = "/ocean/projects/bio200049p/zjiang2/Files/spring25/SNURF-like"  # Replace with the actual directory path
    excel_file = "/ocean/projects/bio200049p/zjiang2/Files/spring24/new_species_match_analysis_plus_percent.xlsx"  # Replace with the actual Excel file path
    output_file = "/ocean/projects/bio200049p/zjiang2/Files/spring25/SNURFseqinfo.txt"  # Replace with the desired output file name

    # Call the function
    process_files_and_excel(directory, excel_file, output_file)

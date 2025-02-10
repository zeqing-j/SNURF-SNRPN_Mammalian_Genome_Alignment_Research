import os
import pandas as pd
import shutil

def process_excel_and_files(excel_file, input_dir, output_dir, output_text_file):
    # Read and sort the Excel file by 5' UTR Name
    df = pd.read_excel(excel_file)
    df.sort_values(by="5' UTR Name", inplace=True)

    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Prepare the output text file
    with open(output_text_file, 'w') as output_file:
        grouped = df.groupby("5' UTR Name")

        for utr_name, group in grouped:
            # Filter rows with uORFs of required lengths
            uorfs = group[group['ORF Type'].str.split(" ").str[0] == "uORF"]
            valid_uorfs = uorfs[(uorfs['ORF Sequence'].str.len() <= 30) | 
                                ((uorfs['ORF Sequence'].str.len() >= 45) & (uorfs['ORF Sequence'].str.len() <= 300))]

            # Check if the 5' UTR Name has both short and long uORFs
            has_short_uorf = not valid_uorfs[valid_uorfs['ORF Sequence'].str.len() <= 30].empty
            has_long_uorf = not valid_uorfs[(valid_uorfs['ORF Sequence'].str.len() >= 45) & 
                                            (valid_uorfs['ORF Sequence'].str.len() <= 300)].empty

            if not (has_short_uorf and has_long_uorf):
                continue

            # Extract start, end, and sequences
            utr_uorfs = []
            for _, row in valid_uorfs.iterrows():
                utr_uorfs.append((row['Start Index'], row['End Index'], row['ORF Sequence'].upper()))

            # Find the file corresponding to the 5' UTR Name
            input_file = os.path.join(input_dir, utr_name)
            if not os.path.isfile(input_file):
                continue

            with open(input_file, 'r') as f:
                lines = f.readlines()
                if len(lines) < 2:
                    continue
                second_line = lines[1].strip()

            # Verify sequences and check distances
            sequences_verified = []
            for start, end, orf_seq in utr_uorfs:
                extracted_seq = second_line[start:end].replace("-", "")
                if extracted_seq == orf_seq:
                    sequences_verified.append((start, end, extracted_seq))

            if len(sequences_verified) < 2:
                continue

            short_long_pairs = []
            for i, (short_start, short_end, short_seq) in enumerate(sequences_verified):
                if len(short_seq) > 30:
                    continue
                for j, (long_start, long_end, long_seq) in enumerate(sequences_verified):
                    if i == j or len(long_seq) < 45:
                        continue

                    # Remove dashes to calculate actual distance
                    subseq_between = second_line[short_end:long_start].replace("-", "")
                    actual_distance = len(subseq_between)

                    if 0 <= actual_distance <= 50:
                        short_long_pairs.append((short_seq, long_seq))

            if not short_long_pairs:
                continue

            # Copy file to output directory and write details to the text file
            shutil.copy(input_file, output_dir)

            for short_seq, long_seq in short_long_pairs:
                output_file.write(f"{utr_name}\n")
                output_file.write(f"{short_seq}\n")
                output_file.write(f"{long_seq}\n")

# Define paths
excel_file = "/ocean/projects/bio200049p/zjiang2/Files/spring24/new_species_match_analysis_plus_percent.xlsx"  # Replace with your Excel file path
input_dir = "/ocean/projects/bio200049p/zjiang2/Files/spring24/corrected_fasta"  # Replace with your input directory path
output_dir = "/ocean/projects/bio200049p/zjiang2/Files/spring25/SNURF-like"  # Replace with your output directory path
output_text_file = "/ocean/projects/bio200049p/zjiang2/Files/spring25/SNURFinfo.txt"  # Replace with your desired output text file path

# Run the script
process_excel_and_files(excel_file, input_dir, output_dir, output_text_file)

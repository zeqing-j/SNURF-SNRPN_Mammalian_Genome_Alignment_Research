#get information from excel after get unique SNURFs
import pandas as pd

def extract_uorf_data(transcript_file, excel_file, output_file):
    df = pd.read_excel(excel_file)
    with open(transcript_file, 'r') as tf, open(output_file, 'w') as of:
        lines = tf.readlines()

        for i in range(0, len(lines), 3):
            transcript_name = lines[i].strip()
            short_uorf = lines[i + 1].strip()
            long_uorf = lines[i + 2].strip()
            short_row = df[
                (df["5' UTR Name"] == transcript_name) &
                (df["ORF Type"].str.split(" ").str[0] == "uORF") &
                (df["ORF Sequence"].str.upper() == short_uorf.upper())
            ]
            long_row = df[
                (df["5' UTR Name"] == transcript_name) &
                (df["ORF Type"].str.split(" ").str[0] == "uORF") &
                (df["ORF Sequence"].str.upper() == long_uorf.upper())
            ]
            
            if not short_row.empty:
                short_start = short_row.iloc[0]["Start Index"]
                short_end = short_row.iloc[0]["End Index"]
                short_percentage = short_row.iloc[0]["Total Percentage"]
                of.write(f"{transcript_name} {short_uorf} {short_start} {short_end} {short_percentage}\n")

            
            if not long_row.empty:
                long_start = long_row.iloc[0]["Start Index"]
                long_end = long_row.iloc[0]["End Index"]
                long_percentage = long_row.iloc[0]["Total Percentage"]
                of.write(f"{transcript_name} {long_uorf} {long_start} {long_end} {long_percentage}\n")


transcript_file = "/ocean/projects/bio200049p/zjiang2/Files/spring25/unique_transcripts.txt"  
excel_file = "/ocean/projects/bio200049p/zjiang2/Files/spring24/new_species_match_analysis_plus_percent.xlsx"  
output_file = "/ocean/projects/bio200049p/zjiang2/Files/spring25/SNURFuniquedata.txt" 

extract_uorf_data(transcript_file, excel_file, output_file)

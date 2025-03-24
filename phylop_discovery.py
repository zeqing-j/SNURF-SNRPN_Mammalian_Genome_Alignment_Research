#to get the transcripts with high phylop difference and find relationship with conservation
import pandas as pd

transcripts = []
with open("/ocean/projects/bio200049p/zjiang2/Files/spring25/phylopdiff.txt", "r") as file:
    lines = file.readlines()
    for i in range(0, len(lines), 3):
        name = lines[i].strip()
        phylop1, phylop2 = map(float, lines[i+1].strip().split(","))
        difference = float(lines[i+2].strip())
        transcripts.append((name, phylop1, phylop2, difference))

df = pd.DataFrame(transcripts, columns=["Transcript", "Phylop1", "Phylop2", "Difference"])

df_filtered = df[df["Difference"] < 0]  # Keep only rows with negative differences
df_filtered = df_filtered.nsmallest(len(df_filtered) // 2, "Difference")  # Top 50% most negative

excel_file = "/ocean/projects/bio200049p/zjiang2/Files/spring24/new_species_match_analysis.xlsx"
output_file = "/ocean/projects/bio200049p/zjiang2/Files/spring25/phylop_conservation.xlsx"
excel_data = pd.read_excel(excel_file)

# Filter rows in Excel file
matched_rows = excel_data[excel_data.iloc[:, 0].isin(df_filtered["Transcript"])]

# Add the difference column
matched_rows = matched_rows.copy() 
matched_rows["Phylop Difference"] = matched_rows.iloc[:, 0].map(df_filtered.set_index("Transcript")["Difference"])
matched_rows.to_excel(output_file, index=False)

#to get the transcripts with high phylop difference and find relationship with conservation
import pandas as pd

# Step 1: Parse the text file
transcripts = []
with open("/ocean/projects/bio200049p/zjiang2/Files/spring25/phylopdiff.txt", "r") as file:
    lines = file.readlines()
    for i in range(0, len(lines), 3):
        name = lines[i].strip()
        phylop1, phylop2 = map(float, lines[i+1].strip().split(","))
        difference = float(lines[i+2].strip())
        transcripts.append((name, phylop1, phylop2, difference))

# Convert to DataFrame for easier processing
df = pd.DataFrame(transcripts, columns=["Transcript", "Phylop1", "Phylop2", "Difference"])

# Step 2: Filter out transcripts
df_filtered = df[df["Difference"] < 0]  # Keep only rows with negative differences
df_filtered = df_filtered.nsmallest(len(df_filtered) // 2, "Difference")  # Top 50% most negative

# Step 3: Search in Excel
excel_file = "/ocean/projects/bio200049p/zjiang2/Files/spring24/new_species_match_analysis.xlsx"
output_file = "/ocean/projects/bio200049p/zjiang2/Files/spring25/phylop_conservation.xlsx"
excel_data = pd.read_excel(excel_file)

# Filter rows in Excel file
matched_rows = excel_data[excel_data.iloc[:, 0].isin(df_filtered["Transcript"])]

# Add the difference column
matched_rows = matched_rows.copy()  # Ensure no SettingWithCopyWarning
matched_rows["Phylop Difference"] = matched_rows.iloc[:, 0].map(df_filtered.set_index("Transcript")["Difference"])

# Step 4: Save the results
matched_rows.to_excel(output_file, index=False)

print(f"Filtered data saved to {output_file}")

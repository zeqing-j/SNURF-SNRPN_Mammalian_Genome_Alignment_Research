#to find the seqeunce with SNURF structure in the phylop excel file to see if there are patterns
import pandas as pd

# List of names to search
names_to_search = [
    "ENST00000263710.8.txt", "ENST00000360273.7.txt", "ENST00000382150.8.txt", "ENST00000447325.5.txt",
    "ENST00000529611.5.txt", "ENST00000274811.9.txt", "ENST00000367434.5.txt", "ENST00000389858.4.txt",
    "ENST00000454775.5.txt", "ENST00000543283.2.txt", "ENST00000282928.5.txt", "ENST00000367685.5.txt",
    "ENST00000397077.6.txt", "ENST00000455322.6.txt", "ENST00000624776.3.txt", "ENST00000288840.10.txt",
    "ENST00000370272.9.txt", "ENST00000399351.7.txt", "ENST00000462443.2.txt", "ENST00000642456.1.txt",
    "ENST00000311534.6.txt", "ENST00000373525.9.txt", "ENST00000401558.7.txt", "ENST00000468789.5.txt",
    "ENST00000642620.1.txt", "ENST00000319394.8.txt", "ENST00000379214.9.txt", "ENST00000379388.7.txt",
    "ENST00000420358.2.txt", "ENST00000482871.6.txt", "ENST00000647152.1.txt", "ENST00000333305.5.txt",
    "ENST00000525503.5.txt", "ENST00000649271.1.txt"
]

# Load the Excel file
input_file = r"C:\Users\zeqin\Downloads\phylop_conservation.xlsx"  # Replace with your actual file name
df = pd.read_excel(input_file)

# Filter rows where the first column matches the names to search
filtered_rows = df[df.iloc[:, 0].isin(names_to_search)]

# Select specific columns to display
columns_to_print = ["5' UTR Name", "ORF Type", "ORF Sequence", "Total Percentage", "Phylop Difference"]

# Display the relevant rows with selected columns
if not filtered_rows.empty:
    result = filtered_rows[columns_to_print]
    print(result)
else:
    print("No matching names found.")

# Optionally, save the filtered results to a new Excel file
output_file = r"C:\Users\zeqin\Downloads\filtered_results.xlsx"
result.to_excel(output_file, index=False)
print(f"Filtered data saved to {output_file}")

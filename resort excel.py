import pandas as pd

input_file = r"C:\Users\zeqin\Desktop\Research\winter25\new_translation_analysis_filter_gene.xlsx" 
output_file = r"C:\Users\zeqin\Desktop\Research\winter25\filterby_proteinseq.xlsx" 

df = pd.read_excel(input_file)

required_columns = [
    'transcript_id', 'ORF Type', 'Human Protein Sequence', 'geneSymbol',
    'Priority Score'
]


missing_columns = [col for col in required_columns if col not in df.columns]
if missing_columns:
    print("Missing columns in the input file:", missing_columns)
else:
    df['geneSymbol'] = df['geneSymbol'].astype(str).replace('nan', '')

    # Group by 'geneSymbol', 'Human Protein Sequence', 'ORF Type'
    grouped = df.groupby(['geneSymbol', 'Human Protein Sequence', 'ORF Type'], as_index=False).agg(
        transcript_id=('transcript_id', lambda x: ', '.join(x.unique())),
        Highest_Priority_Score=('Priority Score', 'max')
    )

    grouped_sorted = grouped.sort_values(by='geneSymbol')

    grouped_sorted.to_excel(output_file, index=False)

    print(f"Processed data has been written to '{output_file}' successfully.")

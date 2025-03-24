import os
from collections import defaultdict

def calculate_conservation_rate(dna_sequences):
    "Calculate the conservation rate for the first two nucleotides and the third nucleotide of each codon."
    num_sequences = len(dna_sequences)
    codon_conservation_first_two = []
    codon_conservation_third = []

    codons = list(zip(*[seq[i:i+3] for seq in dna_sequences for i in range(0, len(seq), 3)]))

    for codon_positions in codons:
        first_two_count = defaultdict(int)
        third_count = defaultdict(int)

        for codon in codon_positions:
            if len(codon) == 3: 
                first_two_count[codon[:2]] += 1
                third_count[codon[2]] += 1

        first_two_conservation = max(first_two_count.values()) / num_sequences
        third_conservation = max(third_count.values()) / num_sequences

        codon_conservation_first_two.append(first_two_conservation)
        codon_conservation_third.append(third_conservation)

    return codon_conservation_first_two, codon_conservation_third

def process_files(input_dir, output_dir):
    "Process files in the input directory, calculate conservation rates, and write to the output directory."
    for file_name in os.listdir(input_dir):
        if not file_name.endswith(".txt"):
            continue

        output_file_name = file_name.split("_")[0] + ".txt"
        output_file_path = os.path.join(output_dir, output_file_name)
        with open(os.path.join(input_dir, file_name), "r") as file:
            lines = file.readlines()

        species_dna_lengths = defaultdict(list)
        for i in range(0, len(lines), 3):
            species = lines[i].strip()
            dna_sequence = lines[i+1].strip()

            species_dna_lengths[len(dna_sequence)].append(dna_sequence)

        # Find the DNA length with the highest number of species
        most_common_length = max(species_dna_lengths.keys(), key=lambda x: len(species_dna_lengths[x]))
        dna_sequences = species_dna_lengths[most_common_length]

        first_two_rates, third_rates = calculate_conservation_rate(dna_sequences)

        first_two_conservation_str = ";".join(map(str, first_two_rates))
        third_conservation_str = ";".join(map(str, third_rates))
        conservation_output = f"{first_two_conservation_str},{third_conservation_str}\n"
        
        with open(output_file_path, "w") as output_file:
            output_file.write(conservation_output)


input_directory = "/ocean/projects/bio200049p/zjiang2/Files/spring24/test_translated_conservation"
output_directory = "/ocean/projects/bio200049p/zjiang2/Files/spring24/codon_conservation"

os.makedirs(output_directory, exist_ok=True)
process_files(input_directory, output_directory)

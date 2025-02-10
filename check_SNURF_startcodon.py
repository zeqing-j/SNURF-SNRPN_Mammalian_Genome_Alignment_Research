import os
import shutil

def check_conditions_and_copy(input_dir1, input_dir2, text_file, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Read the filenames and conditions from the text file
    with open(text_file, 'r') as file:
        lines = file.readlines()

    # Get the list of filenames in the first directory
    input_dir1_files = set(os.listdir(input_dir1))

    # Iterate over the odd lines in the text file
    for i in range(0, len(lines), 2):  # Odd lines (0-based index)
        odd_line = lines[i].strip().split(" ")
        filename = odd_line[0]

        # Only process if the filename exists in the first directory
        if filename in input_dir1_files:
            if len(odd_line[1]) <= 30:  # Ensure the second element length <= 30
                next_line = lines[i + 1].strip().split(" ")

                if int(next_line[-1]) > 75 and 45 <= len(next_line[1]) <= 300:
                    start_idx = int(odd_line[2])
                    end_idx = int(odd_line[3])

                    # Find and process the corresponding file in the second directory
                    file_path2 = os.path.join(input_dir2, filename)
                    if os.path.exists(file_path2):
                        with open(file_path2, 'r') as f:
                            even_lines = f.readlines()[1::2]  # Get even lines

                        valid_lines = 0
                        for line in even_lines:
                            line = line.strip()
                            start_codon = line[start_idx:start_idx + 3]
                            stop_codon = line[end_idx - 3:end_idx]

                            if start_codon == "ATG" and stop_codon in {"TAA", "TAG", "TGA"}:
                                valid_lines += 1

                        # Check if codons exist in 75% of the even lines
                        if valid_lines / len(even_lines) >= 0.75:
                            # Copy the file from the first directory to the output directory
                            input_file1_path = os.path.join(input_dir1, filename)
                            if os.path.exists(input_file1_path):
                                shutil.copy(input_file1_path, output_dir)


# Example usage
input_directory1 = "/ocean/projects/bio200049p/zjiang2/Files/spring25/SNURF-unique"
input_directory2 = "/ocean/projects/bio200049p/zjiang2/Files/spring24/fasta_corrected"
input_text_file = "/ocean/projects/bio200049p/zjiang2/Files/spring25/SNURFuniquedata.txt"
output_directory = "/ocean/projects/bio200049p/zjiang2/Files/spring25/SNURF-final"

check_conditions_and_copy(input_directory1, input_directory2, input_text_file, output_directory)

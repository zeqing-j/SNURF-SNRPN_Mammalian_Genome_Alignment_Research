import os
import shutil

def validate_and_process_file(input_file, input_dir, output_dir):
    stop_codons = {"TAA", "TAG", "TGA"}

    # Function to check if a sequence is a valid uORF
    def is_valid_uorf(sequence, max_length):
        if not sequence.startswith("ATG"):
            return False
        if len(sequence) > max_length:
            return False
        for i in range(3, len(sequence) - 2, 3):
            if sequence[i:i + 3] in stop_codons:
                return True
        return False

    # Validate file content
    with open(input_file, 'r') as file:
        lines = file.readlines()

    if len(lines) % 3 != 0:
        raise ValueError("File does not follow the pattern of 3 lines per transcript.")

    validated_data = []
    for i in range(0, len(lines), 3):
        transcript_name = lines[i].strip()
        short_uorf = lines[i + 1].strip()
        long_uorf = lines[i + 2].strip()

        if not transcript_name.startswith("ENST"):
            print("Pattern mismatch:", lines[i:i + 3])
            continue

        if not is_valid_uorf(short_uorf, 30):
            print("Pattern mismatch:", lines[i:i + 3])
            continue

        if not is_valid_uorf(long_uorf, 300) or len(long_uorf) < 45:
            print("Pattern mismatch:", lines[i:i + 3])
            continue

        validated_data.append((transcript_name, short_uorf, long_uorf))

    # Remove duplicates based on short and long uORFs
    unique_data = {}
    for transcript_name, short_uorf, long_uorf in validated_data:
        key = (short_uorf, long_uorf)
        if key not in unique_data:
            unique_data[key] = transcript_name

    # Write the unique entries back to a new file
    unique_output_file = "unique_transcripts.txt"
    with open(unique_output_file, 'w') as file:
        for (short_uorf, long_uorf), transcript_name in unique_data.items():
            file.write(f"{transcript_name}\n{short_uorf}\n{long_uorf}\n")

    # Copy files to output directory
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for transcript_name in unique_data.values():
        input_path = os.path.join(input_dir, transcript_name)
        if os.path.exists(input_path):
            shutil.copy(input_path, output_dir)

# Define paths
input_file = "/ocean/projects/bio200049p/zjiang2/Files/spring25/SNURFinfo.txt"  # Replace with your text file path
input_dir = "/ocean/projects/bio200049p/zjiang2/Files/spring25/SNURF-like"  # Replace with your input directory path
output_dir = "/ocean/projects/bio200049p/zjiang2/Files/spring25/SNURF-unique"  # Replace with your output directory path

# Run the script
validate_and_process_file(input_file, input_dir, output_dir)


import os
import shutil

def validate_and_copy(input_txt_file, input_directory, output_directory):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    with open(input_txt_file, 'r') as txt_file:
        lines = txt_file.readlines()

        # Process every second line for validation
        for i in range(1, len(lines), 2):
            line = lines[i].strip()
            elements = line.split()

            # Validate if Total Percentage (last element) > 75
            total_percentage = float(elements[-1])
            transcript_name = elements[0]

            if total_percentage > 75:
                # Copy the transcript file
                input_file_path = os.path.join(input_directory, transcript_name)
                if os.path.isfile(input_file_path):
                    shutil.copy(input_file_path, output_directory)
                else:
                    print(f"File not found: {input_file_path}")

# Define paths
input_txt_file = "/ocean/projects/bio200049p/zjiang2/Files/spring25/SNURFuniquedata.txt "  # Replace with the path to the input text file
input_dir = "/ocean/projects/bio200049p/zjiang2/Files/spring25/SNURF-unique"  # Replace with the path to the input directory containing transcript files
output_dir = "/ocean/projects/bio200049p/zjiang2/Files/spring25/SNURF-longconserved"  # Replace with the path to the desired output directory

# Run the script
validate_and_copy(input_txt_file, input_dir, output_dir)
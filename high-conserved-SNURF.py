import os
import shutil

def validate_and_copy(input_txt_file, input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    with open(input_txt_file, 'r') as txt_file:
        lines = txt_file.readlines()
        for i in range(1, len(lines), 2):
            line = lines[i].strip()
            elements = line.split()

            total_percentage = float(elements[-1])
            transcript_name = elements[0]

            if total_percentage > 75:
                input_file_path = os.path.join(input_directory, transcript_name)
                if os.path.isfile(input_file_path):
                    shutil.copy(input_file_path, output_directory)
                else:
                    print(f"File not found: {input_file_path}")

# Define paths
input_txt_file = "/ocean/projects/bio200049p/zjiang2/Files/spring25/SNURFuniquedata.txt " 
input_dir = "/ocean/projects/bio200049p/zjiang2/Files/spring25/SNURF-unique"  # input directory containing transcript files
output_dir = "/ocean/projects/bio200049p/zjiang2/Files/spring25/SNURF-longconserved"  

# Run the script
validate_and_copy(input_txt_file, input_dir, output_dir)

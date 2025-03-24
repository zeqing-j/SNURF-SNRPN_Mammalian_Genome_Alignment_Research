import os

def remove_last_two_columns_and_combine(input_dir, output_file):
    # Reads all files in `input_dir`. For each line (with 6 columns), removes the last two columns and appends the resulting 4-column line into `output_file`.
    with open(output_file, "w") as out_f:
        for file_name in os.listdir(input_dir):
            file_path = os.path.join(input_dir, file_name)
            
            if os.path.isfile(file_path):
                with open(file_path, "r") as in_f:
                    for line in in_f:
                        # Split on whitespace
                        columns = line.split()
                        first_four = columns[:4]
                        new_line = " ".join(first_four) + "\n"
                        out_f.write(new_line)

if __name__ == "__main__":
    input_directory = "/ocean/projects/bio200049p/zjiang2/Files/spring24/5UTRbed" 
    output_file_path = "/ocean/projects/bio200049p/zjiang2/Files/spring25/extractphylopbed.bed"  

    remove_last_two_columns_and_combine(input_directory, output_file_path)

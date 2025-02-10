#!/usr/bin/env python3

import os

def remove_last_two_columns_and_combine(input_dir, output_file):
    """
    Reads all files in `input_dir`. For each line (with 6 columns),
    removes the last two columns and appends the resulting
    4-column line into `output_file`.
    """
    # Open the output file in write mode (overwrites previous content)
    with open(output_file, "w") as out_f:
        # List all items in the directory
        for file_name in os.listdir(input_dir):
            # Construct full path
            file_path = os.path.join(input_dir, file_name)
            
            # Only process if it's a file (not a directory, etc.)
            if os.path.isfile(file_path):
                # Open each file and process line by line
                with open(file_path, "r") as in_f:
                    for line in in_f:
                        # Split on whitespace
                        columns = line.split()
                        
                        # If the line doesn't have 6 columns, 
                        # you might want to handle or skip it. 
                        # We'll assume 6 for this example, 
                        # but we can add checks if needed.
                        
                        # Extract first 4 columns
                        first_four = columns[:4]
                        
                        # Join the first four columns back into a line
                        new_line = " ".join(first_four) + "\n"
                        
                        # Write to the combined output file
                        out_f.write(new_line)

if __name__ == "__main__":
    # Example usage:
    input_directory = "/ocean/projects/bio200049p/zjiang2/Files/spring24/5UTRbed"  # Update this to your directory path
    output_file_path = "/ocean/projects/bio200049p/zjiang2/Files/spring25/extractphylopbed.bed"     # Update if you prefer a different name

    remove_last_two_columns_and_combine(input_directory, output_file_path)
    print(f"Processed files from {input_directory} and created {output_file_path}")

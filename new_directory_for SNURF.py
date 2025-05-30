#give directory for SNURF sequences with highly conserved long uORF, but start/stop codons not checked yet
import os
import shutil

def extract_filenames(input_file):
    filenames = []
    with open(input_file, 'r') as f:
        lines = f.readlines()
        for i in range(0, len(lines), 3):
            filenames.append(lines[i].strip())
    return filenames

def copy_files(source_dir, dest_dir, filenames):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir) 

    for filename in filenames:
        source_file = os.path.join(source_dir, filename)
        dest_file = os.path.join(dest_dir, filename)

        if os.path.exists(source_file):
            shutil.copy(source_file, dest_file)  
            print(f"Copied: {source_file} to {dest_file}")
        else:
            print(f"File not found: {source_file}")

if __name__ == "__main__":
    # Input file containing filenames and uORF data
    input_file = "/ocean/projects/bio200049p/zjiang2/Files/spring25/conservedlongSNURF.txt" 

    source_dir = "/ocean/projects/bio200049p/zjiang2/Files/spring24/nodashfasta"

    destination_dir = "/ocean/projects/bio200049p/zjiang2/Files/spring24/SNURF-highconserve"

    filenames = extract_filenames(input_file)
    copy_files(source_dir, destination_dir, filenames)

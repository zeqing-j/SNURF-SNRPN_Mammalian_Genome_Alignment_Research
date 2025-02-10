import os
import subprocess
import csv

def process_bed_files(input_dir, output_dir, bigwig_file):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in os.listdir(input_dir):
        if filename.endswith(".bed"):
            input_file = os.path.join(input_dir, filename)
            
            with open(input_file, 'r') as bed_file:
                reader = csv.reader(bed_file, delimiter='\t')
                for row in reader:
                    if len(row) < 3:
                        continue  # Skip malformed lines
                    
                    chrom, start, end = row[0], row[1], row[2]
                    output_bedgraph = os.path.join(output_dir, f"{filename}.bedGraph")
                    
                    cmd = [
                        "bigWigToBedGraph", 
                        bigwig_file, 
                        output_bedgraph,
                        f"-chrom={chrom}",
                        f"-start={start}",
                        f"-end={end}"
                    ]
                    
                    try:
                        subprocess.run(cmd, check=True)
                        print(f"Processed: {chrom}:{start}-{end} from {filename}")
                    except subprocess.CalledProcessError as e:
                        print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    input_directory = "/ocean/projects/bio200049p/zjiang2/Files/spring24/5UTRbed"  # Change to the actual input directory
    output_directory = "/ocean/projects/bio200049p/zjiang2/Files/spring25/5UTRphylop470way"  # Change to the actual output directory
    bigwig_file = "/ocean/projects/bio200049p/zjiang2/Files/spring25/hg38.phyloP470way.bw"  # Path to the bigWig file
    
    process_bed_files(input_directory, output_directory, bigwig_file)
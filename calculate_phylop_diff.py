#to find the difference between first-second and third phylop score average
import sys

def process_phylop_scores(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        lines = infile.readlines()

        for i in range(0, len(lines), 2):
            transcript_name = lines[i].strip()
            phylop_scores = list(map(float, lines[i + 1].strip().split(",")))

            avg_first_second = []
            avg_third = []
            n = len(phylop_scores)

            for j in range(0, n, 3):
                if j + 1 < n:  
                    avg_first_second.append((phylop_scores[j] + phylop_scores[j + 1]) / 2)
                if j + 2 < n:  
                    avg_third.append(phylop_scores[j + 2])
                    
            avg_first_second_value = sum(avg_first_second) / len(avg_first_second) if avg_first_second else 0
            avg_third_value = sum(avg_third) / len(avg_third) if avg_third else 0

            difference = avg_first_second_value - avg_third_value

            outfile.write(transcript_name + "\n")
            outfile.write(f"{avg_first_second_value},{avg_third_value}\n")
            outfile.write(f"{difference}\n")

    input_file = "/ocean/projects/bio200049p/zjiang2/Files/RNAfold/combinedphylop.txt"
    output_file = "/ocean/projects/bio200049p/zjiang2/Files/spring25/phylopdiff.txt"

    process_phylop_scores(input_file, output_file)

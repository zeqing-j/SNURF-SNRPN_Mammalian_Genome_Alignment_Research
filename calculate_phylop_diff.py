#to find the difference between first-second and third phylop score average
import sys

def process_phylop_scores(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        lines = infile.readlines()

        for i in range(0, len(lines), 2):
            # Get transcript name and phylop scores
            transcript_name = lines[i].strip()
            phylop_scores = list(map(float, lines[i + 1].strip().split(",")))

            # Calculate averages for every first and second score, skipping the third
            avg_first_second = []
            avg_third = []
            n = len(phylop_scores)

            for j in range(0, n, 3):
                if j + 1 < n:  # Ensure there are at least two scores
                    avg_first_second.append((phylop_scores[j] + phylop_scores[j + 1]) / 2)
                if j + 2 < n:  # Ensure there is a third score
                    avg_third.append(phylop_scores[j + 2])

            # Final averages
            avg_first_second_value = sum(avg_first_second) / len(avg_first_second) if avg_first_second else 0
            avg_third_value = sum(avg_third) / len(avg_third) if avg_third else 0

            # Calculate the difference
            difference = avg_first_second_value - avg_third_value

            # Write to output file
            outfile.write(transcript_name + "\n")
            outfile.write(f"{avg_first_second_value},{avg_third_value}\n")
            outfile.write(f"{difference}\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file> <output_file>")
        sys.exit(1)

    input_file = "/ocean/projects/bio200049p/zjiang2/Files/RNAfold/combinedphylop.txt"
    output_file = "/ocean/projects/bio200049p/zjiang2/Files/spring25/phylopdiff.txt"

    process_phylop_scores(input_file, output_file)

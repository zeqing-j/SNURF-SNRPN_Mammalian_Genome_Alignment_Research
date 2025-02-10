#to validate if the info in unique_transcripts.txt are true
import os

def validate_uorf_distances(transcript_file, directory):
    with open(transcript_file, 'r') as f:
        lines = f.readlines()

    # Process transcript_file by groups of 3 lines
    invalid_transcripts = []
    for i in range(0, len(lines), 3):
        transcript_name = lines[i].strip()
        short_uorf = lines[i + 1].strip()
        long_uorf = lines[i + 2].strip()

        # Find the file corresponding to the transcript name
        transcript_path = os.path.join(directory, transcript_name)
        if not os.path.isfile(transcript_path):
            print(f"File not found for transcript: {transcript_name}")
            continue

        with open(transcript_path, 'r') as tf:
            transcript_lines = tf.readlines()

            if len(transcript_lines) < 2:
                print(f"Insufficient lines in file for transcript: {transcript_name}")
                continue

            sequence_line = transcript_lines[1].strip()

            # Find start indices of short and long uORFs
            short_start = sequence_line.find(short_uorf)
            long_start = sequence_line.find(long_uorf)

            if short_start == -1 or long_start == -1:
                print(f"uORFs not found in sequence for transcript: {transcript_name}")
                invalid_transcripts.append((transcript_name, short_uorf, long_uorf))
                continue

            # Calculate end index of short uORF
            short_end = short_start + len(short_uorf)

            # Validate the distance between short uORF and long uORF
            distance = long_start - short_end
            if distance < 0 or distance > 50:
                invalid_transcripts.append((transcript_name, short_uorf, long_uorf))

    # Print invalid transcripts
    if invalid_transcripts:
        print("Transcripts not satisfying the distance requirement:")
        for name, short, long in invalid_transcripts:
            print(name)
            print(short)
            print(long)

# Define paths
transcript_file = "/ocean/projects/bio200049p/zjiang2/Files/spring25/unique_transcripts.txt"  # Replace with the actual transcript file path
directory = "/ocean/projects/bio200049p/zjiang2/Files/spring24/nodashfasta"  # Replace with the directory containing the transcript files

# Run the script
validate_uorf_distances(transcript_file, directory)

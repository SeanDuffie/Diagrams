import os
import sys
from seqdiag.command import main as seqdiag_main

def generate_sequence_diagram(input_file, output_file):
    # Ensure the input file exists
    if not os.path.exists(input_file):
        print(f"Error: The file {input_file} does not exist.")
        return

    # Generate the diagram
    try:
        seqdiag_main(['-T', 'PNG', '-o', output_file, input_file])
        if os.path.exists(output_file):
            print(f"Sequence diagram generated successfully: {output_file}")
        else:
            print("Error: Failed to generate the sequence diagram.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    INPF = "seqdiag.txt"
    OUTF = "seqdiag.png"
    generate_sequence_diagram(INPF, OUTF)

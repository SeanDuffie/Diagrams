import os
import sys
from plantuml import PlantUML

def generate_sequence_diagram(input_file, output_file):
    # Ensure the input file exists
    if not os.path.exists(input_file):
        print(f"Error: The file {input_file} does not exist.")
        return

    # Create a PlantUML object with the server URL
    server = PlantUML(url='http://www.plantuml.com/plantuml/img/')

    # Read the PlantUML description from the input file
    with open(input_file, 'r') as file:
        plantuml_description = file.read()

    # Write the PlantUML description to a temporary file
    temp_file = 'temp.puml'
    with open(temp_file, 'w') as file:
        file.write(plantuml_description)

    # Generate the diagram
    server.processes_file(temp_file)

    # Rename the generated file to the desired output file name
    generated_file = temp_file.replace('.puml', '.png')
    if os.path.exists(generated_file):
        os.rename(generated_file, output_file)
        print(f"Sequence diagram generated successfully: {output_file}")
    else:
        print("Error: Failed to generate the sequence diagram.")

    # Clean up the temporary file
    os.remove(temp_file)

if __name__ == "__main__":
    INPF = "plantuml.txt"
    OUTF = "plantuml_diag.pmg"
    generate_sequence_diagram(INPF, OUTF)

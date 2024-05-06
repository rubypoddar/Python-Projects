from Bio import SeqIO
from Bio.Restriction import Restriction, Analysis
import matplotlib.pyplot as plt

def restriction_digest(sequence_file, enzyme_name):
    """
    Perform restriction enzyme digestion on a DNA sequence file.
    """
    # Read the sequence from file
    record = SeqIO.read(sequence_file, "fasta")
    sequence = record.seq

    # Get the restriction enzyme
    enzyme = getattr(Restriction, enzyme_name)

    # Perform restriction digestion
    analysis = Analysis(enzyme, sequence)

    return analysis

def visualize_digestion(analysis):
    """
    Visualize the results of restriction enzyme digestion.
    """
    # Plot the digestion map
    analysis.print_as_graph()
    plt.title('Restriction Enzyme Digestion Map')
    plt.xlabel('Base Pair Position')
    plt.ylabel('Fragment Size')
    plt.show()

if __name__ == "__main__":
    # Take input filename from user
    sequence_file = input("Enter the filename of the sequence in FASTA format: ")

    # Take input enzyme name from user
    enzyme_name = input("Enter the name of the restriction enzyme: ")

    try:
        # Perform restriction enzyme digestion
        digestion_analysis = restriction_digest(sequence_file, enzyme_name)

        # Visualize the digestion results
        visualize_digestion(digestion_analysis)
    except FileNotFoundError:
        print("File not found. Please make sure the file path is correct.")
    except Exception as e:
        print("An error occurred:", e)

from Bio.Seq import Seq
import matplotlib.pyplot as plt
import numpy as np

def translate_dna_to_protein(dna_sequence):
    """
    Translate a given DNA sequence into its corresponding protein sequence.
    """
    # Create a Seq object from the DNA sequence
    dna_seq = Seq(dna_sequence)
    # Translate DNA to protein sequence
    protein_seq = dna_seq.translate()
    return protein_seq

def analyze_protein_sequence(protein_sequence):
    """
    Analyze the given protein sequence and visualize basic statistics.
    """
    # Calculate amino acid frequencies
    amino_acids = list("ACDEFGHIKLMNPQRSTVWY")
    amino_acid_counts = {aa: protein_sequence.count(aa) for aa in amino_acids}
    # Sort amino acids by frequency
    sorted_amino_acids = sorted(amino_acid_counts.items(), key=lambda x: x[1], reverse=True)
    amino_acids, counts = zip(*sorted_amino_acids)
    
    # Plot amino acid frequencies
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(amino_acids)), counts, tick_label=amino_acids, color='skyblue')
    plt.title('Amino Acid Frequencies')
    plt.xlabel('Amino Acid')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Example DNA sequence
    dna_sequence = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"

    # Translate DNA to protein sequence
    protein_sequence = translate_dna_to_protein(dna_sequence)
    print("Translated Protein Sequence:", protein_sequence)

    # Analyze and visualize protein sequence
    analyze_protein_sequence(protein_sequence)

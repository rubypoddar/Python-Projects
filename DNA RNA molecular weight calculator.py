import pandas as pd
import numpy as np

def calculate_molecular_weight(sequence, is_rna=False):
    """
    Calculate the molecular weight of a DNA or RNA sequence.

    Arguments:
    sequence: str, the DNA or RNA sequence
    is_rna: bool, whether the sequence is RNA (default is False for DNA)

    Returns:
    float, the molecular weight of the sequence
    """
    # Define the molecular weights of individual nucleotides
    nucleotide_weights = {
        'A': {'C': 10, 'H': 9, 'N': 5, 'O': 5},
        'T': {'C': 10, 'H': 12, 'N': 2, 'O': 7},
        'G': {'C': 10, 'H': 9, 'N': 5, 'O': 5},
        'C': {'C': 9, 'H': 9, 'N': 3, 'O': 6},
        'U': {'C': 9, 'H': 9, 'N': 3, 'O': 7}  # RNA only
    }

    # Initialize total molecular weight
    total_weight = {'C': 0, 'H': 0, 'N': 0, 'O': 0}

    # Calculate the total molecular weight
    for nucleotide in sequence.upper():
        for element, weight in nucleotide_weights[nucleotide].items():
            total_weight[element] += weight

    # Adjust for RNA if necessary
    if is_rna:
        total_weight['O'] -= 1  # Remove one oxygen atom due to uracil replacing thymine

    # Calculate molecular weight using the formula: MW = sum(ni * Mi)
    atomic_weights = {'C': 12.01, 'H': 1.01, 'N': 14.01, 'O': 16.00}
    molecular_weight = sum(total_weight[element] * atomic_weights[element] for element in total_weight)

    return molecular_weight

# Test the function
sequence = input("Enter DNA/RNA sequence: ")
is_rna = input("Is it RNA? (y/n): ").strip().lower() == 'y'
molecular_weight = calculate_molecular_weight(sequence, is_rna=is_rna)
print("Molecular Weight:", molecular_weight, "g/mol")

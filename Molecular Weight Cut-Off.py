import pandas as pd

def calculate_molecular_weight(amino_acid_sequence, aa_weights):
    """
    Calculate the molecular weight of a protein based on its amino acid sequence.
    """
    molecular_weight = sum(aa_weights[aa] for aa in amino_acid_sequence)
    return molecular_weight

def check_retention(molecular_weight, mwco_threshold):
    """
    Check if the protein would be retained based on the provided MWCO threshold.
    """
    if molecular_weight <= mwco_threshold:
        return "Retained"
    else:
        return "Pass Through"

if __name__ == "__main__":
    # Define amino acid weights (in Da)
    aa_weights = {
        'A': 71.07, 'R': 156.18, 'N': 114.08, 'D': 115.08, 'C': 103.10,
        'E': 129.12, 'Q': 128.13, 'G': 57.05, 'H': 137.14, 'I': 113.15,
        'L': 113.15, 'K': 128.17, 'M': 131.19, 'F': 147.18, 'P': 97.11,
        'S': 87.07, 'T': 101.10, 'W': 186.21, 'Y': 163.18, 'V': 99.13
    }

    # Take input for the amino acid sequence and MWCO threshold
    amino_acid_sequence = input("Enter the amino acid sequence of the protein: ").upper()
    mwco_threshold = float(input("Enter the Molecular Weight Cut-Off (MWCO) threshold (in Da): "))

    # Calculate the molecular weight of the protein
    molecular_weight = calculate_molecular_weight(amino_acid_sequence, aa_weights)

    # Check if the protein would be retained based on the MWCO threshold
    retention_status = check_retention(molecular_weight, mwco_threshold)

    # Output the result
    print(f"Molecular Weight of Protein: {molecular_weight} Da")
    print(f"Retention Status: {retention_status}")

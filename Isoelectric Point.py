from Bio.SeqUtils.ProtParam import ProteinAnalysis
import pandas as pd

def calculate_isoelectric_point(sequence):
    """
    Calculate the isoelectric point (pI) of a protein sequence.
    """
    protein_analyzer = ProteinAnalysis(sequence)
    pI = protein_analyzer.isoelectric_point()
    return pI

if __name__ == "__main__":
    # Take input for the protein sequence
    sequence = input("Enter the protein sequence: ")

    # Calculate the isoelectric point (pI)
    pI = calculate_isoelectric_point(sequence)
    
    # Create a DataFrame for output formatting
    df_output = pd.DataFrame({
        'Parameter': ['Protein Sequence', 'Isoelectric Point (pI)'],
        'Value': [sequence, pI]
    })

    # Output the result
    print("Protein Isoelectric Point (pI):")
    print(df_output)

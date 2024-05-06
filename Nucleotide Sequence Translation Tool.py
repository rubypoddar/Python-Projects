from Bio.Seq import Seq

def translate_sequence(dna_sequence):
    """
    Translate a DNA sequence into its corresponding protein sequence.

    Arguments:
    dna_sequence: str, the DNA sequence to be translated

    Returns:
    str, the translated protein sequence
    """
    seq = Seq(dna_sequence)
    protein_sequence = seq.translate()
    return str(protein_sequence)

# Test the translation tool
dna_sequence = input("Enter DNA sequence: ")
protein_sequence = translate_sequence(dna_sequence)
print("Translated Protein Sequence:", protein_sequence)

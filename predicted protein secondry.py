from Bio.Seq import Seq
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import matplotlib.pyplot as plt

def predict_secondary_structure(protein_sequence):
    # Calculate protein features (amino acid composition)
    protein_analysis = ProteinAnalysis(protein_sequence)
    aa_composition = protein_analysis.get_amino_acids_percent()
    
    # Predict secondary structure based on amino acid composition
    predicted_secondary_structure = []
    for aa in protein_sequence:
        if aa in "ARNDCQEGHILKMFPSTWYV":
            if aa_composition['A'] + aa_composition['G'] + aa_composition['V'] > 0.5:
                predicted_secondary_structure.append('C')  # Coil
            elif aa_composition['E'] + aa_composition['Q'] > 0.15:
                predicted_secondary_structure.append('E')  # Strand
            else:
                predicted_secondary_structure.append('H')  # Helix
        else:
            predicted_secondary_structure.append('C')  # Coil (for non-standard amino acids)
    
    return predicted_secondary_structure

def plot_secondary_structure(protein_sequence, predicted_secondary_structure):
    # Define colors for different secondary structure elements
    colors = {'H': 'red', 'E': 'blue', 'C': 'gray'}
    
    # Create a bar plot to visualize the predicted secondary structure
    plt.figure(figsize=(14, 4))
    for i, ss in enumerate(predicted_secondary_structure):
        plt.bar(i, 1, color=colors[ss], edgecolor='black')
    
    # Set plot properties
    plt.xlabel('Amino Acid Position')
    plt.ylabel('Secondary Structure')
    plt.title('Predicted Protein Secondary Structure')
    plt.xticks(range(len(protein_sequence)), protein_sequence, rotation='vertical')
    plt.yticks([])
    plt.ylim(0, 1.2)
    plt.xlim(-0.5, len(protein_sequence) - 0.5)
    
    # Create legend
    legend_elements = [plt.Line2D([0], [0], color=colors[ss], label=ss) for ss in colors]
    plt.legend(handles=legend_elements, loc='upper right')
    
    plt.tight_layout()
    plt.show()

# Example usage
protein_sequence = "MTEITAAMVKELRESTGAGMMDCKNALSETNGDFDKAVQLLREKGLGKAAKKADRLAAEG"
secondary_structure = predict_secondary_structure(protein_sequence)
plot_secondary_structure(protein_sequence, secondary_structure)

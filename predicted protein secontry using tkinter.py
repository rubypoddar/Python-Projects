from Bio.Seq import Seq
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

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

def get_protein_sequence():
    protein_sequence = entry_sequence.get().strip()
    secondary_structure = predict_secondary_structure(protein_sequence)
    plot_secondary_structure(protein_sequence, secondary_structure)

# Create main window
root = tk.Tk()
root.title("Protein Secondary Structure Prediction")

# Create label and entry field
label_sequence = ttk.Label(root, text="Protein Sequence:")
label_sequence.grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_sequence = ttk.Entry(root, width=50)
entry_sequence.grid(row=0, column=1, padx=5, pady=5)

# Create predict button
button_predict = ttk.Button(root, text="Predict Secondary Structure", command=get_protein_sequence)
button_predict.grid(row=1, columnspan=2, padx=5, pady=10)

# Start the GUI event loop
root.mainloop()

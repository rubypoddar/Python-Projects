import tkinter as tk
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# A dictionary containing the pI values of amino acids
amino_acid_pI = {
    "G": 6.01, "A": 6.11, "V": 6.02, "L": 6.04, "I": 6.00,
    "P": 6.30, "F": 5.91, "W": 5.88, "M": 5.74, "H": 7.60,
    "K": 9.74, "Q": 5.65, "E": 3.22, "S": 5.68, "T": 5.60,
    "C": 5.07, "Y": 5.66, "N": 5.41, "D": 2.77, "R": 10.76
}

def calculate_pI(sequence):
    pI_values = [amino_acid_pI[aa] for aa in sequence]
    return sum(pI_values) / len(pI_values)

def on_calculate():
    sequence = sequence_entry.get().upper()
    if all(aa in amino_acid_pI for aa in sequence):
        pI = calculate_pI(sequence)
        result_label.config(text=f"Theoretical pI: {pI:.2f}")

        # Plot 3D scatter plot of amino acids and their pI values
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        amino_acids = list(amino_acid_pI.keys())
        pI_values = [amino_acid_pI[aa] for aa in amino_acids]
        ax.scatter(range(len(amino_acids)), pI_values, [0]*len(amino_acids), c='r', marker='o')
        ax.set_xticks(range(len(amino_acids)))
        ax.set_xticklabels(amino_acids)
        ax.set_xlabel('Amino Acid')
        ax.set_ylabel('pI Value')
        ax.set_zlabel('Z')
        ax.set_title('Amino Acid pI Values')
        plt.show()
    else:
        result_label.config(text="Invalid sequence! Only standard amino acids allowed.")

# Create tkinter window
root = tk.Tk()
root.title("Isoelectric Focusing Calculator")

# Labels and entries
tk.Label(root, text="Amino Acid Sequence:").grid(row=0, column=0)
sequence_entry = tk.Entry(root)
sequence_entry.grid(row=0, column=1)

# Button to calculate pI
calculate_button = tk.Button(root, text="Calculate pI", command=on_calculate)
calculate_button.grid(row=1, columnspan=2)

# Label to display result
result_label = tk.Label(root, text="")
result_label.grid(row=2, columnspan=2)

root.mainloop()

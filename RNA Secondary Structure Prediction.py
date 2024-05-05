import tkinter as tk
from tkinter import ttk
from Bio.Seq import Seq
from Bio.SeqUtils import MeltingTemp
import subprocess

def predict_secondary_structure():
    # Get input sequence from entry field
    sequence = entry_sequence.get().strip()
    
    # Create a Seq object
    seq = Seq(sequence)
    
    # Use Biopython's MeltingTemp function to calculate melting temperature
    melting_temp = MeltingTemp.Tm_GC(seq)
    label_melting_temp.config(text=f"Melting Temperature: {melting_temp} °C")
    
    # Write sequence to a temporary file
    with open("temp.fasta", "w") as temp_file:
        temp_file.write(f">Sequence\n{sequence}\n")
    
    # Use RNAfold to predict secondary structure
    process = subprocess.Popen(['RNAfold', '-p'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    stdout, stderr = process.communicate(f"< temp.fasta")
    
    # Extract secondary structure from RNAfold output
    secondary_structure = stdout.split('\n')[1]
    label_secondary_structure.config(text=f"Secondary Structure: {secondary_structure}")

# Create main window
root = tk.Tk()
root.title("RNA Secondary Structure Prediction Tool")

# Create labels and entry field
label_sequence = ttk.Label(root, text="RNA Sequence:")
label_sequence.grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_sequence = ttk.Entry(root, width=50)
entry_sequence.grid(row=0, column=1, padx=5, pady=5)

# Create predict button
button_predict = ttk.Button(root, text="Predict Secondary Structure", command=predict_secondary_structure)
button_predict.grid(row=1, columnspan=2, padx=5, pady=10)

# Create melting temperature label
label_melting_temp = ttk.Label(root, text="")
label_melting_temp.grid(row=2, columnspan=2, padx=5, pady=5)

# Create secondary structure label
label_secondary_structure = ttk.Label(root, text="")
label_secondary_structure.grid(row=3, columnspan=2, padx=5, pady=5)

# Start the GUI event loop
root.mainloop()

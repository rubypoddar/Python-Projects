import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

def calculate_codon_usage(sequence):
    """
    Calculate codon usage for a given nucleotide sequence.

    Parameters:
    - sequence: Nucleotide sequence (DNA or RNA)

    Returns:
    - codon_usage: Dictionary containing codon frequencies
    """
    codons = [sequence[i:i+3] for i in range(0, len(sequence) - 2, 3)]
    codon_usage = dict(Counter(codons))
    total_codons = sum(codon_usage.values())
    
    for codon, count in codon_usage.items():
        codon_usage[codon] = count / total_codons

    return codon_usage

def plot_codon_usage(codon_usage):
    """
    Plot the codon usage frequencies.

    Parameters:
    - codon_usage: Dictionary containing codon frequencies
    """
    codons = list(codon_usage.keys())
    frequencies = list(codon_usage.values())

    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(x=codons, y=frequencies, hue=codons, palette="viridis", dodge=False, legend=False)
    ax.set(xlabel='Codons', ylabel='Frequency', title='Codon Usage')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    plt.tight_layout()

    return plt


def analyze_sequence():
    sequence = sequence_entry.get()

    if not sequence:
        messagebox.showwarning("Warning", "Please enter a nucleotide sequence.")
        return

    codon_usage = calculate_codon_usage(sequence)
    plt = plot_codon_usage(codon_usage)

    plt.show()

# Create GUI window
window = tk.Tk()
window.title("Nucleotide Codon Usage Calculator")

# Add sequence input field
sequence_label = tk.Label(window, text="Enter Nucleotide Sequence:")
sequence_label.pack()

sequence_entry = tk.Entry(window, width=50)
sequence_entry.pack()

# Add analyze button
analyze_button = tk.Button(window, text="Analyze Sequence", command=analyze_sequence)
analyze_button.pack()

# Run the GUI
window.mainloop()

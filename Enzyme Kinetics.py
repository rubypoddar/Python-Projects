import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

def michaelis_menten(substrate_concentration, vmax, km):
    """
    Calculate reaction rate using the Michaelis-Menten equation.

    Parameters:
    - substrate_concentration: Array of substrate concentrations
    - vmax: Maximum reaction rate
    - km: Michaelis constant

    Returns:
    - reaction_rate: Array of reaction rates
    """
    reaction_rate = (vmax * substrate_concentration) / (km + substrate_concentration)
    return reaction_rate

def plot_enzyme_kinetics(substrate_concentration, reaction_rate):
    """
    Plot the enzyme kinetics curve.

    Parameters:
    - substrate_concentration: Array of substrate concentrations
    - reaction_rate: Array of reaction rates
    """
    plt.figure(figsize=(8, 6))
    plt.plot(substrate_concentration, reaction_rate, marker='o', linestyle='-')
    plt.xlabel('Substrate Concentration')
    plt.ylabel('Reaction Rate')
    plt.title('Enzyme Kinetics (Michaelis-Menten)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def analyze_enzyme_kinetics():
    try:
        substrate_concentration = np.array([float(x) for x in substrate_entry.get().split(',')])
        vmax = float(vmax_entry.get())
        km = float(km_entry.get())

        reaction_rate = michaelis_menten(substrate_concentration, vmax, km)
        plot_enzyme_kinetics(substrate_concentration, reaction_rate)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numeric values.")

# Create GUI window
window = tk.Tk()
window.title("Enzyme Kinetics Calculator")

# Add substrate concentration input field
substrate_label = tk.Label(window, text="Enter Substrate Concentrations (comma-separated):")
substrate_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

substrate_entry = tk.Entry(window, width=50)
substrate_entry.grid(row=0, column=1, padx=10, pady=5)

# Add vmax input field
vmax_label = tk.Label(window, text="Enter Maximum Reaction Rate (vmax):")
vmax_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

vmax_entry = tk.Entry(window)
vmax_entry.grid(row=1, column=1, padx=10, pady=5)

# Add km input field
km_label = tk.Label(window, text="Enter Michaelis Constant (km):")
km_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

km_entry = tk.Entry(window)
km_entry.grid(row=2, column=1, padx=10, pady=5)

# Add analyze button
analyze_button = tk.Button(window, text="Analyze", command=analyze_enzyme_kinetics)
analyze_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# Run the GUI
window.mainloop()

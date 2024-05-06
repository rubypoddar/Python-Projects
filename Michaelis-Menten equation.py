import numpy as np
import tkinter as tk
from tkinter import messagebox

def michaelis_menten(substrate_concentration, vmax, km):
    """
    Calculate reaction rate using the Michaelis-Menten equation.

    Parameters:
    - substrate_concentration: Substrate concentration
    - vmax: Maximum reaction rate
    - km: Michaelis constant

    Returns:
    - reaction_rate: Reaction rate
    """
    reaction_rate = (vmax * substrate_concentration) / (km + substrate_concentration)
    return reaction_rate

def calculate_reaction_rate():
    try:
        substrate_concentration = float(substrate_entry.get())
        vmax = float(vmax_entry.get())
        km = float(km_entry.get())

        reaction_rate = michaelis_menten(substrate_concentration, vmax, km)
        result_label.config(text=f"Reaction rate: {reaction_rate}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numeric values.")

# Create GUI window
window = tk.Tk()
window.title("Michaelis-Menten Equation Solver")

# Add substrate concentration input field
substrate_label = tk.Label(window, text="Substrate Concentration:")
substrate_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

substrate_entry = tk.Entry(window)
substrate_entry.grid(row=0, column=1, padx=10, pady=5)

# Add vmax input field
vmax_label = tk.Label(window, text="Maximum Reaction Rate (vmax):")
vmax_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

vmax_entry = tk.Entry(window)
vmax_entry.grid(row=1, column=1, padx=10, pady=5)

# Add km input field
km_label = tk.Label(window, text="Michaelis Constant (Km):")
km_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

km_entry = tk.Entry(window)
km_entry.grid(row=2, column=1, padx=10, pady=5)

# Add calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate_reaction_rate)
calculate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# Add result label
result_label = tk.Label(window, text="")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# Run the GUI
window.mainloop()

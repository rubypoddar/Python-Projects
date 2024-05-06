import numpy as np

def henderson_hasselbalch(pKa, acid_concentration, base_concentration):
    """
    Calculate the pH of a buffer solution using the Henderson-Hasselbalch equation.

    Parameters:
    - pKa: The dissociation constant of the weak acid
    - acid_concentration: Concentration of the weak acid (in moles per liter)
    - base_concentration: Concentration of the conjugate base (in moles per liter)

    Returns:
    - pH: The pH of the buffer solution
    """
    pH = pKa + np.log10(base_concentration / acid_concentration)
    return pH

def calculate_pH():
    try:
        pKa = float(pKa_entry.get())
        acid_concentration = float(acid_conc_entry.get())
        base_concentration = float(base_conc_entry.get())

        pH = henderson_hasselbalch(pKa, acid_concentration, base_concentration)
        result_label.config(text=f"pH of the buffer solution: {pH:.2f}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter numeric values.")

# Create GUI window
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Henderson-Hasselbalch Equation Calculator")

# Add pKa input field
pKa_label = ttk.Label(window, text="pKa:")
pKa_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

pKa_entry = ttk.Entry(window)
pKa_entry.grid(row=0, column=1, padx=10, pady=5)

# Add acid concentration input field
acid_conc_label = ttk.Label(window, text="Acid Concentration (M):")
acid_conc_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

acid_conc_entry = ttk.Entry(window)
acid_conc_entry.grid(row=1, column=1, padx=10, pady=5)

# Add base concentration input field
base_conc_label = ttk.Label(window, text="Base Concentration (M):")
base_conc_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

base_conc_entry = ttk.Entry(window)
base_conc_entry.grid(row=2, column=1, padx=10, pady=5)

# Add calculate button
calculate_button = ttk.Button(window, text="Calculate pH", command=calculate_pH)
calculate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# Add result label
result_label = ttk.Label(window, text="")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# Run the GUI
window.mainloop()

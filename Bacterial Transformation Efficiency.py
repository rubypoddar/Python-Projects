import tkinter as tk
from tkinter import ttk

def calculate_transformation_efficiency():
    transformed_colonies = int(entry_colonies.get())
    dna_volume = float(entry_dna_volume.get())
    cells_volume = float(entry_cells_volume.get())

    transformation_efficiency = transformed_colonies / (dna_volume * cells_volume)
    label_result.config(text=f"Transformation Efficiency: {transformation_efficiency:.2f} CFU/µg")

# Create main window
root = tk.Tk()
root.title("Bacterial Transformation Efficiency Calculator")

# Create labels and entry fields
label_colonies = ttk.Label(root, text="Transformed Colonies:")
label_colonies.grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_colonies = ttk.Entry(root)
entry_colonies.grid(row=0, column=1, padx=5, pady=5)

label_dna_volume = ttk.Label(root, text="DNA Volume (µg):")
label_dna_volume.grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_dna_volume = ttk.Entry(root)
entry_dna_volume.grid(row=1, column=1, padx=5, pady=5)

label_cells_volume = ttk.Label(root, text="Competent Cells Volume (µL):")
label_cells_volume.grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_cells_volume = ttk.Entry(root)
entry_cells_volume.grid(row=2, column=1, padx=5, pady=5)

# Create calculate button
button_calculate = ttk.Button(root, text="Calculate", command=calculate_transformation_efficiency)
button_calculate.grid(row=3, columnspan=2, padx=5, pady=10)

# Create result label
label_result = ttk.Label(root, text="")
label_result.grid(row=4, columnspan=2, padx=5, pady=5)

# Start the GUI event loop
root.mainloop()

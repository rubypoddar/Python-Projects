import tkinter as tk
from tkinter import ttk

def calculate_extraction_yield():
    elution_buffer_volume = float(entry_elution_buffer.get())
    dna_concentration = float(entry_concentration.get())
    eluate_volume = float(entry_eluate_volume.get())

    extraction_yield = elution_buffer_volume * dna_concentration * eluate_volume
    label_result.config(text=f"Extraction yield: {extraction_yield} ng")

# Create main window
root = tk.Tk()
root.title("Gel Extraction Yield Calculator")

# Create labels and entry fields
label_elution_buffer = ttk.Label(root, text="Elution Buffer Volume (µL):")
label_elution_buffer.grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_elution_buffer = ttk.Entry(root)
entry_elution_buffer.grid(row=0, column=1, padx=5, pady=5)

label_concentration = ttk.Label(root, text="DNA Concentration (ng/µL):")
label_concentration.grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_concentration = ttk.Entry(root)
entry_concentration.grid(row=1, column=1, padx=5, pady=5)

label_eluate_volume = ttk.Label(root, text="Eluate Volume (µL):")
label_eluate_volume.grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_eluate_volume = ttk.Entry(root)
entry_eluate_volume.grid(row=2, column=1, padx=5, pady=5)

# Create calculate button
button_calculate = ttk.Button(root, text="Calculate", command=calculate_extraction_yield)
button_calculate.grid(row=3, columnspan=2, padx=5, pady=10)

# Create result label
label_result = ttk.Label(root, text="")
label_result.grid(row=4, columnspan=2, padx=5, pady=5)

# Start the GUI event loop
root.mainloop()

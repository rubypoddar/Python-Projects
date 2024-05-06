import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np

def calculate_qpcr_efficiency():
    slope = float(entry_slope.get())
    efficiency = (10 ** (-1 / slope) - 1) * 100
    label_result.config(text=f"qPCR Efficiency: {efficiency:.2f}%")
    
    # Generate standard curve plot
    concentrations = np.array([1, 10, 100, 1000, 10000])  # Template DNA concentrations
    ct_values = slope * np.log10(concentrations) + 20  # Arbitrary intercept value for demonstration
    
    plt.figure()
    plt.plot(np.log10(concentrations), ct_values, marker='o')
    plt.xlabel('Log DNA Concentration')
    plt.ylabel('Cycle Threshold (Ct)')
    plt.title('Standard Curve')
    plt.grid(True)
    plt.show()

# Create main window
root = tk.Tk()
root.title("qPCR Efficiency Calculator")

# Create labels and entry fields
label_slope = ttk.Label(root, text="Slope of Standard Curve:")
label_slope.grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_slope = ttk.Entry(root)
entry_slope.grid(row=0, column=1, padx=5, pady=5)

# Create calculate button
button_calculate = ttk.Button(root, text="Calculate", command=calculate_qpcr_efficiency)
button_calculate.grid(row=1, columnspan=2, padx=5, pady=10)

# Create result label
label_result = ttk.Label(root, text="")
label_result.grid(row=2, columnspan=2, padx=5, pady=5)

# Start the GUI event loop
root.mainloop()

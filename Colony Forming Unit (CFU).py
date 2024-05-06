import tkinter as tk

def calculate_cfu():
    try:
        dilution_factor = float(dilution_factor_entry.get())
        volume_plated = float(volume_plated_entry.get())
        colonies_counted = float(colonies_counted_entry.get())
        
        cfu_per_ml = colonies_counted / (dilution_factor * volume_plated)
        result_label.config(text=f"CFU/mL: {cfu_per_ml:.2f}")
    except ValueError:
        result_label.config(text="Invalid input! Please enter numbers.")

# Create tkinter window
root = tk.Tk()
root.title("Colony Forming Unit (CFU) Calculator")

# Labels and entries
tk.Label(root, text="Dilution Factor:").grid(row=0, column=0)
dilution_factor_entry = tk.Entry(root)
dilution_factor_entry.grid(row=0, column=1)

tk.Label(root, text="Volume Plated (mL):").grid(row=1, column=0)
volume_plated_entry = tk.Entry(root)
volume_plated_entry.grid(row=1, column=1)

tk.Label(root, text="Colonies Counted:").grid(row=2, column=0)
colonies_counted_entry = tk.Entry(root)
colonies_counted_entry.grid(row=2, column=1)

# Button to calculate CFU
calculate_button = tk.Button(root, text="Calculate CFU/mL", command=calculate_cfu)
calculate_button.grid(row=3, columnspan=2)

# Label to display result
result_label = tk.Label(root, text="")
result_label.grid(row=4, columnspan=2)

root.mainloop()

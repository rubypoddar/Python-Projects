import tkinter as tk

def calculate_enzyme_activity():
    try:
        substrate_concentration = float(substrate_entry.get())
        enzyme_concentration = float(enzyme_entry.get())
        reaction_time = float(time_entry.get())
        
        enzyme_activity = substrate_concentration / reaction_time / enzyme_concentration
        result_label.config(text=f"Enzyme Activity: {enzyme_activity:.2f}")
    except ValueError:
        result_label.config(text="Invalid input! Please enter numbers.")

# Create tkinter window
root = tk.Tk()
root.title("Enzyme Activity Calculator")

# Labels and entries
tk.Label(root, text="Substrate Concentration:").grid(row=0, column=0)
substrate_entry = tk.Entry(root)
substrate_entry.grid(row=0, column=1)

tk.Label(root, text="Enzyme Concentration:").grid(row=1, column=0)
enzyme_entry = tk.Entry(root)
enzyme_entry.grid(row=1, column=1)

tk.Label(root, text="Reaction Time:").grid(row=2, column=0)
time_entry = tk.Entry(root)
time_entry.grid(row=2, column=1)

# Button to calculate enzyme activity
calculate_button = tk.Button(root, text="Calculate", command=calculate_enzyme_activity)
calculate_button.grid(row=3, columnspan=2)

# Label to display result
result_label = tk.Label(root, text="")
result_label.grid(row=4, columnspan=2)

root.mainloop()

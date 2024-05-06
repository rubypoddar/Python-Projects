import tkinter as tk

def calculate_transfection_efficiency():
    try:
        cells_transfected = float(cells_transfected_entry.get())
        total_cells = float(total_cells_entry.get())
        
        # Calculate transfection efficiency
        transfection_efficiency = (cells_transfected / total_cells) * 100
        
        result_label.config(text=f"Transfection Efficiency: {transfection_efficiency:.2f}%")
    except ValueError:
        result_label.config(text="Invalid input! Please enter numbers.")

# Create tkinter window
root = tk.Tk()
root.title("Transfection Efficiency Calculator")

# Labels and entries
tk.Label(root, text="Number of Transfected Cells:").grid(row=0, column=0)
cells_transfected_entry = tk.Entry(root)
cells_transfected_entry.grid(row=0, column=1)

tk.Label(root, text="Total Number of Cells:").grid(row=1, column=0)
total_cells_entry = tk.Entry(root)
total_cells_entry.grid(row=1, column=1)

# Button to calculate transfection efficiency
calculate_button = tk.Button(root, text="Calculate Transfection Efficiency", command=calculate_transfection_efficiency)
calculate_button.grid(row=2, columnspan=2)

# Label to display result
result_label = tk.Label(root, text="")
result_label.grid(row=3, columnspan=2)

root.mainloop()

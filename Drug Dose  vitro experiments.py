import tkinter as tk

def calculate_drug_dose():
    try:
        stock_concentration = float(stock_concentration_entry.get())
        final_concentration = float(final_concentration_entry.get())
        final_volume = float(final_volume_entry.get())
        
        # Calculate the required volume of stock solution needed
        stock_volume = (final_concentration * final_volume) / stock_concentration
        
        result_label.config(text=f"Volume of Stock Solution Needed (mL): {stock_volume:.2f} mL")
    except ValueError:
        result_label.config(text="Invalid input! Please enter numbers.")

# Create tkinter window
root = tk.Tk()
root.title("Drug Dose Calculator (for in vitro experiments)")

# Labels and entries
tk.Label(root, text="Stock Concentration (mg/mL):").grid(row=0, column=0)
stock_concentration_entry = tk.Entry(root)
stock_concentration_entry.grid(row=0, column=1)

tk.Label(root, text="Final Concentration (mg/mL):").grid(row=1, column=0)
final_concentration_entry = tk.Entry(root)
final_concentration_entry.grid(row=1, column=1)

tk.Label(root, text="Final Volume (mL):").grid(row=2, column=0)
final_volume_entry = tk.Entry(root)
final_volume_entry.grid(row=2, column=1)

# Button to calculate drug dose
calculate_button = tk.Button(root, text="Calculate Drug Dose", command=calculate_drug_dose)
calculate_button.grid(row=3, columnspan=2)

# Label to display result
result_label = tk.Label(root, text="")
result_label.grid(row=4, columnspan=2)

root.mainloop()

import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt

def calculate_antibody_dilution():
    try:
        stock_concentration = float(stock_concentration_entry.get())
        final_concentration = float(final_concentration_entry.get())
        final_volume = float(final_volume_entry.get())
        
        # Calculate the dilution factor
        dilution_factor = stock_concentration / final_concentration
        
        # Calculate the volume of stock solution needed
        stock_volume = final_volume * dilution_factor
        
        result_label.config(text=f"Dilution Factor: {dilution_factor:.2f}\n"
                                  f"Volume of Stock Solution Needed (mL): {stock_volume:.2f}")
        
        # Create a DataFrame to store the results
        df = pd.DataFrame({'Dilution Factor': [dilution_factor], 'Volume of Stock Solution Needed (mL)': [stock_volume]})
        
        # Plot the results
        plt.figure(figsize=(6, 4))
        df.plot(kind='bar', ax=plt.gca())
        plt.title('Antibody Dilution Results')
        plt.xlabel('Parameters')
        plt.ylabel('Value')
        plt.xticks(rotation=0)
        plt.tight_layout()
        plt.show()
        
    except ValueError:
        result_label.config(text="Invalid input! Please enter numbers.")

# Create tkinter window
root = tk.Tk()
root.title("Antibody Dilution Calculator")

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

# Button to calculate dilution
calculate_button = tk.Button(root, text="Calculate Dilution", command=calculate_antibody_dilution)
calculate_button.grid(row=3, columnspan=2)

# Label to display result
result_label = tk.Label(root, text="")
result_label.grid(row=4, columnspan=2)

root.mainloop()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def calculate_copy_number(rna_per_cell, num_cells):
    """
    Calculate the total RNA copy number based on the number of RNA molecules per cell and the number of cells.
    """
    total_rna_copy_number = rna_per_cell * num_cells
    return total_rna_copy_number

def plot_copy_number_vs_cells(rna_per_cell, max_num_cells):
    """
    Plot the total RNA copy number as a function of the number of cells.
    """
    num_cells = np.arange(1, max_num_cells + 1)
    total_rna_copy_numbers = calculate_copy_number(rna_per_cell, num_cells)

    plt.figure(figsize=(8, 6))
    plt.plot(num_cells, total_rna_copy_numbers, marker='o', linestyle='-')
    plt.title('Total RNA Copy Number vs. Number of Cells')
    plt.xlabel('Number of Cells')
    plt.ylabel('Total RNA Copy Number')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # Take input for the number of RNA molecules per cell
    rna_per_cell = float(input("Enter the number of RNA molecules per cell: "))
    # Set the maximum number of cells for plotting
    max_num_cells = int(input("Enter the maximum number of cells for plotting: "))

    # Plot the total RNA copy number as a function of the number of cells
    plot_copy_number_vs_cells(rna_per_cell, max_num_cells)

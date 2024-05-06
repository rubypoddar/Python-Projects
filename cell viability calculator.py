import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def calculate_cell_viability(total_cells, dead_cells):
    """
    Calculate the percentage of viable cells in a cell culture.
    Args:
    - total_cells: Total number of cells counted.
    - dead_cells: Number of non-viable (dead) cells counted.
    Returns:
    - viability_percentage: Percentage of viable cells.
    """
    viability_percentage = ((total_cells - dead_cells) / total_cells) * 100
    return viability_percentage

def main():
    print("Welcome to the Cell Viability Calculator!")
    print("This calculator estimates the percentage of viable cells in a cell culture.")

    try:
        # Input total number of cells
        total_cells = int(input("Enter the total number of cells counted: "))

        # Input number of dead cells
        dead_cells = int(input("Enter the number of non-viable (dead) cells counted: "))

        # Calculate cell viability
        viability_percentage = calculate_cell_viability(total_cells, dead_cells)

        # Output cell viability
        print("\nEstimated Cell Viability: {:.2f}%".format(viability_percentage))

        # Create a bar plot to visualize cell viability
        data = {'Cell Status': ['Viable', 'Non-viable'],
                'Count': [total_cells - dead_cells, dead_cells]}
        df = pd.DataFrame(data)
        plt.figure(figsize=(8, 6))
        plt.bar(df['Cell Status'], df['Count'], color=['blue', 'red'])
        plt.xlabel('Cell Status')
        plt.ylabel('Count')
        plt.title('Cell Viability')
        plt.show()

    except ValueError as ve:
        print("Error:", ve)

if __name__ == "__main__":
    main()

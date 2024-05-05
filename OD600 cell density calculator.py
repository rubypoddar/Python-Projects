import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def calculate_cell_density(od600, path_length, conversion_factor=1.0):
    """
    Calculate the cell density (cells/mL) from OD600 readings.
    Args:
    - od600: OD600 reading.
    - path_length: Path length of the cuvette used in the spectrophotometer (in cm).
    - conversion_factor: Conversion factor specific to the cell type and growth conditions (default is 1.0).
    Returns:
    - cell_density: Cell density in cells/mL.
    """
    if od600 <= 0 or path_length <= 0:
        raise ValueError("Invalid input. OD600 and path length must be positive values.")

    cell_density = (od600 / (conversion_factor * path_length)) * 1e7  # Conversion factor for OD600 to cell density
    return cell_density

def main():
    print("Welcome to the Advanced OD600 to Cell Density Calculator!")
    print("This calculator estimates cell density from OD600 readings.")

    try:
        # Input parameters
        od600 = float(input("Enter the OD600 reading: "))
        path_length = float(input("Enter the path length of the cuvette used (in cm): "))
        conversion_factor = float(input("Enter the conversion factor (default is 1.0): "))
        cell_type = input("Enter the type of cells (e.g., E. coli, yeast, mammalian): ")

        # Calculate cell density
        cell_density = calculate_cell_density(od600, path_length, conversion_factor)

        # Output cell density
        print("\nEstimated Cell Density: {:.2f} cells/mL".format(cell_density))

    except ValueError as ve:
        print("Error:", ve)

if __name__ == "__main__":
    main()

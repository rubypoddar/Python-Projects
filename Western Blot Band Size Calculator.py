import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def calculate_band_size(migration_distance, standard_distances, standard_molecular_weights):
    """
    Calculate the size of a protein band on a Western blot based on its migration distance
    and the migration distances and molecular weights of protein standards.
    Args:
    - migration_distance: Migration distance of the protein band of interest (in mm).
    - standard_distances: List of migration distances of protein standards (in mm).
    - standard_molecular_weights: List of molecular weights of protein standards (in kDa).
    Returns:
    - band_size: Estimated size of the protein band of interest (in kDa).
    """
    # Perform linear regression to calculate the slope and intercept of the standard curve
    slope, intercept = np.polyfit(standard_distances, standard_molecular_weights, 1)

    # Use the linear regression equation to estimate the size of the protein band
    band_size = (migration_distance - intercept) / slope
    return band_size

def main():
    print("Welcome to the Western Blot Band Size Calculator!")
    print("This calculator estimates the size of a protein band on a Western blot.")

    try:
        # Input migration distance of the protein band of interest
        migration_distance = float(input("Enter the migration distance of the protein band of interest (in mm): "))

        # Input migration distances of protein standards
        standard_distances_input = input("Enter the migration distances of protein standards (comma-separated, in mm): ")
        standard_distances = [float(val.strip()) for val in standard_distances_input.split(',')]

        # Input molecular weights of protein standards
        standard_molecular_weights_input = input("Enter the molecular weights of protein standards (comma-separated, in kDa): ")
        standard_molecular_weights = [float(val.strip()) for val in standard_molecular_weights_input.split(',')]

        # Validate input data
        if len(standard_distances) != len(standard_molecular_weights):
            raise ValueError("Invalid input data. The number of migration distances and molecular weights should be the same.")

        # Calculate band size
        band_size = calculate_band_size(migration_distance, standard_distances, standard_molecular_weights)

        # Output band size
        print("\nEstimated Size of the Protein Band: {:.2f} kDa".format(band_size))

        # Plot standard curve and the protein band
        plt.figure(figsize=(8, 6))
        plt.scatter(standard_distances, standard_molecular_weights, color='blue', label='Protein Standards')
        plt.xlabel('Migration Distance (mm)')
        plt.ylabel('Molecular Weight (kDa)')
        plt.title('Western Blot Standard Curve')
        plt.axvline(x=migration_distance, color='red', linestyle='--', label='Protein Band')
        plt.legend()
        plt.grid(True)
        plt.show()

    except ValueError as ve:
        print("Error:", ve)

if __name__ == "__main__":
    main()

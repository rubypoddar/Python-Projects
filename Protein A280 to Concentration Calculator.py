import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class ProteinConcentrationCalculator:
    def __init__(self):
        self.molar_absorptivity_data = {
            "protein_A": 1490,  # Example molar absorptivity coefficient for protein A
            "protein_B": 1800,  # Example molar absorptivity coefficient for protein B
            # Add more proteins and their respective coefficients as needed
        }

    def calculate_concentration(self, a280, path_length, protein_type="protein_A"):
        """
        Calculate the concentration of a protein solution from A280 readings.
        Args:
        - a280: Absorbance at 280 nm (A280).
        - path_length: Path length of the cuvette used in the spectrophotometer (in cm).
        - protein_type: Type of protein (default is "protein_A").
        Returns:
        - concentration: Concentration of the protein solution (in M).
        """
        if a280 <= 0 or path_length <= 0:
            raise ValueError("Invalid input. A280 and path length must be positive values.")

        molar_absorptivity = self.molar_absorptivity_data.get(protein_type)
        if molar_absorptivity is None:
            raise ValueError("Invalid protein type. Protein type must be one of: {}".format(", ".join(self.molar_absorptivity_data.keys())))

        concentration = a280 / (molar_absorptivity * path_length)
        return concentration

def main():
    print("Welcome to the Advanced Protein A280 to Concentration Calculator!")
    print("This calculator estimates protein concentration from A280 readings.")

    try:
        # Initialize calculator
        calculator = ProteinConcentrationCalculator()

        # Input parameters
        a280 = float(input("Enter the absorbance at 280 nm (A280): "))
        path_length = float(input("Enter the path length of the cuvette used (in cm): "))
        protein_type = input("Enter the type of protein (default is 'protein_A'): ")

        # Calculate protein concentration
        concentration = calculator.calculate_concentration(a280, path_length, protein_type)

        # Output protein concentration
        print("\nEstimated Protein Concentration: {:.4f} M".format(concentration))

    except ValueError as ve:
        print("Error:", ve)

if __name__ == "__main__":
    main()

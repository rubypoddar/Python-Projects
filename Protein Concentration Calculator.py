import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def calculate_protein_concentration(absorbance_values, extinction_coefficient, pathlength):
    """
    Calculate protein concentration using the Beer-Lambert law.
    Args:
    - absorbance_values: List/array of absorbance values.
    - extinction_coefficient: Extinction coefficient of the protein.
    - pathlength: Pathlength of the cuvette used in the spectrophotometer (in cm).
    Returns:
    - protein_concentrations: List/array of calculated protein concentrations (in mg/mL).
    """
    protein_concentrations = (np.array(absorbance_values) / extinction_coefficient) * 1000 / pathlength
    return protein_concentrations

def plot_standard_curve(absorbance_values, protein_concentrations):
    """
    Plot the standard curve.
    """
    plt.figure(figsize=(8, 6))
    plt.scatter(protein_concentrations, absorbance_values, color='blue', label='Data Points')
    plt.xlabel('Protein Concentration (mg/mL)')
    plt.ylabel('Absorbance')
    plt.title('Protein Standard Curve')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    print("Welcome to the Protein Concentration Calculator!")
    print("This calculator estimates the concentration of a protein solution based on absorbance measurements.")

    try:
        # Input parameters
        absorbance_input = input("Enter absorbance values (comma-separated): ")
        absorbance_values = [float(val.strip()) for val in absorbance_input.split(',')]
        extinction_coefficient = float(input("Enter the extinction coefficient of the protein (in L/(mg*cm)): "))
        pathlength = float(input("Enter the pathlength of the cuvette used in the spectrophotometer (in cm): "))

        # Validate input data
        if len(absorbance_values) < 2 or extinction_coefficient <= 0 or pathlength <= 0 or not all(isinstance(val, (int, float)) for val in absorbance_values) or any(val <= 0 for val in absorbance_values):
            raise ValueError("Invalid input data. Absorbance values should have at least 2 valid numeric data points, and extinction coefficient and pathlength should be positive.")

        # Calculate protein concentrations
        protein_concentrations = calculate_protein_concentration(absorbance_values, extinction_coefficient, pathlength)

        # Plot standard curve
        plot_standard_curve(absorbance_values, protein_concentrations)

        # Create DataFrame for standard curve data
        data = {'Absorbance': absorbance_values, 'Protein Concentration (mg/mL)': protein_concentrations}
        df = pd.DataFrame(data)

        # Output DataFrame
        print("\nStandard Curve Data:")
        print(df)

    except ValueError as ve:
        print("Error:", ve)

if __name__ == "__main__":
    main()

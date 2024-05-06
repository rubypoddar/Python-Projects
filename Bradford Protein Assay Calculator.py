import numpy as np
import matplotlib.pyplot as plt

def linear_regression(x, y):
    """
    Perform linear regression.
    Args:
    - x: Independent variable (protein standard concentrations).
    - y: Dependent variable (absorbance values).
    Returns:
    - slope: Slope of the regression line.
    - intercept: Intercept of the regression line.
    """
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    numerator = np.sum((x - mean_x) * (y - mean_y))
    denominator = np.sum((x - mean_x) ** 2)
    slope = numerator / denominator
    intercept = mean_y - slope * mean_x
    return slope, intercept

def bradford_assay(protein_standard_concentration, absorbance_values):
    """
    Calculate protein concentration using the Bradford assay.
    Args:
    - protein_standard_concentration: List/array of protein standard concentrations (in mg/mL).
    - absorbance_values: List/array of absorbance values for protein standards.
    Returns:
    - protein_concentrations: List/array of calculated protein concentrations (in mg/mL).
    """
    slope, intercept = linear_regression(protein_standard_concentration, absorbance_values)
    protein_concentrations = (np.array(absorbance_values) - intercept) / slope
    return protein_concentrations

def plot_standard_curve(protein_standard_concentration, absorbance_values, protein_concentrations):
    """
    Plot the standard curve.
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(protein_standard_concentration, absorbance_values, color='blue', label='Data Points')
    plt.plot(protein_standard_concentration, protein_concentrations, color='red', label='Standard Curve')
    plt.xlabel('Protein Standard Concentration (mg/mL)')
    plt.ylabel('Absorbance')
    plt.title('Bradford Protein Standard Curve')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    print("Welcome to the Bradford Protein Assay Calculator!")
    print("This calculator estimates the concentration of a protein solution using the Bradford assay.")

    try:
        # Input protein standard concentrations and absorbance values
        protein_standard_concentration_input = input("Enter protein standard concentrations (comma-separated, in mg/mL): ")
        protein_standard_concentration = np.array([float(val.strip()) for val in protein_standard_concentration_input.split(',')])
        absorbance_values_input = input("Enter absorbance values for protein standards (comma-separated): ")
        absorbance_values = np.array([float(val.strip()) for val in absorbance_values_input.split(',')])

        # Validate input data
        if len(protein_standard_concentration) < 2 or len(protein_standard_concentration) != len(absorbance_values):
            raise ValueError("Invalid input data. At least 2 protein standard concentrations are required, and the number of absorbance values should match the number of standard concentrations.")

        # Calculate protein concentrations
        protein_concentrations = bradford_assay(protein_standard_concentration, absorbance_values)

        # Plot standard curve
        plot_standard_curve(protein_standard_concentration, absorbance_values, protein_concentrations)

        # Output protein concentrations
        print("\nEstimated Protein Concentrations:")
        for i, conc in enumerate(protein_concentrations):
            print("Standard {}: {:.2f} mg/mL".format(i+1, conc))

    except ValueError as ve:
        print("Error:", ve)

if __name__ == "__main__":
    main()

import numpy as np
import matplotlib.pyplot as plt

def generate_standard_curve(standard_concentrations, absorbance_values):
    """
    Generate the standard curve using the provided absorbance values and known protein concentrations.
    Args:
    - standard_concentrations: Array of known protein standard concentrations (in mg/mL).
    - absorbance_values: Array of corresponding absorbance values.
    Returns:
    - slope: Slope of the standard curve.
    - intercept: Intercept of the standard curve.
    """
    slope, intercept = np.polyfit(standard_concentrations, absorbance_values, 1)
    return slope, intercept

def calculate_protein_concentration(unknown_absorbance, slope, intercept):
    """
    Calculate protein concentration using the standard curve equation.
    Args:
    - unknown_absorbance: Absorbance value of the unknown sample.
    - slope: Slope of the standard curve.
    - intercept: Intercept of the standard curve.
    Returns:
    - protein_concentration: Estimated protein concentration of the unknown sample (in mg/mL).
    """
    protein_concentration = (unknown_absorbance - intercept) / slope
    return protein_concentration

def plot_standard_curve(standard_concentrations, absorbance_values, slope, intercept):
    """
    Plot the standard curve.
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(standard_concentrations, absorbance_values, color='blue', label='Data Points')
    plt.plot(standard_concentrations, slope * standard_concentrations + intercept, color='red', label='Standard Curve')
    plt.xlabel('Protein Standard Concentration (mg/mL)')
    plt.ylabel('Absorbance')
    plt.title('BCA Protein Standard Curve')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    print("Welcome to the BCA Protein Assay Calculator!")
    print("This calculator estimates the concentration of a protein solution using the BCA assay.")

    try:
        # Input protein standard concentrations and absorbance values
        standard_concentration_input = input("Enter known protein standard concentrations (comma-separated, in mg/mL): ")
        standard_concentrations = np.array([float(val.strip()) for val in standard_concentration_input.split(',')])
        absorbance_values_input = input("Enter absorbance values for protein standards (comma-separated): ")
        absorbance_values = np.array([float(val.strip()) for val in absorbance_values_input.split(',')])

        # Validate input data
        if len(standard_concentrations) < 2 or len(standard_concentrations) != len(absorbance_values):
            raise ValueError("Invalid input data. At least 2 known protein standard concentrations are required, and the number of absorbance values should match the number of standard concentrations.")

        # Generate standard curve
        slope, intercept = generate_standard_curve(standard_concentrations, absorbance_values)

        # Plot standard curve
        plot_standard_curve(standard_concentrations, absorbance_values, slope, intercept)

        # Input absorbance value of the unknown sample
        unknown_absorbance = float(input("Enter absorbance value of the unknown sample: "))

        # Calculate protein concentration of the unknown sample
        protein_concentration = calculate_protein_concentration(unknown_absorbance, slope, intercept)

        # Output estimated protein concentration
        print("\nEstimated Protein Concentration of the Unknown Sample: {:.2f} mg/mL".format(protein_concentration))

    except ValueError as ve:
        print("Error:", ve)

if __name__ == "__main__":
    main()

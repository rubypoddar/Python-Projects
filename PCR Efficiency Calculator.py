import numpy as np
import matplotlib.pyplot as plt

def calculate_pcr_efficiency(cycle_thresholds, template_concentrations):
    """
    Calculate PCR efficiency based on cycle thresholds and template concentrations.
    Returns the efficiency.
    """
    try:
        # Perform linear regression to calculate slope (m) of the standard curve
        m, _ = np.polyfit(template_concentrations, cycle_thresholds, 1)
        
        # Efficiency (E) calculation: E = 10^(-1/m) - 1
        efficiency = 10 ** (-1 / m) - 1
        return efficiency
    except Exception as e:
        print("Error:", e)
        return None

def plot_standard_curve(template_concentrations, cycle_thresholds, efficiency):
    """
    Plot the standard curve and linear regression line.
    """
    plt.figure(figsize=(8, 6))
    plt.scatter(template_concentrations, cycle_thresholds, color='blue', label='Data Points')
    
    # Plot linear regression line
    m, b = np.polyfit(np.log10(template_concentrations), cycle_thresholds, 1)
    x_fit = np.linspace(min(np.log10(template_concentrations)), max(np.log10(template_concentrations)), 100)
    y_fit = m * x_fit + b
    plt.plot(10**x_fit, y_fit, color='red', label='Linear Regression Line')
    
    plt.xscale('log')
    plt.xlabel('Template Concentration')
    plt.ylabel('Cycle Threshold')
    plt.title('PCR Standard Curve')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    print("Welcome to the PCR Efficiency Calculator!")

    try:
        # Input data points
        template_concentrations = list(map(float, input("Enter template concentrations (comma-separated): ").split(',')))
        cycle_thresholds = list(map(float, input("Enter corresponding cycle thresholds (comma-separated): ").split(',')))
        
        # Validate input data
        if len(template_concentrations) != len(cycle_thresholds) or len(template_concentrations) < 2:
            raise ValueError("Invalid input data. Number of template concentrations and cycle thresholds should be the same, and at least two data points are required.")

        # Calculate PCR efficiency
        efficiency = calculate_pcr_efficiency(cycle_thresholds, template_concentrations)
        if efficiency is not None:
            print("PCR Efficiency:", efficiency)
            
            # Plot standard curve
            plot_standard_curve(template_concentrations, cycle_thresholds, efficiency)

    except ValueError as ve:
        print("Error:", ve)

if __name__ == "__main__":
    main()

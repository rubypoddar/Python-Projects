import numpy as np
import matplotlib.pyplot as plt

def standard_curve(x_values, y_values):
    """
    Fit a standard curve to the provided absorbance values and return the slope and intercept.

    Parameters:
    - x_values: Concentration values (e.g., ng/mL)
    - y_values: Corresponding absorbance values

    Returns:
    - slope: Slope of the standard curve
    - intercept: Intercept of the standard curve
    """
    slope, intercept = np.polyfit(x_values, y_values, 1)
    return slope, intercept

def analyze_sample(absorbance, slope, intercept):
    """
    Analyze the sample absorbance values using the provided standard curve parameters.

    Parameters:
    - absorbance: Absorbance values of the sample
    - slope: Slope of the standard curve
    - intercept: Intercept of the standard curve

    Returns:
    - concentration: Estimated concentration of the sample
    """
    concentration = (absorbance - intercept) / slope
    return concentration

# Input for standard curve points
num_points = int(input("Enter the number of standard curve points: "))
print("Enter the concentration (ng/mL) and corresponding absorbance values for each point:")
standard_concentrations = []
absorbance_values = []
for i in range(num_points):
    concentration = float(input(f"Concentration {i+1}: "))
    absorbance = float(input(f"Absorbance {i+1}: "))
    standard_concentrations.append(concentration)
    absorbance_values.append(absorbance)

# Fit standard curve
slope, intercept = standard_curve(standard_concentrations, absorbance_values)

# Input for sample absorbance
sample_absorbance = float(input("Enter the absorbance value of the sample: "))

# Analyze sample absorbance
estimated_concentration = analyze_sample(sample_absorbance, slope, intercept)

# Plot standard curve
plt.figure(figsize=(8, 6))
plt.scatter(standard_concentrations, absorbance_values, color='blue', label='Standard Curve Points')
plt.plot(standard_concentrations, slope * np.array(standard_concentrations) + intercept, color='red', linestyle='--', label='Standard Curve Fit')
plt.xlabel('Concentration (ng/mL)')
plt.ylabel('Absorbance')
plt.title('ELISA Standard Curve')
plt.legend()
plt.grid(True)
plt.show()

# Display estimated concentration of sample
print(f"Estimated concentration of sample: {estimated_concentration:.2f} ng/mL")

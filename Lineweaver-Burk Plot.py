import numpy as np
import matplotlib.pyplot as plt

def michaelis_menten(substrate_concentration, vmax, km):
    """
    Calculate reaction rate using the Michaelis-Menten equation.

    Parameters:
    - substrate_concentration: Substrate concentration
    - vmax: Maximum reaction rate
    - km: Michaelis constant

    Returns:
    - reaction_rate: Reaction rate
    """
    reaction_rate = (vmax * substrate_concentration) / (km + substrate_concentration)
    return reaction_rate

def lineweaver_burk_plot(substrate_concentration, reaction_rate):
    """
    Generate Lineweaver-Burk plot.

    Parameters:
    - substrate_concentration: Array of substrate concentrations
    - reaction_rate: Array of reaction rates
    """
    reciprocal_substrate = 1 / substrate_concentration
    reciprocal_rate = 1 / reaction_rate

    # Perform linear regression
    slope, intercept = np.polyfit(reciprocal_substrate, reciprocal_rate, 1)
    x_fit = np.linspace(0, max(reciprocal_substrate), 100)
    y_fit = slope * x_fit + intercept

    # Plot Lineweaver-Burk plot
    plt.figure(figsize=(8, 6))
    plt.scatter(reciprocal_substrate, reciprocal_rate, label='Experimental Data')
    plt.plot(x_fit, y_fit, color='red', linestyle='--', label='Linear Fit')
    plt.xlabel('1/[S] (1/mM)')
    plt.ylabel('1/Reaction Rate (1/s)')
    plt.title('Lineweaver-Burk Plot')
    plt.legend()
    plt.grid(True)
    plt.show()

# Example data
substrate_concentration = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
vmax = 10
km = 2

# Calculate reaction rates using Michaelis-Menten equation
reaction_rate = michaelis_menten(substrate_concentration, vmax, km)

# Generate Lineweaver-Burk plot
lineweaver_burk_plot(substrate_concentration, reaction_rate)

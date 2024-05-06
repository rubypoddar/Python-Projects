import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def calculate_zeta_potential(pH, particle_size):
    """
    Calculate Zeta potential based on pH and particle size.

    Parameters:
    - pH: pH value
    - particle_size: Particle size in nm

    Returns:
    - zeta_potential: Calculated Zeta potential in mV
    """
    zeta_potential = 20 * np.sin(pH) / np.sqrt(particle_size)
    return zeta_potential

# User input for pH and particle size
pH = float(input("Enter pH value: "))
particle_size = float(input("Enter particle size (nm): "))

# Calculate Zeta potential
zeta_potential = calculate_zeta_potential(pH, particle_size)

# Simulated data for plotting
pH_range = np.linspace(3, 9, 100)
particle_size_range = np.linspace(50, 200, 100)
pH_mesh, particle_size_mesh = np.meshgrid(pH_range, particle_size_range)
zeta_potential_mesh = calculate_zeta_potential(pH_mesh, particle_size_mesh)

# Create 3D scatter plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot data points
ax.scatter(pH, particle_size, zeta_potential, color='r', marker='o', label='Zeta Potential')

# Plot surface
ax.plot_surface(pH_mesh, particle_size_mesh, zeta_potential_mesh, cmap='viridis', alpha=0.5)

# Set labels and title
ax.set_xlabel('pH')
ax.set_ylabel('Particle Size (nm)')
ax.set_zlabel('Zeta Potential (mV)')
ax.set_title('Zeta Potential Calculator')

# Show calculated Zeta potential
ax.text(pH, particle_size, zeta_potential, f' Zeta Potential: {zeta_potential:.2f} mV', color='r')

# Show plot
plt.legend()
plt.show()

import numpy as np

def calculate_fret_efficiency(distance, R0):
    """
    Calculate FRET efficiency based on the distance between donor and acceptor fluorophores (r),
    the Förster distance (R0), and the orientation factor (kappa2).

    Parameters:
    - distance: Distance between donor and acceptor fluorophores (in Ångströms)
    - R0: Förster distance (in Ångströms)

    Returns:
    - FRET efficiency (a value between 0 and 1)
    """
    kappa2 = 2/3  # Default value for freely rotating fluorophores
    return 1 / (1 + (distance / R0) ** 6 * kappa2)

# Input distance and Förster distance
distance = float(input("Enter the distance between donor and acceptor fluorophores (Å): "))
R0 = float(input("Enter the Förster distance (Å): "))

# Calculate FRET efficiency
fret_efficiency = calculate_fret_efficiency(distance, R0)

# Display FRET efficiency
print(f"FRET Efficiency: {fret_efficiency:.2f}")

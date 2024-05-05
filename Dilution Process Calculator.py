import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def calculate_final_concentration(initial_concentration, initial_volume, final_volume, unit='M'):
    """
    Calculate the final concentration of a solution after dilution.
    Args:
    - initial_concentration: Initial concentration of the solution (in mol/L or M).
    - initial_volume: Initial volume of the solution (in liters or L).
    - final_volume: Final volume of the solution after dilution (in liters or L).
    - unit: Unit of concentration (default is 'M').
    Returns:
    - final_concentration: Final concentration of the solution after dilution.
    """
    if initial_concentration < 0 or initial_volume < 0 or final_volume < 0:
        raise ValueError("Invalid input. Concentration and volumes must be non-negative.")

    if unit == 'M':
        final_concentration = (initial_concentration * initial_volume) / final_volume
    elif unit == 'mM':
        final_concentration = (initial_concentration * initial_volume) / (final_volume * 1e3)
    elif unit == 'μM':
        final_concentration = (initial_concentration * initial_volume) / (final_volume * 1e6)
    else:
        raise ValueError("Invalid concentration unit. Please use 'M', 'mM', or 'μM'.")

    return final_concentration

def main():
    print("Welcome to the Advanced Dilution Calculator!")
    print("This calculator computes the final concentration of a solution after dilution.")

    try:
        # Input parameters
        initial_concentration = float(input("Enter the initial concentration of the solution (in mol/L): "))
        initial_volume = float(input("Enter the initial volume of the solution (in liters): "))
        final_volume = float(input("Enter the final volume of the solution after dilution (in liters): "))
        unit = input("Enter the unit of concentration (M, mM, or μM): ")

        # Calculate final concentration
        final_concentration = calculate_final_concentration(initial_concentration, initial_volume, final_volume, unit)

        # Output final concentration
        print("\nFinal Concentration of the Solution: {:.4f} {}".format(final_concentration, unit))

        # Visualize the dilution process
        plt.figure(figsize=(8, 6))
        plt.plot([0, initial_volume, final_volume], [initial_concentration, initial_concentration, final_concentration], marker='o')
        plt.xlabel('Volume (L)')
        plt.ylabel('Concentration (mol/L)')
        plt.title('Dilution Process')
        plt.grid(True)
        plt.show()

    except ValueError as ve:
        print("Error:", ve)

if __name__ == "__main__":
    main()

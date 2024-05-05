import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def calculate_final_concentration(initial_concentration, initial_volume, final_volume):
    """
    Calculate the final concentration of a solution after dilution.
    Args:
    - initial_concentration: Initial concentration of the solution (in mol/L or M).
    - initial_volume: Initial volume of the solution (in liters or L).
    - final_volume: Final volume of the solution after dilution (in liters or L).
    Returns:
    - final_concentration: Final concentration of the solution after dilution (in mol/L or M).
    """
    final_concentration = (initial_concentration * initial_volume) / final_volume
    return final_concentration

def main():
    print("Welcome to the Dilution Calculator!")
    print("This calculator computes the final concentration of a solution after dilution.")

    try:
        # Input parameters
        initial_concentration = float(input("Enter the initial concentration of the solution (in mol/L or M): "))
        initial_volume = float(input("Enter the initial volume of the solution (in liters or L): "))
        final_volume = float(input("Enter the final volume of the solution after dilution (in liters or L): "))

        # Calculate final concentration
        final_concentration = calculate_final_concentration(initial_concentration, initial_volume, final_volume)

        # Output final concentration
        print("\nFinal Concentration of the Solution: {:.4f} mol/L".format(final_concentration))

    except ValueError as ve:
        print("Error:", ve)

if __name__ == "__main__":
    main()

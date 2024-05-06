import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def calculate_molarity(mass_solute, molecular_weight, volume_solvent):
    """
    Calculate the molarity of a solution.
    Args:
    - mass_solute: Mass of the solute (in grams).
    - molecular_weight: Molecular weight of the solute (in g/mol).
    - volume_solvent: Volume of the solvent (in liters).
    Returns:
    - molarity: Molarity of the solution (in moles/L).
    """
    molarity = (mass_solute / molecular_weight) / volume_solvent
    return molarity

def main():
    print("Welcome to the Molarity Calculator!")
    print("This calculator computes the molarity of a solution.")

    try:
        # Input parameters
        mass_solute = float(input("Enter the mass of the solute (in grams): "))
        molecular_weight = float(input("Enter the molecular weight of the solute (in g/mol): "))
        volume_solvent = float(input("Enter the volume of the solvent (in liters): "))

        # Calculate molarity
        molarity = calculate_molarity(mass_solute, molecular_weight, volume_solvent)

        # Output molarity
        print("\nMolarity of the Solution: {:.4f} moles/L".format(molarity))

    except ValueError as ve:
        print("Error:", ve)

if __name__ == "__main__":
    main()

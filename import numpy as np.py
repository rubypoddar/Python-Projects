import numpy as np
import pandas as pd

def calculate_purification_yield(initial_concentration, final_concentration, initial_volume):
    """
    Calculate the yield of protein purification.
    """
    initial_amount = initial_concentration * initial_volume
    final_amount = final_concentration * initial_volume
    yield_percent = (final_amount / initial_amount) * 100
    return yield_percent

if __name__ == "__main__":
    # Take input for initial protein concentration, final protein concentration, and initial volume
    initial_concentration = float(input("Enter the initial protein concentration (in mg/mL): "))
    final_concentration = float(input("Enter the final protein concentration (in mg/mL): "))
    initial_volume = float(input("Enter the initial volume (in mL): "))

    # Calculate the yield of protein purification
    yield_percent = calculate_purification_yield(initial_concentration, final_concentration, initial_volume)
    
    # Create a DataFrame for output formatting
    df_output = pd.DataFrame({
        'Parameter': ['Initial Protein Concentration', 'Final Protein Concentration', 'Initial Volume', 'Yield'],
        'Value': [initial_concentration, final_concentration, initial_volume, yield_percent]
    })

    # Output the result
    print("Protein Purification Yield:")
    print(df_output)

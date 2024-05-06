import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def calculate_reagent_volumes(sample_volume, sample_concentration, antibody_volume, antibody_concentration, substrate_volume):
    """
    Calculate reagent volumes for ELISA experiment.
    Args:
    - sample_volume: Volume of sample to be added to each well (in μL).
    - sample_concentration: Concentration of sample (in ng/mL).
    - antibody_volume: Volume of antibody to be added to each well (in μL).
    - antibody_concentration: Concentration of antibody (in μg/mL).
    - substrate_volume: Volume of substrate to be added to each well (in μL).
    Returns:
    - reagent_volumes: DataFrame containing reagent volumes for each well.
    """
    # Calculate sample volume for each well based on sample concentration
    sample_volume_per_well = (sample_volume * 1000) / sample_concentration  # Convert ng/mL to μg/mL
    sample_volumes = np.full((8, 12), sample_volume_per_well)

    # Calculate antibody volume for each well based on antibody concentration
    antibody_volume_per_well = (antibody_volume * 1000) / antibody_concentration  # Convert μg/mL to ng/mL
    antibody_volumes = np.full((8, 12), antibody_volume_per_well)

    # Create DataFrame for reagent volumes
    reagent_volumes = pd.DataFrame({
        'Sample Volume (μL)': sample_volumes.flatten(),
        'Antibody Volume (μL)': antibody_volumes.flatten(),
        'Substrate Volume (μL)': substrate_volume
    })

    return reagent_volumes

def main():
    print("Welcome to the ELISA Plate Calculator!")
    print("This calculator assists in designing ELISA experiments by calculating reagent volumes.")

    try:
        # Input parameters
        sample_volume = float(input("Enter the volume of sample to be added to each well (in μL): "))
        sample_concentration = float(input("Enter the concentration of sample (in ng/mL): "))
        antibody_volume = float(input("Enter the volume of antibody to be added to each well (in μL): "))
        antibody_concentration = float(input("Enter the concentration of antibody (in μg/mL): "))
        substrate_volume = float(input("Enter the volume of substrate to be added to each well (in μL): "))

        # Calculate reagent volumes
        reagent_volumes = calculate_reagent_volumes(sample_volume, sample_concentration, antibody_volume, antibody_concentration, substrate_volume)

        # Output reagent volumes
        print("\nReagent Volumes for Each Well:")
        print(reagent_volumes)

        # Create a heatmap to visualize reagent volumes
        plt.figure(figsize=(10, 6))
        plt.imshow(reagent_volumes.values, cmap='Blues', interpolation='nearest')
        plt.colorbar(label='Reagent Volume (μL)')
        plt.xlabel('Column')
        plt.ylabel('Row')
        plt.title('ELISA Plate Reagent Volumes')
        plt.show()

    except ValueError as ve:
        print("Error:", ve)

if __name__ == "__main__":
    main()

import numpy as np

def calculate_gel_percentage(molecular_weight, separation_range=(10, 250), resolution=0.1):
    """
    Calculate the appropriate SDS-PAGE gel percentage based on the molecular weight range of proteins,
    desired separation range, and resolution.
    Args:
    - molecular_weight: Molecular weight of the protein of interest (in kDa).
    - separation_range: Tuple specifying the desired separation range of proteins (in kDa) (default is (10, 250)).
    - resolution: Desired resolution (default is 0.1).
    Returns:
    - gel_percentage: Recommended SDS-PAGE gel percentage.
    """
    # Constants for resolving power of different gel percentages
    resolving_power = {
        3: 3.3,
        4: 2.0,
        5: 1.4,
        6: 1.2,
        7: 1.0,
        8: 0.8,
        10: 0.6,
        12: 0.5,
        15: 0.4
    }

    # Find the gel percentage that provides the desired resolution
    for gel_percentage, rp in resolving_power.items():
        gel_separation_range = (separation_range[0] / gel_percentage, separation_range[1] / gel_percentage)
        if molecular_weight >= gel_separation_range[0] and molecular_weight <= gel_separation_range[1]:
            if molecular_weight * resolution <= rp:
                return gel_percentage
    return None

def main():
    print("Welcome to the Bestest SDS-PAGE Gel Percentage Calculator!")
    print("This calculator recommends the appropriate gel percentage for SDS-PAGE based on various parameters.")

    try:
        # Input molecular weight of the protein
        molecular_weight = float(input("Enter the molecular weight of the protein (in kDa): "))

        # Input desired separation range
        separation_range_input = input("Enter the desired separation range (in kDa, default is 10-250): ") or "10-250"
        separation_range = tuple(map(float, separation_range_input.split('-')))

        # Input desired resolution
        resolution = float(input("Enter the desired resolution (default is 0.1): ") or 0.1)

        # Calculate gel percentage
        gel_percentage = calculate_gel_percentage(molecular_weight, separation_range, resolution)

        if gel_percentage:
            print("\nRecommended SDS-PAGE Gel Percentage: {}%".format(gel_percentage))
        else:
            print("\nNo suitable gel percentage found for the provided parameters.")

    except ValueError as ve:
        print("Error:", ve)

if __name__ == "__main__":
    main()

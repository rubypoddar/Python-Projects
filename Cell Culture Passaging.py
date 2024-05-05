import numpy as np

def calculate_passaging(cell_density, split_ratio, target_density):
    """
    Calculate the number of cells to seed and the volume of medium needed for passaging.

    Parameters:
    - cell_density: Current cell density (cells/cm^2)
    - split_ratio: Split ratio (e.g., 1:2 for 1 part of cells to 2 parts of fresh medium)
    - target_density: Target cell density after passaging (cells/cm^2)

    Returns:
    - cells_to_seed: Number of cells to seed
    - medium_volume: Volume of medium needed (in mL)
    """
    cells_to_seed = (target_density * split_ratio - cell_density) / (1 - split_ratio)
    medium_volume = cells_to_seed / cell_density
    return cells_to_seed, medium_volume

# Input parameters
cell_density = float(input("Enter the current cell density (cells/cm^2): "))
split_ratio = float(input("Enter the split ratio (e.g., 1:2 for 1 part of cells to 2 parts of fresh medium): "))
target_density = float(input("Enter the target cell density after passaging (cells/cm^2): "))

# Calculate passaging parameters
cells_to_seed, medium_volume = calculate_passaging(cell_density, split_ratio, target_density)

# Display results
print(f"Number of cells to seed: {cells_to_seed:.2f} cells")
print(f"Volume of medium needed: {medium_volume:.2f} mL")


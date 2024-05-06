import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def logistic_function(concentration_ligand, kd, cooperativity=1):
    """
    Calculate the binding affinity based on the dissociation constant (Kd) and ligand concentration
    using a logistic function.

    Parameters:
    - concentration_ligand: Array of ligand concentrations
    - kd: Dissociation constant (Kd)
    - cooperativity: Cooperativity factor (default: 1 for no cooperativity)

    Returns:
    - binding_affinity: Array of calculated binding affinities
    """
    binding_affinity = 1 / (1 + (concentration_ligand / kd) ** cooperativity)
    return binding_affinity

# Input from the user
concentration_ligand_input = input("Enter ligand concentrations separated by commas: ")
kd = float(input("Enter the dissociation constant (Kd): "))
cooperativity = float(input("Enter the cooperativity factor: "))

# Convert input string to array of concentrations
concentration_ligand = np.array([float(x) for x in concentration_ligand_input.split(',')])

# Calculate binding affinity using the logistic function model
binding_affinity = logistic_function(concentration_ligand, kd, cooperativity)

# Plot the binding affinity using Seaborn
sns.set(style="whitegrid")
plt.figure(figsize=(8, 6))
sns.lineplot(x=concentration_ligand, y=binding_affinity, marker='o')
plt.xlabel('Ligand Concentration')
plt.ylabel('Binding Affinity')
plt.title('Protein-Ligand Binding Affinity')
plt.grid(True)
plt.show()

# Display output in the console
print("Binding affinities:")
for conc, ba in zip(concentration_ligand, binding_affinity):
    print(f"Ligand concentration: {conc}, Binding affinity: {ba}")

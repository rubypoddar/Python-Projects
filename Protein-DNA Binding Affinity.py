import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def binding_affinity_model(concentration_protein1, concentration_protein2, kd, cooperativity=1):
    """
    Calculate the binding affinity between two proteins based on the dissociation constant (Kd) 
    and the concentrations of the two proteins using a logistic function.

    Parameters:
    - concentration_protein1: Array of concentrations of protein 1
    - concentration_protein2: Array of concentrations of protein 2
    - kd: Dissociation constant (Kd)
    - cooperativity: Cooperativity factor (default: 1 for no cooperativity)

    Returns:
    - binding_affinity: Array of calculated binding affinities
    """
    binding_affinity = 1 / (1 + ((concentration_protein1 * concentration_protein2) / kd) ** cooperativity)
    return binding_affinity

# Input from the user
concentration_protein1_input = input("Enter concentrations of protein 1 separated by commas: ")
concentration_protein2_input = input("Enter concentrations of protein 2 separated by commas: ")
kd = float(input("Enter the dissociation constant (Kd): "))
cooperativity = float(input("Enter the cooperativity factor: "))

# Convert input strings to arrays of concentrations
concentration_protein1 = np.array([float(x) for x in concentration_protein1_input.split(',')])
concentration_protein2 = np.array([float(x) for x in concentration_protein2_input.split(',')])

# Calculate binding affinity using the model
binding_affinity = binding_affinity_model(concentration_protein1, concentration_protein2, kd, cooperativity)

# Plot the binding affinity using Seaborn
sns.set(style="whitegrid")
plt.figure(figsize=(8, 6))
sns.lineplot(x=concentration_protein1, y=binding_affinity, marker='o', label='Protein 1')
sns.lineplot(x=concentration_protein2, y=binding_affinity, marker='o', label='Protein 2')
plt.xlabel('Protein Concentration')
plt.ylabel('Binding Affinity')
plt.title('Protein-Protein Interaction Affinity')
plt.legend()
plt.grid(True)
plt.show()

# Display output in the console
print("Binding affinities:")
for conc1, conc2, ba in zip(concentration_protein1, concentration_protein2, binding_affinity):
    print(f"Protein 1 concentration: {conc1}, Protein 2 concentration: {conc2}, Binding affinity: {ba}")

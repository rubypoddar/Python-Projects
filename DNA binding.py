import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def binding_affinity_model(concentration_dna, kd, cooperativity=1):
    """
    Calculate the binding affinity between a protein and DNA sequence based on the dissociation constant (Kd) 
    and DNA concentration using a logistic function.

    Parameters:
    - concentration_dna: Array of DNA concentrations
    - kd: Dissociation constant (Kd)
    - cooperativity: Cooperativity factor (default: 1 for no cooperativity)

    Returns:
    - binding_affinity: Array of calculated binding affinities
    """
    binding_affinity = 1 / (1 + (concentration_dna / kd) ** cooperativity)
    return binding_affinity

# Input from the user
concentration_dna_input = input("Enter DNA concentrations separated by commas: ")
kd = float(input("Enter the dissociation constant (Kd): "))
cooperativity = float(input("Enter the cooperativity factor: "))

# Convert input string to array of concentrations
concentration_dna = np.array([float(x) for x in concentration_dna_input.split(',')])

# Calculate binding affinity using the model
binding_affinity = binding_affinity_model(concentration_dna, kd, cooperativity)

# Plot the binding affinity using Seaborn
sns.set(style="whitegrid")
plt.figure(figsize=(8, 6))
sns.lineplot(x=concentration_dna, y=binding_affinity, marker='o')
plt.xlabel('DNA Concentration')
plt.ylabel('Binding Affinity')
plt.title('Protein-DNA Binding Affinity')
plt.grid(True)
plt.show()

# Display output in the console
print("Binding affinities:")
for conc, ba in zip(concentration_dna, binding_affinity):
    print(f"DNA concentration: {conc}, Binding affinity: {ba}")

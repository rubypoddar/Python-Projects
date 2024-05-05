import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def design_primers(target_sequence):
    # Placeholder function for primer design
    # For now, let's generate random primer properties for demonstration
    
    # Generate random data
    np.random.seed(0)
    num_primers = 5
    primer_names = [f"Primer{i+1}" for i in range(num_primers)]
    melting_temps = np.random.uniform(55, 65, num_primers)
    gc_contents = np.random.uniform(40, 60, num_primers)
    
    # Create DataFrame
    primer_data = {
        'Primer': primer_names,
        'Melting Temp (°C)': melting_temps,
        'GC Content (%)': gc_contents
    }
    df = pd.DataFrame(primer_data)
    return df

# Input target sequence
target_seq = input("Enter target sequence: ")
primers_df = design_primers(target_seq)
print("Designed Primers:")
print(primers_df)

# Visualization
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.barplot(x='Primer', y='Melting Temp (°C)', data=primers_df, hue='Primer', dodge=False, palette='viridis', legend=False)
plt.title('Melting Temperature of Primers')
plt.xlabel('Primer')
plt.ylabel('Melting Temp (°C)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from Bio.Restriction import Analysis, RestrictionBatch

def calculate_insert_size(vector_size, insert_size):
    """
    Calculate the size of the resulting recombinant DNA after insertion.
    """
    recombinant_size = vector_size + insert_size
    return recombinant_size

def plot_insert_size_distribution(insert_sizes):
    """
    Plot the distribution of insert DNA fragment sizes.
    """
    plt.figure(figsize=(8, 6))
    sns.histplot(insert_sizes, bins=20, kde=True, color='skyblue')
    plt.title('Insert DNA Fragment Size Distribution')
    plt.xlabel('Insert Size (bp)')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # Example data: vector size and insert size
    vector_size = 5000  # base pairs
    insert_sizes = np.random.normal(loc=1000, scale=100, size=1000)  # Generate 1000 insert sizes

    # Calculate recombinant DNA sizes
    recombinant_sizes = calculate_insert_size(vector_size, insert_sizes)

    # Plot distribution of insert sizes
    plot_insert_size_distribution(insert_sizes)

    # Calculate statistics
    mean_size = np.mean(recombinant_sizes)
    median_size = np.median(recombinant_sizes)
    min_size = np.min(recombinant_sizes)
    max_size = np.max(recombinant_sizes)

    # Create a DataFrame to store statistics
    df_stats = pd.DataFrame({
        'Statistic': ['Mean', 'Median', 'Min', 'Max'],
        'Size (bp)': [mean_size, median_size, min_size, max_size]
    })

    print("Recombinant DNA Size Statistics:")
    print(df_stats)

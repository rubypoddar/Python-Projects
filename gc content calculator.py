import matplotlib.pyplot as plt

def calculate_gc_content(sequence):
    """
    Calculate the GC content of a DNA/RNA sequence.
    """
    sequence = sequence.upper()  # Convert sequence to uppercase
    gc_count = sequence.count('G') + sequence.count('C')  # Count G and C bases
    gc_content = (gc_count / len(sequence)) * 100  # Calculate GC content percentage
    return gc_content

if __name__ == "__main__":
    try:
        # Take input for the DNA/RNA sequence
        sequence = input("Enter the DNA/RNA sequence (use only A, T/U, G, C): ")

        # Validate input sequence
        valid_bases = {'A', 'T', 'U', 'G', 'C'}
        if not set(sequence.upper()).issubset(valid_bases):
            raise ValueError("Invalid input sequence. Please use only A, T/U, G, C.")

        # Calculate the GC content
        gc_content = calculate_gc_content(sequence)

        # Create a bar plot to visualize the GC content
        plt.figure(figsize=(6, 4))  # Set figure size
        plt.bar(['GC Content'], [gc_content], color='skyblue')  # Create bar plot
        plt.ylabel('Percentage')  # Add y-axis label
        plt.title('DNA/RNA GC Content')  # Add title
        plt.ylim(0, 100)  # Set y-axis limit
        plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add gridlines
        plt.show()  # Show plot

    except ValueError as ve:
        print("Error:", ve)
    except Exception as e:
        print("An unexpected error occurred:", e)

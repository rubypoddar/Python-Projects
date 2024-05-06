import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def calculate_doubling_time(initial_count, final_count, time_period):
    """
    Calculate the doubling time of cells during a growth period.
    Args:
    - initial_count: Initial number of cells at the start of the growth period.
    - final_count: Final number of cells at the end of the growth period.
    - time_period: Duration of the growth period (in hours).
    Returns:
    - doubling_time: Time taken for the cell population to double (in hours).
    """
    doubling_time = time_period * np.log(2) / np.log(final_count / initial_count)
    return doubling_time

def main():
    print("Welcome to the Cell Doubling Time Calculator!")
    print("This calculator estimates the time taken for a population of cells to double.")

    try:
        # Input initial and final cell counts
        initial_count = int(input("Enter the initial number of cells: "))
        final_count = int(input("Enter the final number of cells: "))

        # Input duration of the growth period
        time_period = float(input("Enter the duration of the growth period (in hours): "))

        # Calculate doubling time
        doubling_time = calculate_doubling_time(initial_count, final_count, time_period)

        # Output doubling time
        print("\nEstimated Doubling Time: {:.2f} hours".format(doubling_time))

        # Create a bar plot to visualize cell counts
        data = {'Cell Count': [initial_count, final_count]}
        df = pd.DataFrame(data, index=['Initial', 'Final'])
        plt.figure(figsize=(8, 6))
        plt.bar(df.index, df['Cell Count'], color=['blue', 'green'])
        plt.xlabel('Cell Count')
        plt.ylabel('Number of Cells')
        plt.title('Cell Doubling Time')
        plt.show()

    except ValueError as ve:
        print("Error:", ve)

if __name__ == "__main__":
    main()

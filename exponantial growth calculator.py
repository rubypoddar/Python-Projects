import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def exponential_growth(initial_population, growth_rate, time_period):
    """
    Calculate the population size at each time point using exponential growth.
    """
    time_points = np.arange(time_period + 1)
    population_sizes = initial_population * np.exp(growth_rate * time_points)
    return time_points, population_sizes

def plot_growth_curve(time_points, population_sizes):
    """
    Plot the growth curve showing population size over time.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(time_points, population_sizes, marker='o', linestyle='-')
    plt.title('Exponential Growth Curve')
    plt.xlabel('Time')
    plt.ylabel('Population Size')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # Take input for initial population size, growth rate, and time period
    initial_population = float(input("Enter the initial population size: "))
    growth_rate = float(input("Enter the growth rate (as a decimal): "))
    time_period = int(input("Enter the time period (in years): "))

    # Calculate population sizes over time
    time_points, population_sizes = exponential_growth(initial_population, growth_rate, time_period)

    # Plot the growth curve
    plot_growth_curve(time_points, population_sizes)

    # Create a DataFrame to store population sizes at each time point
    df_population = pd.DataFrame({
        'Time': time_points,
        'Population Size': population_sizes
    })

    print("Population Size over Time:")
    print(df_population)

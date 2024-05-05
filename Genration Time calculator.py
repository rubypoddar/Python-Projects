import math

def calculate_generation_time(doubling_time, initial_population, final_population):
    try:
        generation_time = doubling_time / (math.log2(final_population) - math.log2(initial_population))
        return generation_time
    except ValueError:
        print("Error: Logarithm of population values must be greater than 0.")

def main():
    doubling_time = float(input("Enter the doubling time (in hours): "))
    initial_population = float(input("Enter the initial population: "))
    final_population = float(input("Enter the final population: "))

    generation_time = calculate_generation_time(doubling_time, initial_population, final_population)
    if generation_time:
        print(f"Generation Time: {generation_time:.2f} hours")

if __name__ == "__main__":
    main()

import math

# Constants
c = 299792458  # Speed of light in meters per second

def lorentz_factor(v):
    """
    Calculate the Lorentz factor based on the velocity (v).
    """
    return 1 / math.sqrt(1 - (v**2 / c**2))

def time_dilation(v, t_proper):
    """
    Calculate time dilation based on the velocity (v) and proper time (t_proper).
    Returns the dilated time.
    """
    gamma = lorentz_factor(v)
    dilated_time = gamma * t_proper
    return dilated_time

def main():
    print("Welcome to the Time Dilation Calculator!")
    print("Time dilation is a phenomenon predicted by Einstein's theory of special relativity.")
    print("It occurs when an object moves relative to another at speeds approaching the speed of light.")
    print("This program will calculate the dilated time experienced by a traveler based on their velocity.")

    try:
        # Input velocity as a fraction of the speed of light
        velocity = float(input("\nEnter the velocity of the traveler (as a fraction of the speed of light): "))
        if velocity >= 1:
            raise ValueError("Velocity cannot exceed or equal the speed of light.")
        
        # Input proper time experienced by the traveler
        time_proper = float(input("Enter the proper time experienced by the traveler (in seconds): "))
        if time_proper < 0:
            raise ValueError("Proper time cannot be negative.")

        # Calculate time dilation
        dilated_time = time_dilation(velocity, time_proper)

        # Output results
        print("\nResults:")
        print("Velocity (v): {:.2f}c".format(velocity))
        print("Proper Time (t_proper): {:.2f} seconds".format(time_proper))
        print("Lorentz Factor (γ): {:.5f}".format(lorentz_factor(velocity)))
        print("Dilated Time: {:.5f} seconds".format(dilated_time))

    except ValueError as ve:
        print("\nError:", ve)

if __name__ == "__main__":
    main()

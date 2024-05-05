def calculate_buffer_volume(final_concentration, final_volume, stock_concentration):
    """
    Calculate the volume of stock buffer solution needed for buffer preparation.
    """
    buffer_volume = (final_concentration * final_volume) / stock_concentration
    return buffer_volume

if __name__ == "__main__":
    try:
        # Take input for the final concentration, final volume, and stock concentration
        final_concentration = float(input("Enter the desired final concentration (in mM): "))
        final_volume = float(input("Enter the desired final volume (in mL): "))
        stock_concentration = float(input("Enter the stock concentration (in mM): "))

        # Calculate the volume of stock buffer solution needed
        buffer_volume = calculate_buffer_volume(final_concentration, final_volume, stock_concentration)
        
        # Output the result
        print("Volume of stock buffer solution needed:", buffer_volume, "mL")

    except ValueError:
        print("Invalid input. Please enter numerical values for concentrations and volumes.")
    except ZeroDivisionError:
        print("Error: Stock concentration cannot be zero.")
    except Exception as e:
        print("An unexpected error occurred:", e)

import pandas as pd

def calculate_media_components(final_volume, component_concentrations):
    """
    Calculate the volumes of individual components for tissue culture media preparation.
    """
    # Define the components and their respective concentrations
    components = list(component_concentrations.keys())

    # Calculate the volumes of each component based on its concentration
    volumes = {}
    for component in components:
        concentration = component_concentrations[component]
        volume = (concentration * final_volume) / 100  # Convert concentration to volume
        volumes[component] = volume

    return volumes

if __name__ == "__main__":
    try:
        # Take input for the final volume of the media
        final_volume = float(input("Enter the desired final volume of the media (in mL): "))

        # Define the concentrations of individual components (in percentage)
        component_concentrations = {
            'Component A': 5,
            'Component B': 10,
            'Component C': 15,
            # Add more components as needed
        }

        # Calculate the volumes of individual components
        component_volumes = calculate_media_components(final_volume, component_concentrations)
        
        # Create a DataFrame to display the results
        df = pd.DataFrame.from_dict(component_volumes, orient='index', columns=['Volume (mL)'])
        df.index.name = 'Component'

        # Output the result
        print("Volumes of individual components for tissue culture media preparation:")
        print(df)

    except ValueError:
        print("Invalid input. Please enter a numerical value for the final volume.")
    except Exception as e:
        print("An unexpected error occurred:", e)

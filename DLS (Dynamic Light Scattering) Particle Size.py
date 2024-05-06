import tkinter as tk
from tkinter import ttk
import numpy as np

def dls_particle_size():
    try:
        temperature = float(temperature_entry.get())
        viscosity = float(viscosity_entry.get())
        scattering_angle = float(angle_entry.get())
        laser_wavelength = float(wavelength_entry.get())
        autocorrelation_time = float(autocorrelation_entry.get())

        temperature_kelvin = temperature + 273.15  # Convert Celsius to Kelvin
        viscosity_pascal_sec = viscosity * 0.001    # Convert centipoise to Pascal-second

        particle_size = (laser_wavelength / (2 * np.pi * np.sin(np.radians(scattering_angle / 2)))) * \
                        ((autocorrelation_time * temperature_kelvin) / (3 * viscosity_pascal_sec))

        result_label.config(text=f"Estimated particle size: {particle_size:.2f} nm")
    except ValueError:
        result_label.config(text="Invalid input. Please enter numeric values.")

# Create GUI window
window = tk.Tk()
window.title("DLS Particle Size Calculator")

# Add temperature input field
temperature_label = ttk.Label(window, text="Temperature (°C):")
temperature_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

temperature_entry = ttk.Entry(window)
temperature_entry.grid(row=0, column=1, padx=10, pady=5)

# Add viscosity input field
viscosity_label = ttk.Label(window, text="Viscosity (cP):")
viscosity_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

viscosity_entry = ttk.Entry(window)
viscosity_entry.grid(row=1, column=1, padx=10, pady=5)

# Add scattering angle input field
angle_label = ttk.Label(window, text="Scattering Angle (degrees):")
angle_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

angle_entry = ttk.Entry(window)
angle_entry.grid(row=2, column=1, padx=10, pady=5)

# Add laser wavelength input field
wavelength_label = ttk.Label(window, text="Laser Wavelength (nm):")
wavelength_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)

wavelength_entry = ttk.Entry(window)
wavelength_entry.grid(row=3, column=1, padx=10, pady=5)

# Add autocorrelation time input field
autocorrelation_label = ttk.Label(window, text="Autocorrelation Time (s):")
autocorrelation_label.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)

autocorrelation_entry = ttk.Entry(window)
autocorrelation_entry.grid(row=4, column=1, padx=10, pady=5)

# Add calculate button
calculate_button = ttk.Button(window, text="Calculate", command=dls_particle_size)
calculate_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# Add result label
result_label = ttk.Label(window, text="")
result_label.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

# Run the GUI
window.mainloop()

def calculate_tm(dna_sequence):
    """
    Calculate the melting temperature (Tm) of a DNA sequence using the nearest-neighbor method.
    """
    # Define nearest neighbor thermodynamic parameters (ΔH and ΔS values in kcal/mol and cal/mol/K respectively)
    nn_parameters = {
        'AA/TT': {'dH': -7.9, 'dS': -22.2},
        'AT/TA': {'dH': -7.2, 'dS': -20.4},
        'TA/AT': {'dH': -7.2, 'dS': -21.3},
        'CA/GT': {'dH': -8.5, 'dS': -22.7},
        'GT/CA': {'dH': -8.4, 'dS': -22.4},
        'CT/GA': {'dH': -7.8, 'dS': -21.0},
        'GA/CT': {'dH': -8.2, 'dS': -22.2},
        'CG/GC': {'dH': -10.6, 'dS': -27.2},
        'GC/CG': {'dH': -9.8, 'dS': -24.4},
        'GG/CC': {'dH': -8.0, 'dS': -19.9},
        'CC/GG': {'dH': -8.0, 'dS': -19.9},
        'AC/GT': {'dH': -8.4, 'dS': -22.4},
        'GT/AC': {'dH': -8.4, 'dS': -22.4},
        'AG/CT': {'dH': -7.8, 'dS': -21.0},
        'CT/AG': {'dH': -7.8, 'dS': -21.0},
        'AT/GA': {'dH': -7.2, 'dS': -20.4},
        'GA/AT': {'dH': -7.2, 'dS': -20.4},
        'CT/GT': {'dH': -8.5, 'dS': -22.7},
        'GT/CT': {'dH': -8.5, 'dS': -22.7},
        'TT/AA': {'dH': -7.9, 'dS': -22.2},
        'TG/CA': {'dH': -8.2, 'dS': -22.2},
        'CA/TG': {'dH': -8.2, 'dS': -22.2},
        'CC/GA': {'dH': -8.0, 'dS': -19.9},
        'GA/CC': {'dH': -8.0, 'dS': -19.9},
        'GG/CT': {'dH': -8.0, 'dS': -19.9},
        'CT/GG': {'dH': -8.0, 'dS': -19.9},
        'CG/GT': {'dH': -10.6, 'dS': -27.2},
        'GT/CG': {'dH': -10.6, 'dS': -27.2},
        'AG/TC': {'dH': -7.8, 'dS': -21.0},
        'TC/AG': {'dH': -7.8, 'dS': -21.0},
        'TG/CA': {'dH': -8.4, 'dS': -22.4},
        'CA/TG': {'dH': -8.4, 'dS': -22.4},
        'TG/TA': {'dH': -8.2, 'dS': -22.2},
        'TA/TG': {'dH': -8.2, 'dS': -22.2},
        'TC/GA': {'dH': -8.5, 'dS': -22.7},
        'GA/TC': {'dH': -8.5, 'dS': -22.7},
        'TG/GT': {'dH': -8.4, 'dS': -22.4},
        'GT/TG': {'dH': -8.4, 'dS': -22.4},
        'TT/AT': {'dH': -7.9, 'dS': -22.2},
        'AT/TT': {'dH': -7.9, 'dS': -22.2}
    }

    # Initialize variables for total enthalpy and entropy
    total_dH = 0.0
    total_dS = 0.0

    # Calculate Tm for each pair of adjacent nucleotides
    for i in range(len(dna_sequence) - 1):
        pair = dna_sequence[i:i + 2]
        if pair in nn_parameters:
            total_dH += nn_parameters[pair]['dH']
            total_dS += nn_parameters[pair]['dS']
        else:
            # If no parameters found for the pair, use average values
            total_dH += -1.0
            total_dS += -2.0

    # Calculate Tm using the formula: Tm = (1000 * ΔH) / (ΔS + R * ln(C / 4)) - 273.15
    R = 1.987  # Universal gas constant in cal/mol/K
    C = 1e-6   # Concentration of DNA in mol/L (1 µM)
    Tm = (1000 * total_dH) / (total_dS + R * (C / 4)) - 273.15

    return Tm

# Test the function
dna_sequence = input("Enter DNA sequence: ")
tm = calculate_tm(dna_sequence)
print("Melting Temperature (Tm) of the sequence:", round(tm, 2), "°C")

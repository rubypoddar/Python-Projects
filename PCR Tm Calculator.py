import math

def calculate_tm(sequence, sodium_concentration=50, primer_concentration=0.25):
    """
    Calculate melting temperature (Tm) of a DNA primer sequence.
    Default values for sodium concentration (mM) and primer concentration (µM) are used.
    Returns the Tm in Celsius.
    """
    # Constants for nearest-neighbor thermodynamics
    dH = {'AA': -7.9, 'TT': -7.9, 'AT': -7.2, 'TA': -7.2, 'CA': -8.5, 'TG': -8.5, 'GT': -8.4, 'AC': -8.4,
          'CT': -7.8, 'AG': -7.8, 'GA': -8.2, 'TC': -8.2, 'CG': -10.6, 'GC': -9.8, 'GG': -8.0, 'CC': -8.0}
    dS = {'AA': -22.2, 'TT': -22.2, 'AT': -20.4, 'TA': -21.3, 'CA': -22.7, 'TG': -22.7, 'GT': -22.4, 'AC': -22.4,
          'CT': -21.0, 'AG': -21.0, 'GA': -22.2, 'TC': -22.2, 'CG': -27.2, 'GC': -24.4, 'GG': -19.9, 'CC': -19.9}

    if len(sequence) < 2:
        raise ValueError("Sequence length should be at least 2 nucleotides.")
    
    # Calculate melting temperature (Tm) using nearest-neighbor method
    tm = 0.0
    for i in range(len(sequence) - 1):
        dinucleotide = sequence[i:i+2].upper()
        tm += dH.get(dinucleotide, 0) * 1000 / (dS.get(dinucleotide, 0) + 1.987 * (273.15 + 25))  # in Kelvin
    tm += (1000 * (dH.get(sequence[0].upper(), 0) + dH.get(sequence[-1].upper(), 0))) / (dS.get(sequence[0].upper(), 0) + 1.987 * (273.15 + 25))  # Adjust for first and last nucleotides
    tm += 16.6 * math.log10(primer_concentration)  # Salt adjustment
    tm -= 0.72 * sodium_concentration  # Salt adjustment
    return tm

def validate_sequence(sequence):
    """
    Validate primer sequence.
    Returns True if valid, False otherwise.
    """
    return all(base.upper() in 'ATGC' for base in sequence)

def main():
    print("Welcome to the PCR Tm Calculator!")
    print("This calculator estimates the melting temperature (Tm) of PCR primers using the nearest-neighbor method.")
    
    try:
        # Input primer sequence
        while True:
            primer_sequence = input("Enter primer sequence (e.g., ATGCATGC): ").strip()
            if validate_sequence(primer_sequence):
                break
            print("Invalid primer sequence. Only DNA bases (A, T, G, C) are allowed.")

        # Input sodium concentration (mM)
        while True:
            try:
                sodium_concentration = float(input("Enter sodium concentration (mM, default 50): ") or 50)
                if sodium_concentration >= 0:
                    break
                else:
                    print("Sodium concentration must be a non-negative number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Input primer concentration (µM)
        while True:
            try:
                primer_concentration = float(input("Enter primer concentration (µM, default 0.25): ") or 0.25)
                if primer_concentration > 0:
                    break
                else:
                    print("Primer concentration must be a positive number.")
            except ValueError:
                print("Invalid input. Please enter a number greater than 0.")

        # Calculate Tm
        tm = calculate_tm(primer_sequence, sodium_concentration, primer_concentration)
        print("Estimated Tm:", round(tm, 2), "°C")

    except ValueError as ve:
        print("Error:", ve)

if __name__ == "__main__":
    main()

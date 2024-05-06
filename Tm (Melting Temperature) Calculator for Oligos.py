def calculate_tm(sequence):
    # Constants for nearest-neighbor method
    salt_conc = 0.05  # Salt concentration in Molar (50 mM)
    oligo_conc = 5e-7  # Oligo concentration in Molar (500 nM)
    a_count = sequence.upper().count('A')
    t_count = sequence.upper().count('T')
    c_count = sequence.upper().count('C')
    g_count = sequence.upper().count('G')

    # Melting temperature calculation using nearest-neighbor method
    tm = 64.9 + 41 * (g_count + c_count - 16.4) / (a_count + t_count + g_count + c_count) - 675 / (a_count + t_count + g_count + c_count) + 0.5 * salt_conc * 1000

    return tm

# Get oligonucleotide sequence from user input
sequence = input("Enter the oligonucleotide sequence: ")

# Calculate Tm
tm = calculate_tm(sequence)
print(f"Melting Temperature (Tm) for sequence '{sequence}': {tm:.2f} °C")

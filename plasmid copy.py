def calculate_copy_number(plasmids_per_cell, chromosomes_per_cell):
    """
    Calculate the plasmid copy number based on the ratio of plasmids to chromosomes.
    """
    copy_number = plasmids_per_cell / chromosomes_per_cell
    return copy_number

if __name__ == "__main__":
    # Take input for the number of plasmids per cell and chromosomes per cell
    plasmids_per_cell = float(input("Enter the number of plasmids per cell: "))
    chromosomes_per_cell = float(input("Enter the number of chromosomes per cell: "))

    # Calculate the plasmid copy number
    copy_number = calculate_copy_number(plasmids_per_cell, chromosomes_per_cell)
    print("Plasmid Copy Number:", copy_number)

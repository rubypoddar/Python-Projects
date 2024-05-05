class GibbsFreeEnergyCalculator:
    def __init__(self):
        self.gibbs_free_energy_data = {
            "H2": -50,  # Example Gibbs free energy of formation for H2 (in kJ/mol)
            "O2": 0,    # Example Gibbs free energy of formation for O2 (in kJ/mol)
            "H2O": -200 # Example Gibbs free energy of formation for H2O (in kJ/mol)
            # Add more species and their respective Gibbs free energy of formation values as needed
        }

    def calculate_gibbs_free_energy(self, reactants, products):
        """
        Calculate the Gibbs free energy change for a chemical reaction.
        Args:
        - reactants: Dictionary containing reactants and their coefficients.
        - products: Dictionary containing products and their coefficients.
        Returns:
        - delta_g: Gibbs free energy change for the reaction (in kJ/mol).
        """
        reactants_energy = sum(reactants[species] * self.gibbs_free_energy_data.get(species, 0) for species in reactants)
        products_energy = sum(products[species] * self.gibbs_free_energy_data.get(species, 0) for species in products)
        delta_g = products_energy - reactants_energy
        return delta_g

def get_input():
    reactants = {}
    products = {}

    num_reactants = int(input("Enter the number of reactants: "))
    for _ in range(num_reactants):
        reactant = input("Enter reactant species: ")
        coefficient = int(input("Enter coefficient for {}: ".format(reactant)))
        reactants[reactant] = coefficient

    num_products = int(input("Enter the number of products: "))
    for _ in range(num_products):
        product = input("Enter product species: ")
        coefficient = int(input("Enter coefficient for {}: ".format(product)))
        products[product] = coefficient

    return reactants, products

def main():
    print("Welcome to the Advanced Gibbs Free Energy Calculator!")
    print("This calculator estimates the Gibbs free energy change for a chemical reaction.")

    try:
        # Initialize calculator
        calculator = GibbsFreeEnergyCalculator()

        # Get user input for reactants and products
        reactants, products = get_input()

        # Calculate Gibbs free energy change
        delta_g = calculator.calculate_gibbs_free_energy(reactants, products)

        # Output Gibbs free energy change
        print("\nGibbs Free Energy Change: {:.2f} kJ/mol".format(delta_g))

    except ValueError as ve:
        print("Error:", ve)

if __name__ == "__main__":
    main()

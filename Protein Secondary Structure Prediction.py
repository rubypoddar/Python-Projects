from Bio.PDB import PDBParser
from Bio.PDB.DSSP import DSSP

def predict_secondary_structure(pdb_file):
    # Parse the PDB file
    parser = PDBParser()
    structure = parser.get_structure("protein", pdb_file)
    
    # Calculate secondary structure using DSSP
    model = structure[0]
    dssp = DSSP(model, pdb_file)
    
    # Extract secondary structure information
    secondary_structure = [dssp_residue[2] for dssp_residue in dssp]
    
    return secondary_structure

# Example usage
pdb_file = "example.pdb"  # Replace with the path to your PDB file
secondary_structure = predict_secondary_structure(pdb_file)
print("Predicted Secondary Structure:", secondary_structure)

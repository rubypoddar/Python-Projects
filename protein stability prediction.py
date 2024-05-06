import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function to calculate stability score based on protein sequence
def calculate_stability_score(sequence):
    # Calculate features
    length = len(sequence)
    cysteine_count = sequence.count('C')
    proline_count = sequence.count('P')
    hydrophobic_count = sequence.count('A') + sequence.count('V') + sequence.count('L') + sequence.count('I') + sequence.count('M') + sequence.count('F') + sequence.count('W') + sequence.count('Y')
    
    # Rule-based prediction
    stability_score = 0
    
    # Longer sequences are more stable
    if length > 100:
        stability_score += 1
    
    # Presence of cysteine indicates potential for disulfide bonds
    if cysteine_count >= 2:
        stability_score += 1
        
    # Proline can disrupt secondary structures, making protein less stable
    if proline_count > 0:
        stability_score -= 1
        
    # Hydrophobic residues tend to stabilize protein structures
    if hydrophobic_count >= 5:
        stability_score += 1
    
    return stability_score

# User interface
def main():
    sequence = input("Enter protein sequence: ")
    
    # Calculate stability score
    stability_score = calculate_stability_score(sequence)
    
    # Output stability prediction
    if stability_score > 0:
        print("Predicted Stability: Stable")
    elif stability_score < 0:
        print("Predicted Stability: Unstable")
    else:
        print("Predicted Stability: Neutral")
    
    # 3D Visualization
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = len(sequence)
    y = sequence.count('C')
    z = sequence.count('P')

    ax.scatter(x, y, z, c='r', marker='o')

    ax.set_xlabel('Sequence Length')
    ax.set_ylabel('Cysteine Count')
    ax.set_zlabel('Proline Count')

    plt.show()

if __name__ == "__main__":
    main()

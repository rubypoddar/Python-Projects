# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from Bio.SeqUtils.ProtParam import ProteinAnalysis

# Load dataset
# Replace 'dataset.csv' with the path to your dataset file
dataset = pd.read_csv('dataset.csv')

# Feature Engineering
def extract_features(sequence):
    # Example: Extract amino acid composition
    analysis = ProteinAnalysis(sequence)
    amino_acid_composition = analysis.get_amino_acids_percent()

    # Other feature extraction methods can be added here
    
    return amino_acid_composition

dataset['features'] = dataset['sequence'].apply(extract_features)

# Split dataset into features and target variable
X = np.array(list(dataset['features']))
y = dataset['solubility']

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Function to predict solubility for a given protein sequence
def predict_solubility(sequence):
    features = extract_features(sequence)
    solubility = model.predict([features])[0]
    return solubility

# User interface
def main():
    sequence = input("Enter protein sequence: ")
    solubility = predict_solubility(sequence)
    print(f'Predicted Solubility: {solubility:.2f}')

if __name__ == "__main__":
    main()

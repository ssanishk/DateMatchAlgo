import pandas as pd
import numpy as np
from scipy.optimize import linear_sum_assignment

# Load the Excel file
file_path = '/content/SampleData.xlsx' #Add Excel File
data = pd.read_excel(file_path)

# Example weight dictionary
# Assuming each column represents an attribute
weights = {
    'TypeOfDate': 0.3,
    'Pet':0.1,
    'Movies': 0.2,
    'Weather': 0.1,
    'FreeTime': 0.1,
    'Music': 0.2
}

# Define the scoring matrices based on the image
scoring_matrices = {
    'Pet': {
        ('Dog', 'Cat'): 0.5, ('Cat', 'Dog'): 0.5, ('Dog', 'Dog'): 1,
        ('Cat', 'Cat'): 1
    },
    'Weather': {
        ('Summer', 'Winter'): 0, ('Winter', 'Summer'): 0, ('Summer', 'Summer'): 1,
        ('Winter', 'Winter'): 1
    },
    'TypeOfDate': {
        ('Cafe', 'Cafe'): 1, ('Cafe', 'Outdoor'): 0.25, ('Cafe', 'FineDine'): 0.75,
        ('Outdoor', 'Outdoor'): 1, ('Outdoor', 'FineDine'): 0, ('FineDine', 'FineDine'): 1
    },
    'Movies': {
        ('RomCom', 'RomCom'): 1, ('RomCom', 'Action'): 0, ('RomCom', 'Documentary'): 0.25,
        ('Action', 'Action'): 1, ('Action', 'Documentary'): 0.6, ('Documentary', 'Documentary'): 1
    },
    'FreeTime': {
        ('Netflix/Chill', 'Netflix/Chill'): 1, ('Netflix/Chill', 'ExploreActivities'): 0, ('Netflix/Chill', 'Travel'): 0,
        ('ExploreActivities', 'ExploreActivities'): 1, ('ExploreActivities', 'Travel'): 0.5, ('Travel', 'Travel'): 1
    },
    'Music': {
        ('Classical', 'Classical'): 1, ('Classical', 'Rock'): 0, ('Classical', 'Pop'): 0.25,
        ('Rock', 'Rock'): 1, ('Rock', 'Pop'): 0.5, ('Pop', 'Pop'): 1
    }
}

# Function to calculate the score between two entries based on categorical matching
def calculate_score(entry1, entry2, weights, scoring_matrices):
    score = 0
    for attribute, weight in weights.items():
        value1, value2 = entry1[attribute], entry2[attribute]
        if (value1, value2) in scoring_matrices[attribute]:
            score += weight * scoring_matrices[attribute][(value1, value2)]
        elif (value2, value1) in scoring_matrices[attribute]:
            score += weight * scoring_matrices[attribute][(value2, value1)]
        else:
            score += weight * 0  # No score for unmatched or undefined pairs
    return score

# Create an empty 2D matrix to store scores
n = len(data)
score_matrix = np.zeros((n, n))

# Compare each entry with every other entry
for i in range(n):
    for j in range(n):
        if i != j:
            score_matrix[i][j] = calculate_score(data.iloc[i], data.iloc[j], weights, scoring_matrices)

# Apply the Hungarian algorithm to find the optimal matching
row_ind, col_ind = linear_sum_assignment(-score_matrix)

# Calculate the total maximum score
total_max_score = score_matrix[row_ind, col_ind].sum()

# Create a DataFrame to show the optimal matching and corresponding scores
optimal_matching = pd.DataFrame({
    'Person i': data.iloc[row_ind]['Name'].values,
    'Person j': data.iloc[col_ind]['Name'].values,
    'Score': score_matrix[row_ind, col_ind]
})

# Display the optimal matching and the total maximum score
print("Optimal Matching:")
print(optimal_matching)
print(f"\nTotal Maximum Score: {total_max_score:.2f}")

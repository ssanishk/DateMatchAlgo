## Overview
This Python script implements a Date Matching Algorithm using the Hungarian Algorithm to find the optimal match between individuals based on a set of weighted attributes. The algorithm reads data from an Excel file, assigns scores based on user preferences, and finds the best possible matches that maximize compatibility scores.

## Requirements
- Python 3.x
- pandas (Data manipulation library)
- numpy (Numerical computation library)
- scipy (Scientific computing library, specifically for the 
Hungarian algorithm)

You can install these dependencies by running:

```
pip install pandas numpy scipy
```
## How It Works
1. Data Loading: The script loads an Excel file (Book1.xlsx) containing date preferences for multiple people. Each row represents an individual's preferences across several attributes, such as 'Type of Date,' 'Pet,' 'Movies,' 'Weather,' 'Free Time,' and 'Music.'

2. Weighted Attributes: The algorithm uses a weight dictionary where each attribute is assigned different weights. You can modify the weights to prioritize certain attributes over others.

3. Scoring Matrices: Each attribute has a predefined scoring matrix that assigns a compatibility score between different pairs of attribute values. For example, if two people like the same type of pet, they receive a higher score.

4. Score Calculation: The calculate_score function compares two entries (two people) based on their preferences. The function applies the weights and scoring matrices to compute a compatibility score.

5. Score Matrix: A square matrix is created, where each element represents the compatibility score between two individuals.

6. Hungarian Algorithm: The script applies the Hungarian algorithm (via linear_sum_assignment function) to the negative of the score matrix to find the optimal pairings that maximize compatibility.

## Output: 
The script outputs the optimal matchings (pairs of people) and their respective compatibility scores. It also calculates the total maximum compatibility score.

## How to Run the Script
1. Place your data in an Excel file named Book1.xlsx with the following columns: 'Name,' 'TypeOfDate,' 'Pet,' 'Movies,' 'Weather,' 'FreeTime,' and 'Music.'

2. Modify the file path in the script to point to your Excel file if it's stored elsewhere.

## Customization
1. Weights: You can adjust the weights of each attribute in the weights dictionary.
2. Scoring Matrices: Modify the scoring matrices to fit your specific attribute matching logic.
3. Attributes: Add or remove attributes as needed, ensuring the weights and scoring_matrices dictionaries reflect the changes.

## Potential Contribution

1. More parameters and mapping
2. Alternates to the Hungarian bipartite matching.
3. Adjustments in the weights

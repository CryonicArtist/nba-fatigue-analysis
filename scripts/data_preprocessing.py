import os
import pandas as pd

# Load the raw game data
data_path = '../data/raw/nba_game_data.csv'
games = pd.read_csv(data_path)

# Print column names to verify the actual column names
print("Column Names:")
print(games.columns)

# Display the first few rows of the original data
print("Original Data:")
print(games.head())

# Adjust the list of columns based on the actual column names
# Using the available columns: 'TEAM_ID', 'PTS', 'GAME_ID', 'GAME_DATE', etc.
columns_to_keep = ['GAME_ID', 'GAME_DATE', 'TEAM_ID', 'PTS']  # Adjust based on available columns

# Filter the dataset with the columns you want
games_cleaned = games[columns_to_keep]

# Convert the 'GAME_DATE' to a datetime object
games_cleaned['GAME_DATE'] = pd.to_datetime(games_cleaned['GAME_DATE'])

# Handle any missing values (if applicable)
games_cleaned.dropna(inplace=True)

# Display the cleaned data to verify the changes
print("\nCleaned Data:")
print(games_cleaned.head())

# Define the directory and cleaned data file path
cleaned_data_dir = '../data/cleaned'
os.makedirs(cleaned_data_dir, exist_ok=True)  # Create directory if it doesn't exist
cleaned_data_path = os.path.join(cleaned_data_dir, 'nba_game_data_cleaned.csv')

# Save the cleaned data to a new CSV file
games_cleaned.to_csv(cleaned_data_path, index=False)

print(f"\nCleaned data saved to {cleaned_data_path}")

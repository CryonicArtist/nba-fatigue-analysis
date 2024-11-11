import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

# Load the cleaned data
games_cleaned = pd.read_csv('../data/cleaned/nba_game_data_cleaned.csv')

# Exploratory Data Analysis (EDA)

# Plot distribution of points scored
plt.figure(figsize=(10, 6))
sns.histplot(games_cleaned['PTS'], bins=20, kde=True)
plt.title('Distribution of Points Scored in Games')
plt.xlabel('Points Scored')
plt.ylabel('Frequency')
plt.show()

# Check correlation between minutes played and points scored
plt.figure(figsize=(10, 6))
sns.scatterplot(x=games_cleaned['MIN'], y=games_cleaned['PTS'])
plt.title('Minutes Played vs Points Scored')
plt.xlabel('Minutes Played')
plt.ylabel('Points Scored')
plt.show()

# Feature Engineering

# Create a 'GAME_FATIGUE' feature based on minutes played and points scored
games_cleaned['GAME_FATIGUE'] = games_cleaned['MIN'] * (games_cleaned['PTS'] / games_cleaned['MIN'])

# Calculate rolling average of points scored over the last 5 games for each team
games_cleaned['ROLLING_PTS'] = games_cleaned.groupby('TEAM_ID')['PTS'].rolling(window=5).mean().reset_index(0, drop=True)

# Standardize selected features
scaler = StandardScaler()
features_to_scale = ['MIN', 'PTS', 'GAME_FATIGUE', 'ROLLING_PTS']
games_cleaned[features_to_scale] = scaler.fit_transform(games_cleaned[features_to_scale])

# Save the updated data to a new file
games_cleaned.to_csv('../data/cleaned/nba_game_data_eda_and_features.csv', index=False)

print("EDA and feature engineering complete. Data saved to ../data/cleaned/nba_game_data_eda_and_features.csv")

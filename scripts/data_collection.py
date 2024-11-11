# Import necessary libraries
from nba_api.stats.endpoints import leaguegamefinder
import pandas as pd

# Initialize the LeagueGameFinder for regular season games
gamefinder = leaguegamefinder.LeagueGameFinder(season_type_nullable='Regular Season')

# Retrieve the data as a DataFrame
games = gamefinder.get_data_frames()[0]

# Display the first few rows to verify the data
print(games.head())

# Save the DataFrame to a CSV file in the 'data/raw/' folder
games.to_csv('../data/raw/nba_game_data.csv', index=False)

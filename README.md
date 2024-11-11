#NBA Fatigue Analysis

This project analyzes NBA game data to evaluate player fatigue and performance trends, with the goal of understanding the impact of game schedules on player efficiency. It includes preprocessing, exploratory data analysis (EDA), feature engineering, and potential predictive modeling for player fatigue based on in-game performance data.

Installation

To get started with the NBA Fatigue Analysis project, you'll need to install a few Python libraries. You can set up a virtual environment and install dependencies using the following steps:
1. Clone the Repository

First, clone the project repository to your local machine:

git clone https://github.com/your-username/nba-fatigue-analysis.git
cd nba-fatigue-analysis

2. Set up a Virtual Environment

To avoid version conflicts with other Python projects, it's recommended to create a virtual environment:

python -m venv venv

Activate the virtual environment:

    On Windows:

venv\Scripts\activate

On macOS/Linux:

    source venv/bin/activate

3. Install Dependencies

Install the necessary Python libraries using pip:

pip install -r requirements.txt

If you don't have a requirements.txt yet, you can manually install the required libraries:

pip install pandas numpy matplotlib seaborn scikit-learn

Usage
Step 1: Data Preprocessing

This step involves cleaning and preparing raw NBA game data for analysis. It loads the data, drops missing values, and selects relevant columns.

To run the data preprocessing script, use the following command:

python scripts/data_preprocessing.py

This will:

    Read raw NBA game data (in data/raw/).
    Clean and preprocess the data, focusing on necessary columns like GAME_ID, TEAM_ID, and performance stats.
    Save the cleaned data to data/cleaned/.

Step 2: Exploratory Data Analysis (EDA) & Feature Engineering

This step explores the cleaned data and creates features for further modeling. It includes visualizations, statistical analysis, and generating new features based on the raw data.

Run the EDA and feature engineering script:

python scripts/eda_and_feature_engineering.py

This will:

    Perform visualizations of game performance trends (e.g., scoring, minutes played).
    Create new features related to fatigue (e.g., average points scored, minutes played in the last few games).
    Save the processed data for future use (model training).

Step 3: Model Training (Coming Soon)

Future versions of this project will include a script for training machine learning models to predict player fatigue and performance. This will be done by analyzing the relationship between game data and player efficiency over time.

Run the model training script once it is available:

python scripts/model_training.py

Step 4: Review Results

Once you’ve run the preprocessing and EDA steps, you can review the cleaned data and visualizations. The cleaned data is stored in data/cleaned/, and visualizations will be displayed in your default web browser.
Dependencies

The following Python libraries are required to run the project:

    pandas - For data manipulation and analysis.
    numpy - For numerical operations.
    matplotlib - For creating static, animated, and interactive visualizations.
    seaborn - For statistical data visualization.
    scikit-learn - For machine learning tasks, including preprocessing and scaling.

You can install these libraries manually using:

pip install pandas numpy matplotlib seaborn scikit-learn

Contributing

We welcome contributions! To contribute to the project:

    Fork the repository.
    Create a new branch (git checkout -b feature-branch).
    Make your changes.
    Commit your changes (git commit -m 'Add new feature').
    Push to your branch (git push origin feature-branch).
    Open a pull request to merge your changes.

License

This project is licensed under the MIT License - see the LICENSE file for details.
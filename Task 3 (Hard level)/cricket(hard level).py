import pandas as pd
import re
import matplotlib.pyplot as plt

# Load the cricket data from a CSV file into a pandas DataFrame
df = pd.read_csv('/home/richer/Documents/ShadowFox/dhrumil.csv')

# Define weights for different actions
weights = {
    "CP": 1,  # Clean Picks
    "GT": 1,  # Good Throws
    "C": 3,  # Catches
    "DC": -3,  # Dropped Catches
    "S": 3,  # Stumpings
    "RO": 3,  # Run Outs
    "MR": -2,  # Missed Run Outs
    "DH": 2  # Direct Hits
}

# Extracting numbers from 'Runs' column and converting to integers
df[['Runs_Value', 'Runs_Sign']] = df['Runs'].str.extract(r'(\d+)(\+|-)').fillna(0)
df['Runs_Value'] = df['Runs_Value'].astype(int)
df['Runs'] = df.apply(lambda row: -row['Runs_Value'] if row['Runs_Sign'] == '-' else row['Runs_Value'], axis=1)


# Calculate performance score for each player
def calculate_performance_score(df, weights):
    score_df = df.groupby('Player Name').agg(
        CP=pd.NamedAgg(column='Pick', aggfunc=lambda x: (x == 'Y').sum() * weights['CP']),
        GT=pd.NamedAgg(column='Throw', aggfunc=lambda x: (x == 'Y').sum() * weights['GT']),
        C=pd.NamedAgg(column='Throw', aggfunc=lambda x: (x == 'C').sum() * weights['C']),
        DC=pd.NamedAgg(column='Pick', aggfunc=lambda x: (x == 'DC').sum() * weights['DC']),
        S=pd.NamedAgg(column='Pick', aggfunc=lambda x: (x == 'S').sum() * weights['S']),
        RO=pd.NamedAgg(column='Throw', aggfunc=lambda x: (x == 'RO').sum() * weights['RO']),
        MR=pd.NamedAgg(column='Throw', aggfunc=lambda x: (x == 'MR').sum() * weights['MR']),
        DH=pd.NamedAgg(column='Throw', aggfunc=lambda x: (x == 'DH').sum() * weights['DH']),
        RS=pd.NamedAgg(column='Runs', aggfunc='sum')
    ).reset_index()

    # Calculate Performance Score (PS)
    score_df['PS'] = (
            score_df['CP'] +
            score_df['GT'] +
            score_df['C'] +
            score_df['DC'] +
            score_df['S'] +
            score_df['RO'] +
            score_df['MR'] +
            score_df['DH'] +
            score_df['RS']
    )

    return score_df


# Calculate the performance score
performance_scores = calculate_performance_score(df, weights)

# Print the final DataFrame with calculated Performance Scores
print(performance_scores)

# Plot the top 10 performers
top_performers = performance_scores.nlargest(10, 'PS')

plt.figure(figsize=(12, 8))
plt.barh(top_performers['Player Name'], top_performers['PS'], color='skyblue')
plt.xlabel('Performance Score')
plt.ylabel('Player Name')
plt.title('Top 10 Fielding Performers')
plt.gca().invert_yaxis()
plt.show()

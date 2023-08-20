import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('file.csv')

# Define your list of locations
locations = ['Austria', 'United Kingdom']  # add the rest of your locations here

# Create a new DataFrame with only the rows that match your locations
matched_df = df[df['State'].isin(locations)]

# For each matched row, output the country, tax credit, and eligibility
for index, row in matched_df.iterrows():
    print(f"Country: {row['Countries']}, Tax Credit: {row['Tax credits']}, Eligibility: {row['Eligibility']}")

import pandas as pd

# Read the CSV file
df = pd.read_csv('ScreenCrib Tax Credit Sheet - Sheet1.csv')

most_common_countries = [('United Kingdom', 46), ('Iran', 3), ('Wisconsin', 2)]

# Iterate over each country and print tax credit and eligibility
for country in most_common_countries:
    data = df.loc[df['Country'] == country[0]]
    if not data.empty:
        print(f"Country: {country[0]}")
        print(f"Tax credits: {data['Tax credits'].values[0]}")
        print(f"Eligibility: {data['Eligibility'].values[0]}\n")
    else:
        print(f"No data available for {country[0]}\n")
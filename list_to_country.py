from geopy.geocoders import Nominatim
from collections import Counter
from geopy.exc import GeocoderUnavailable

locations_set = {'Audi', 'Ally Pally', 'TOTTENHAM COURT ROAD', 'LIVING ROOM', 'England', 'GARDEN', 'Portobello', 'Crystal Palace FC', 'Earth', 'AMBULANCE', 'Perseid', 'NORTH END WAY', 'ROYAL LONDON HOSPITAL', 'CHISWICK STATION PLATFORM', 'YouTube', 'United', 'OFF', 'HAMPSTEAD HEATH PONDS', 'Westminster Bridge', 'OUTSIDE PORTISHEAD HOUSE', 'Ladbroke Grove', 'ROYAL LONDON HOSPITAL A', 'Westway', 'Hammersmith', 'THEME PARK', 'REGENT', 'CLIFFS', 'Maps', 'MacDoonald', 'PUB TOILETS', 'Wilmington \nAvenue', 'Kensal Rise', 'Tehran', 'VW', 'BISHOPS AVENUE', 'HAMPSTEAD HEATH', 'Central \nLondon', 'St Tropez', 'PRICE', 'McDonald', 'WEST LONDON', 'CHISWICK STATION', 'FINSBURY PARK TUBE STATION', 'CHISWICK HIGH SCHOOL', 'Waterloo Roundabout', 'Manchester', 'Notting Hill', 'London', 'PORTOBELLO ROAD', 'STREETS', 'MOTORWAY OVERPASS', 'NASSINGTON ROAD', 'Starbucks', 'Wilmington Avenue', 'WHITSTABLE HOUSE TOWER LIFT', 'ERDANG SCHOOL OF DANCE', 'WESTMINSTER BRIDGE', 'LONDON', 'FINSBURY PARK', 'DR GILANI', 'Bishop’s Avenue', 'NORTHERN LINE', 'BURLINGTON LANE', 'Hampstead', 'BRENTFORD', 'Harrow Road', 'LONDON BRIDGE ESCALATOR', 'UNIVERSITY COLLEGE LONDON', 'BT Tower', 'Hampstead Heath', 'Crystal Palace', 'Kentucky', 'BA', 'REGENT’S PARK', 'Kings', 'Iran', 'HAMPSTEAD PERGOLA', 'OVERGROUND TRAIN', 'Subvay', 'PRINTWORKS', 'BEDROOM', 'Regent’s Park', 'Price & Co’s', 'BBC Persia', 'UNIVERSITY COLLEGE', 'CHISWICK SCHOOL', 'Berrrger \nKeeng', 'Camden', 'Thames', 'ROYAL LONDON', 'CEX ELECTRONICS', 'PORTISHEAD HOUSE', 'UCL TUTOR ROOM', 'THE EARTH FROM SPACE'}

# Create a geolocator object to access Nominatim
geolocator = Nominatim(user_agent="myGeocoder")

# List to hold the countries
countries = []

for loc in locations_set:
    try:
        location = geolocator.geocode(loc, timeout=10)  # Increase timeout
        # location = geolocator.geocode(loc)
        if location:
            location_info = geolocator.reverse([location.latitude, location.longitude], exactly_one=True, language='en')
            if 'state' in location_info.raw['address'] and location_info.raw['address']['country_code'] == 'us':
                countries.append(location_info.raw['address']['state'])
            else:
                countries.append(location_info.raw['address']['country'])
        else:
            print(f"No location found for {loc}")
    except GeocoderUnavailable:
        print("The geocoding service is currently unavailable. Please try again later.")

# Now we have a list of countries
country_counts = Counter(countries)
print(countries)
most_common_countries = country_counts.most_common(3)
print(most_common_countries)

# Read the CSV file
# df = pd.read_csv('ScreenCrib Tax Credit Sheet - Sheet1.csv')

# Iterate over each country and print tax credit and eligibility
# for country in most_common_countries:
#     data = df.loc[df['Country'] == country[0]]
#     if not data.empty:
#         print(f"Country: {country[0]}")
#         print(f"Tax credits: {data['Tax credits'].values[0]}")
#         print(f"Eligibility: {data['Eligibility'].values[0]}\n")
#     else:
#         print(f"No data available for {country[0]}\n")
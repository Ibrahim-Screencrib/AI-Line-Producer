import PyPDF2
import spacy
import re

def pdf_to_text(path):
    """Extract text from PDF file"""
    with open(path, 'rb') as file:
        pdf = PyPDF2.PdfReader(file)
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
    return text

text = pdf_to_text(input("Enter the file path: ")) # Enter the file path of the script
with open('output.txt', 'w') as file: 
    file.write(text) # Write the text to a file

def extract_locations(text):
    """Extract locations from text"""
    pattern = r"(INT\.|EXT\.)\s([A-Z\s]*)(- DAY|- NIGHT)?" # Regex pattern to match locations
    matches = re.findall(pattern, text) # Find all matches
    locations = [match[1].strip() for match in matches] # Extract the locations from the matches
    return locations

text = open('output.txt', 'r').read() # Read the text from the file
regex_locations = extract_locations(text) # Extract locations with regex

# Load the Spacy model
nlp = spacy.load('en_core_web_trf')

# Process the script with Spacy
doc = nlp(text)

# Identify the '...' Entities
locations = [ent.text for ent in doc.ents if ent.label_ in ['LOC', 'ORG', 'FAC', 'GPE']] 



# Identify the '...' Entities
other_entities = [ent.text for ent in doc.ents if ent.label_ in ['PERSON', 'NORP', 'PRODUCT', 'EVENT', 'WORK_OF_ART']] 
# optional 'LAW', 'LANGUAGE', 'DATE', 'TIME', 'PERCENT', 'MONEY', 'QUANTITY', 'ORDINAL', 'CARDINAL'

# Convert the lists to sets
locations_set = set(locations)
other_entities_set = set(other_entities)

# convert the regex_locations to a set
regex_locations_set = set(regex_locations)

# all locations - other_entities_set
all_locations = locations_set.union(regex_locations_set) - other_entities_set

# remove all locations that start with a lowercase letter or contain an '@' or start with a '"'
all_locations = {loc for loc in all_locations if loc and len(loc) > 1 and not loc[0].islower() and '@' not in loc and not loc.startswith('"') and '(' not in loc and ')' not in loc and '?' not in loc}

# Find the common elements
#common_elements = locations_set.intersection(other_entities_set)

print(all_locations)


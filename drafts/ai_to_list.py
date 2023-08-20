import PyPDF2
import re
import json

def pdf_to_text(path):
    with open(path, 'rb') as file:
        pdf = PyPDF2.PdfReader(file)
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
    return text

text = pdf_to_text(input("Enter the file path: "))
with open('output.txt', 'w') as file:
    file.write(text)

def extract_locations(text):
    pattern = r"(INT\.|EXT\.)\s([A-Z\s]*)(- DAY|- NIGHT)?"
    matches = re.findall(pattern, text)
    locations = [match[1].strip() for match in matches]
    return locations

text = open('output.txt', 'r').read()
locations = extract_locations(text)

def output_to_json(data, file_name):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)

output_to_json(locations, 'locations.json')
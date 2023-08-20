import PyPDF2
import spacy


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

# Load the Spacy model
nlp = spacy.load('en_core_web_sm')

# Read the script from the .txt file
with open('output.txt', 'r') as file:
    script = file.read()

# Process the script with Spacy
doc = nlp(script)

# Identify the locations
locations = [ent.text for ent in doc.ents if ent.label_ == 'GPE'] # GPE is the label for locations

# Print the locations
for location in locations:
    print(location)
# DAY 7 NOTES

### AI tool top-down

* The tool will extract all locations from movie scripts
    * this can be done in a couple ways:
        * regex and pretrained NLP models
            * After some cleaning these are fairly accurate
            * ok for MVP?
        * our own trained model
            * this needs a labeled dataset of movie scripts - toloka.ai
            * this will be the most accurate method of getting locations

* with a list of locations from the script the tool will generate a couple of countries/states that would best match the correlation between the list of locations that must be included in the script
    * if there is no specific location the tool will output the most cost effective location of filming
        * Ex. "Kill Your Lover" - no location so it suggests the most optimal filming location that would be of most convienience to the producer

* With a list of countries/states it references a manually updated csv file that has countries/states listed with their film tax credit rates, elegibility for film tax credits, and links to more information to match it with the locations on the list and suggest the corresponding information to the user.
    * if there is an empty list it gives the country/state with the highest tax credit rate, and associated information.



# Find out safest food products
## OpenClassrooms - my 5th project for OC Python Path

![alt][text](https://static.openfoodfacts.org/images/misc/openfoodfacts-logo-fr-178x150.png "OpenFoodFacts Logo")

This app is about finding safest, healthy products by using the french database OpenFoodFacts.

### Installing:

1. Pull master branch and put all files in the same folder
2. Please update `CREDENTIALS` in configuration.py has needed
3. Install python3.7
4. Install pipenv
5. run "pipenv install"
6. run "pipenv shell"
7. run "python3 -m main" (Linux) or "py -m main" (Windows)47.

### How it works:

1. This app pull products from OFF API (Categories chosen in `CATEGORIES_TO_SCRAPE`)
2. Please be patient, regarding how much data you've asked, it could take a few seconds
3. Data are stored in local database
4. Menu in CLI mode lets user choose a product to fine a healthier substitute
5. User can record his choice and find out later which substitute has been found given a product

***

If you like my work, please consider staring my repo :)
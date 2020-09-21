import pandas as pd
data = pd.read_csv('https://raw.githubusercontent.com/mayank2567/intership-test/master/input/main.csv')
booleans = []
for country in data.COUNTRY:
    if country == "USA (CA)":
        booleans.append(True)
    else:
        booleans.append(False)

filtered_country = data[country_name]
filtered_country.to_csv('filteredCountry.csv')
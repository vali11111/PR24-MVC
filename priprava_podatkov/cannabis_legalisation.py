from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import random
import csv
import os

states_csv_path = r"C:\Users\Uporabnik\Desktop\FAKS\3. LETNIK\2. SEMESTER\PR\seminarska_podatki\states.csv"

# Slovar za shranjevanje imen držav in njihovih kod
state_data = {}

# Preberi vsebino CSV datoteke z državami in njihovimi kodi
with open(states_csv_path, mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Preskoči glavo
    for row in reader:
        state, code = row
        state_data[code.strip()] = state.strip()

userAgents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.3	32.54",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3.1 Safari/605.1.1	20.51",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.	14.24",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.3	10.17",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.3	6.78",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.1	5.42",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.1	4.92",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.3	2.71",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.	1.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 OPR/108.0.0.	0.68",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.	0.68"
]

url = "https://mjbizdaily.com/map-of-us-marijuana-legalization-by-state/"
data_request = requests.get("https://mjbizdaily.com/map-of-us-marijuana-legalization-by-state/", headers={"User-Agent": random.choice(userAgents)})

html_content = data_request.text

soup = BeautifulSoup(html_content, 'html.parser')

# Find the table
table = soup.find('table', {'id': 'tablepress-26'})

# Extract data from the table
data = []
headers = [header.get_text() for header in table.find_all('th')]
data.append(headers)

for row in table.find_all('tr')[1:]:
    row_data = [cell.get_text() for cell in row.find_all('td')]
    data.append(row_data)

# Ime izhodne mape
output_folder = r"podatki"
# Ime izhodne CSV datoteke
output_csv_file = os.path.join(output_folder, "legalization.csv")



# Preveri, ali se ime države ujema z imenom na spletni strani
filtered_data = []
for row in data[1:]:
    state_name = row[0]
    if state_name in state_data.values():
        state_code = list(state_data.keys())[list(state_data.values()).index(state_name)]
        filtered_data.append([state_name, state_code] + row[1:])

# Zapiši filtrirane podatke v CSV datoteko
with open(output_csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Dodaj header
    writer.writerow(["State", "Code"] + headers)
    writer.writerows(filtered_data)

print(f"Filtrirani podatki so bili shranjeni v {output_csv_file}")

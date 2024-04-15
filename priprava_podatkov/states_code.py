from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import random
import csv
import os


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

url = "https://www.lovetoknow.com/parenting/kids/list-all-50-states-abbreviations"
data_request = requests.get(url, headers={"User-Agent": random.choice(userAgents)})

html_content = data_request.text
soup = BeautifulSoup(html_content, 'html.parser')


# Poišči naslov seznama
list_title = soup.find('p', string=lambda
    text: text and 'Here is a list of the 50 states and their proper abbreviations:' in text)

# Preveri, ali je naslov najden
if list_title:
    print("Naslov seznama je bil najden.")

    # Poišči naslednji seznam
    state_list = list_title.find_next_sibling('ol')

    # Preveri, ali je seznam najden
    if state_list:
        print("Seznam držav je bil najden.")

        # Določi pot do mape za shranjevanje CSV datoteke
        save_path = r'podatki'
        csv_file_path = os.path.join(save_path, 'states.csv')

        # Odpremo CSV datoteko za pisanje
        with open(csv_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)

            # Dodamo glavo CSV datoteke
            writer.writerow(['State', 'Code'])

            # Zapišemo vsebino seznama v CSV datoteko
            for item in state_list.find_all('li'):
                state, code = item.text.split(': ')
                writer.writerow([state.strip(), code.strip()])

            print("Vsebina seznama je bila shranjena v datoteko states.csv.")
    else:
        print("Seznam držav ni bil najden.")
else:
    print("Naslov seznama ni bil najden.")


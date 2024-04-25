from bs4 import BeautifulSoup
import requests
import random
import csv
import os

# Pot do CSV datoteke z državami in njihovimi kodami
states_csv_path = r"podatki\states.csv"

# Pot do nove CSV datoteke za shranjevanje podatkov
output_csv_path = r"podatki/population.csv"

# Slovar za shranjevanje imen držav in njihovih kod
state_data = {}

# Preberi vsebino CSV datoteke z državami in njihovimi kodi
with open(states_csv_path, mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Preskoči glavo
    for row in reader:
        state, code = row
        state_data[code.strip()] = state.strip()


# Uporabniški agenti
userAgents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3.1 Safari/605.1.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.1",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 OPR/108.0.0.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0"
]

# Nastavi uporabniški agent za zahtevek
headers = {"User-Agent": random.choice(userAgents)}

# Nastavitev začetnega leta in končnega leta
start_year = 2022
end_year = 2000

# Odpiranje CSV datoteke za pisanje
with open(output_csv_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Zapisovanje glave CSV datoteke
    writer.writerow(["Year","Code", "State", "Value"])

    # Zanka za pridobivanje podatkov za vsako leto
    for year in range(start_year, end_year - 1, -1):
        # Sestavi URL za zahtevek
        url = f"https://fred.stlouisfed.org/release/tables?rid=118&eid=259194&od={year}-01-01#"

        # Pošlji zahtevek za HTML vsebino
        data_request = requests.get(url, headers=headers)

        # Preveri, če je zahteva uspešna
        if data_request.status_code == 200:
            html_content = data_request.text

            # Uporabi BeautifulSoup za analizo HTML-ja
            soup = BeautifulSoup(html_content, 'html.parser')

            # Poišči tabelo po razredu 'table-responsive'
            table = soup.find('div', class_='table-responsive').find('table')

            # Izlušči vrstice iz tabele
            rows = table.find_all('tr')

            # Izlušči ime države in številke iz tabele
            for row in rows:
                cols = row.find_all('td')
                cols = [col.text.strip() for col in cols]
                # Če obstajajo stolpci
                if cols:
                    # Preveri, če prvi stolpec vsebuje kodo države
                    if cols[0] in state_data:
                        # Če je koda države, dodaj ime države pred številkami
                        cols.insert(0, state_data[cols[0]])
                    # Če obstajajo spani z imeni držav
                    span = row.find('span', class_='fred-rls-elm-nm')
                    if span:
                        span_text = span.text.strip()
                        cols[0] = span_text
                    # Odstrani prazen stolpec
                    cols = [col for col in cols if col]

                    if cols[0] in state_data.values():
                        code = [k for k, v in state_data.items() if v == cols[0]][0]

                        writer.writerow([year, code, cols[0], cols[1]])

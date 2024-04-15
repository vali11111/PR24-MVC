import pandas as pd
import os
import csv

states_csv_path = r"C:\Users\Uporabnik\Desktop\FAKS\3. LETNIK\2. SEMESTER\PR\seminarska_podatki\states.csv"

# Seznam za shranjevanje samo kod držav
state_codes = []

# Preberi samo kode držav iz CSV datoteke
with open(states_csv_path, mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Preskoči glavo
    for row in reader:
        state, code = row
        state_codes.append(code.strip())


# Preberi vse liste v Excel datotek
excel_file_path = r"priprava_podatkov\originalni_podatki\Unemployment.xlsx"
df = pd.read_excel(excel_file_path, skiprows=4)  # preskoči prvih nekaj vrstic

# Ustvari seznam stolpcev za vsako leto od 2000 do 2022
years = range(2000, 2023)
employment_columns = [f'Civilian_labor_force_{year}' for year in years] + \
                     [f'Employed_{year}' for year in years] + \
                     [f'Unemployed_{year}' for year in years] + \
                     [f'Unemployment_rate_{year}' for year in years]

# Izberi samo stolpce, ki se nanašajo na zaposlenost in brezposelnost za vsako leto
filtered_df = df[['FIPS_Code', 'State', 'Area_Name'] + employment_columns]

# Pripravi prazno DataFrame za shranjevanje podatkov
final_data = pd.DataFrame(columns=['Year', 'FIPS_Code', 'State', 'Area_Name', 'Civilian_labor_force', 'Employed', 'Unemployed', 'Unemployment_rate'])

# Izpiši podatke za vsako leto od 2000 do 2022
for year in years:
    year_columns = [f'Civilian_labor_force_{year}', f'Employed_{year}', f'Unemployed_{year}', f'Unemployment_rate_{year}']
    data_year = filtered_df[['FIPS_Code', 'State', 'Area_Name'] + year_columns]
    data_year_no_comma = data_year[~data_year['Area_Name'].astype(str).str.contains(',')]


    if not data_year_no_comma.empty:
        data_year_no_comma_unique = data_year_no_comma.drop_duplicates(subset=['Area_Name'])
        data_year_no_comma_unique.columns = ['FIPS_Code', 'State', 'Area_Name', 'Civilian_labor_force', 'Employed', 'Unemployed', 'Unemployment_rate']
        data_year_no_comma_unique = data_year_no_comma_unique.copy()
        data_year_no_comma_unique.loc[:, 'Year'] = year
        final_data = pd.concat([final_data, data_year_no_comma_unique], ignore_index=True)

# Shranjevanje podatkov v CSV datoteko
all_states = final_data['State'].unique()
i = 0
for state in all_states:
    #print(state)
    i += 1

print("Seznam kod držav:")
print(len(state_codes))


user_folder = r'podatki'

# Določite ime datoteke
file_name = 'unemployment.csv'

filtered_data = []

# Preveri vsako državo v finalnih podatkih
for state in final_data['State']:
    if state in state_codes or state == 'US':
        # Če je država v seznamu state_codes ali pa je enaka "USA",
        # jo dodaj v filtrirane podatke
        filtered_data.append(state)

# Pretvori filtrirane podatke v DataFrame
unemployment_data_filtered = final_data[final_data['State'].isin(filtered_data)]

# Shranjevanje filtriranih podatkov v CSV datoteko
unemployment_data_filtered.to_csv(os.path.join(user_folder, file_name), index=False)

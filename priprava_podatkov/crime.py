import csv
from collections import defaultdict

# Function to load and clean the data
def load_data(file_path):
    cleaned_data = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Filter data for years after 2000
            if int(row['Year']) >= 2000:
                cleaned_data.append(row)
    return cleaned_data

# Load the cleaned data
file_path = "priprava_podatkov\originalni_podatki\state_crime.csv"
collected_data = load_data(file_path)
output_csv_path = r"podatki/crime.csv"
states_csv_path = r"C:\Users\Uporabnik\Desktop\FAKS\3. LETNIK\2. SEMESTER\PR\seminarska_podatki\states.csv"

def get_state_code(state_name, states_csv_path):
    with open(states_csv_path, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Preskoči glavo
        for row in reader:
            if row[0].lower() == state_name.lower():
                return row[1].strip()
    return None 


print(get_state_code("California",states_csv_path))
# Function to analyze the data
def analyze_data(collected_data):
    # Initialize dictionaries to store total crimes per year and most common crime per state
    crimes_per_year = defaultdict(int)
    most_common_crime_per_state = {}

    # Iterate through the collected data
    for data in collected_data:
        state = data['State']
        year = data['Year']
        total_property_crimes = int(data['Data.Totals.Property.All'])
        total_violent_crimes = int(data['Data.Totals.Violent.All'])

        # Find the most common property crime for the current state
        property_crimes = {
            'Burglary': int(data['Data.Totals.Property.Burglary']),
            'Larceny': int(data['Data.Totals.Property.Larceny']),
            'Motor': int(data['Data.Totals.Property.Motor'])
        }
        most_common_property_crime = max(property_crimes, key=property_crimes.get)
        property_crime_count = sum(property_crimes.values())

        # Find the most common violent crime for the current state
        violent_crimes = {
            'Assault': int(data['Data.Totals.Violent.Assault']),
            'Murder': int(data['Data.Totals.Violent.Murder']),
            'Rape': int(data['Data.Totals.Violent.Rape']),
            'Robbery': int(data['Data.Totals.Violent.Robbery'])
        }
        most_common_violent_crime = max(violent_crimes, key=violent_crimes.get)
        violent_crime_count = sum(violent_crimes.values())

        # Calculate the total number of crimes
        total_crimes = total_property_crimes + total_violent_crimes

        # Store the most common crimes for the current state
        most_common_crime_per_state[(state, year)] = {
            'State': state,
            'Year': year,
            'Code': get_state_code(state,states_csv_path),
            'Total Crimes': total_crimes,
            'Top Property Crime': most_common_property_crime,
            'Burglary': property_crimes['Burglary'],
            'Larceny': property_crimes['Larceny'],
            'Motor': property_crimes['Motor'],
            'Total Property Crime Count': property_crime_count,
            'Top Violent Crime': most_common_violent_crime,
            'Assault': violent_crimes['Assault'],
            'Murder': violent_crimes['Murder'],
            'Rape': violent_crimes['Rape'],
            'Robbery': violent_crimes['Robbery'],
            'Total Violent Crime Count': violent_crime_count
        }

        # Increment the total crimes for the current year
        crimes_per_year[(state, year)] += total_crimes

    # Print the statistics for each year and state
    with open(output_csv_path, mode='w') as file:
        file.write("State,Code,Year,Total Crimes,Total Property Crime Count,Burglary,Larceny,Motor,Total Violent Crime Count,Assault,Murder,Rape,Robbery\n")
        for (state, year), crimes in most_common_crime_per_state.items():
            file.write(f"{crimes['State']},{crimes['Code']},{crimes['Year']},{crimes['Total Crimes']},{crimes['Total Property Crime Count']},{crimes['Burglary']},{crimes['Larceny']},{crimes['Motor']},{crimes['Total Violent Crime Count']},{crimes['Assault']},{crimes['Murder']},{crimes['Rape']},{crimes['Robbery']}\n")
# Call the function to analyze the data
analyze_data(collected_data)
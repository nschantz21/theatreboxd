import requests
from bs4 import BeautifulSoup
import pandas as pd

# Replace this URL with the URL of the webpage you want to scrape
url = 'https://www.ibdb.com/broadway-production/cats-4186#OpeningNightCast'
div_id = "Replacements"

# Make a GET request to the webpage
response = requests.get(url)

df_list = []

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Locate the <div> containing the table (replace 'div_id' with the actual ID or class)
    div_table = soup.find('div', {'id': div_id})
    #print(div_table)

    if div_table:
        # Extract data from the table within the <div>
        table_rows = div_table.find_all('div', {'class': 'row'})  # Adjust based on your HTML structure


        # Extracting data and creating a list of dictionaries
        data = []
        for row in table_rows:
            cells = row.find_all('div', {'class': 'col m4 s12'})  # Adjust based on your HTML structure
            row_data = [cell.text.strip() for cell in cells]
            data.append(row_data)

        #print(data)
        # Convert the list of dictionaries into a Pandas DataFrame
        df = pd.DataFrame([d for d in data if d], columns=["Column1", "Column2", "Column3"])  # Adjust column names

        # Print or manipulate the DataFrame as needed
        #print(df)
        df_list.append(df)

    else:
        print("Table not found within the specified <div>.")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

df_mega_list = pd.concat(df_list)
df_mega_list.to_csv("div_table.csv", index=False)
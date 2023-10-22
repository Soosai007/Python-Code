import pandas as pd 
import requests 
from bs4 import BeautifulSoup

table_class="wikitable sortable jquery-tablesorter"
response=requests.get("https://en.wikipedia.org/wiki/List_of_cities_in_India_by_population")
print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable = soup.find('table',{'class':"wikitable sortable"})
#print(indiatable)


df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])



data = df.drop(["Ref"], axis=1)
data.rename(columns={"State or union territory": "State","Population (2001)[3][a]": "Population"})
print(data.head())

# creating the DataFrame
marks_data = pd.DataFrame(data)

# determining the name of the file
file_name = 'MarksData.xlsx'

# saving the excel
marks_data.to_excel(file_name)
print('DataFrame is written to Excel File successfully.')


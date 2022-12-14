
import requests
import json 
import pandas as pd
import csv

''' CA COVID'''
url = 'https://api.covidtracking.com/v1/states/ca/current.json'
response = requests.get(url)
content = response.text
contents_list = json.loads(content)

print(contents_list['positive'], contents_list['death'])


'''LA Covid'''
url = 'http://publichealth.lacounty.gov/media/Coronavirus/locations.htm'
html = requests.get(url).content
df_list = pd.read_html(html)
df_1 = df_list[0]

df = df_list[1]
df.to_csv('my_data.csv')
df_1.to_csv('my_data_1.csv')

'''Beginning of the CSV Conversion'''

with open('my_data_1.csv', newline='') as f:
    reader = csv.reader(f)
    LA_data = list(reader)

with open('my_data.csv', newline='') as f:
    reader = csv.reader(f)
    LC_data = list(reader)


print(LA_data[1][2], LA_data[2][2])
print(LC_data[39][1], LC_data[39][2])

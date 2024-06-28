import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests

# Fetching data from the website
page = requests.get('https://pogoda.interia.pl/prognoza-dlugoterminowa-warszawa,cId,36917')
soup = BeautifulSoup(page.text, 'html.parser')

# Parsing the relevant data
days = soup.find_all("span", class_="day")
dates = soup.find_all("span", class_="date")
temps = soup.find_all("span", class_="weather-forecast-longterm-list-entry-forecast-temp")

# Prompt user for number of days forecast
num = int(input("prognoza na <tu podaj ilosc dni>: "))

# Preparing data for the plot
dev_x = []
dev_y = []
TMP_x = []
weekdays = []

# Extracting and cleaning the data
for date, temp, day in zip(dates, temps, days):
    if len(TMP_x) < num:
        TMP_x.append(date.text)
        temp_value = ''.join(filter(str.isdigit, temp.text.split()[0]))
        dev_y.append(int(temp_value))
        weekdays.append(day.text)

# Handling the x-axis labels
if num < 7:
    dev_x = ["dzisiaj", "jutro"] + weekdays[2:num]
else:
    dev_x = ["dzisiaj", "jutro"] + weekdays[2:7] + TMP_x[7:num]

# Plotting
plt.title(f"Pogoda na Warszawę dla {TMP_x[0]} - {TMP_x[num-1]}")
plt.plot(dev_x, dev_y, marker='o')
plt.xlabel("Data")
plt.ylabel("°C", rotation=0, labelpad=10)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

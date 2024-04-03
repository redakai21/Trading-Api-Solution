import requests
import matplotlib.pyplot as plt
import pandas as pd

endpoint = "https://api.tradingeconomics.com/markets/historical"

api_key = "3025412754ba456:d6raixklaeuejqv"

def get_time_series(country, indicator):
    params = {
        'country': country,
        'indicator': indicator,
        'c': api_key
    }
    response = requests.get(endpoint, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code)
        return None

def plot_time_series(country, indicator, data):
    df = pd.DataFrame(data)
    df['Date'] = pd.to_datetime(df['date'])
    plt.plot(df['Date'], df['value'])
    plt.xlabel('Date')
    plt.ylabel(indicator)
    plt.title(f'{indicator} in {country}')
    plt.show()

if __name__ == "__main__":
    country = input("Enter a country: ")
    indicator = input("Enter an indicator: ")
    time_series_data = get_time_series(country, indicator)
    if time_series_data:
        plot_time_series(country, indicator, time_series_data)
    else:
        print("No data found for the selected country and indicator.")

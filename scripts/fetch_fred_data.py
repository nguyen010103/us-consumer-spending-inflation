import requests
from dotenv import load_dotenv
import os 
import pandas as pd

load_dotenv(dotenv_path = '/Users/anhnguyendo/Documents/Python machine learning/US CPI project/us-consumer-spending-inflation/.env')

FRED_API_KEY = os.getenv("FRED_API_KEY")
BASE_URL = "https://api.stlouisfed.org/fred/series/observations"

def fetch_fred_series(series_id, start_date="2010-01-01"):
    params = {
        "series_id": series_id,
        "api_key": FRED_API_KEY,
        "file_type": "json",
        "observation_start": start_date,
    }
    response = requests.get(BASE_URL, params=params)
    
    # Debugging help
    print("Status Code:", response.status_code)
    data = response.json()
    print("API Response:", data)

    if "observations" not in data:
        print("No observations found.")
        return []

    return data["observations"]

if __name__ == "__main__":
    series_id = "PCE"  # Example: Personal Consumption Expenditures
    observations = fetch_fred_series(series_id)
    print(f"Fetched {len(observations)} data points.")

def fetch_and_save_series(series_list, start_date = '2010-01-01', out_dir = 'data/raw'):
    for series in series_list:
        print(f'Fetching series: {series}')
        data = fetch_fred_series(series, start_date)

        if not data:
            print(f'Skipping series: {series}')
        
        #safe as csv
        df = pd.DataFrame(data)
        df.to_csv(f'{out_dir}/{series}.csv', index=False)
        print(f'Saved to: {out_dir}/{series}.csv')

if __name__ == "__main__":
    import pandas as pd
    os.makedirs("data/raw", exist_ok=True)

    series_to_fetch = ["PCE", "CPIAUCSL", "CPIENGSL", "CPIFABSL", "CPIHOSSL", "PCEPILFE"]
    fetch_and_save_series(series_to_fetch)



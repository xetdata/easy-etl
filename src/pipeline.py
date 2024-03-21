import os
import requests
import pandas as pd

def extract_and_transform():
    """
    Fetch and process air quality measurements from the OpenAQ API.

    Returns
    -------
    df : pandas.DataFrame or None
        Dataframe containing the fetched measurements, or None if no data is fetched.
    """
    
    # API URL
    api_url = "https://api.openaq.org/v2/measurements"
    
    # Define the query parameters to API
    params = {
        "location_id": "1938", # Seattle, WA
        "parameter": ["pressure", "temperature", "um003", "um025", "um010", "pm10", "um100", "pm1", "um005", "humidity", "um050", "pm25"],
        "limit": 9000,
    }
    
    try:
        # Make the GET request
        response = requests.get(api_url, params=params, timeout=120)
        response.raise_for_status()  # Raise exception for HTTP errors
        
        if response.status_code == 200:
            data = response.json()
            output = pd.json_normalize(data['results'])
            df = pd.DataFrame(output)
            
            if df.empty:
                print("Extracted dataframe is empty. No data to load.")
                return None

            df['date.utc'] = pd.to_datetime(df['date.utc'], errors='coerce')
            df['date.local'] = df['date.utc'].dt.tz_convert('America/Los_Angeles')
            df['date.local'] = df['date.local'].dt.tz_localize(None)
            df = df[df['value'] > 0.0]
            
            return df

    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("Error: Something Else", err)


if __name__ == "__main__":
    df = extract_and_transform()

    # save the data in the data directory
    data_directory = os.path.join(os.getcwd(), "data")
    if not os.path.exists(data_directory):
        os.makedirs(data_directory)

    data_file = os.path.join(data_directory, "air_data.csv")

    df.to_csv(data_file)


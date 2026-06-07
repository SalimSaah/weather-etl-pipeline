import requests

def extract_weather_data() -> dict:

    """
    Performs the extraction of daily weather data from the Open-Meteo API.
    The data is returned in a raw format (JSON) to be processed by the transformation script.
    It focuses on temperature and precipitation metrics.

    Args: 
        None.

    Returns: 
        dict: A dictionary containing time-series data for the requested variables.

    """

    # Log the start of the ingestion process
    print("Beginning weather data extraction...")

    # Open-Meteo REST API Endpoint.
    # This service is chosen for its high availability and because it does not
    # require an API Key for development/testing purposes.
    url = "https://api.open-meteo.com/v1/forecast"

    # We extract max/min temperatures (Celsius) and total precipitation (mm).
    # Apparent temperature is included to analyze 'thermal sensation' fluctuations.
    parameters = {
        "latitude": 4.6097,
        "longitude": -74.0817,
        # We include
        "daily": ["temperature_2m_max", 
                  "temperature_2m_min", 
                  "precipitation_sum", 
                  "apparent_temperature_max", 
                  "apparent_temperature_min"
        ],
        "timezone": "America/Bogota"
    }
    
    # Request data from the provider
    response = requests.get(url, params=parameters)

    # Verify the integrity of the HTTP transmission
    if response.status_code == 200:
        # Return only the 'daily' node which contains the relevant time-series data
        return response.json()['daily']
    else:
        # Raise an exception to allow the orchestrator (Airflow) to detect
        # the failure and trigger a retry attempt.
        raise Exception(f"API request failed with status code: {response.status_code}")
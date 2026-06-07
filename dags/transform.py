import pandas as pd

def transforming_data(raw_data) -> pd.DataFrame:
    """
    Standardizes and cleanses the weather data received from the API.

    Args:
        raw_data (dict): Dictionary containing raw weather metrics from the API.

    Returns:
        pd.DataFrame: A cleaned DataFrame with standardized column names and types.
    """

    # Log the start of the transforming process
    print("Beginning data transformation...")

    # Convert the raw dictionary into a pandas DataFrame format
    df = pd.DataFrame(raw_data)
    
    # Rename columns to follow a more consistent and straightforward naming convention
    # This improves readability for downstream analysis or database storage
    df.rename(columns={
        'temperature_2m_max': 'temp_max',
        'temperature_2m_min': 'temp_min',
        'apparent_temperature_max': 'apparent_temp_max',
        'apparent_temperature_min': 'apparent_temp_min',
        'precipitation_sum': 'precipitation'
    })
    
    #Return the processed dataframe object
    return df


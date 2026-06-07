"""
Main entry point for the Weather ETL Pipeline.
This script orchestrates the sequential execution of the Extract,
Transform, and Load modules.
"""

from extract import extract_weather_data
from transform import transforming_data
from load import load_data

def run_etl():
    """
    Orchestrates the ETL process.
    It captures data from the API, processes it into a tabular format,
    and persists it into the database.
    """
    try:
        # Step 1: Extraction
        # Fetches raw weather data from the external REST API
        raw_data = extract_weather_data()
        
        # Step 2: Transformation
        #Converts raw JSON-like data into a structured pandas DataFrame
        clean_df = transforming_data(raw_data)
        
        # Step 3: Loading
        # Ingests the structured data into the PosgreSQL destination table
        load_data(clean_df)
        
        print("ETL Pipeline executed successfully.")
        
    except Exception as e:
        #Centralized Error Handling:
        # If any step fails, the error is caught here to provide a
        # clear message and stop the downstream execution.
        print(f"Pipeline failed during execution: {e}")
        # Re-raise the exception so the orchestrator (Airflow) knows it failed
        raise

if __name__ == "__main__":
    # This block ensures the pipeline only runs if the script is executed directly.
    # It prevents accidental execution if the script is imported as a module.
    run_etl()
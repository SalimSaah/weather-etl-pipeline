import pandas as pd
from sqlalchemy import create_engine

def load_data(df: pd.DataFrame) -> None:
    """
    Ingests the processed DataFrame into the PostgreSQL database.
    
    Args: 
        df (pd.DataFrame): Cleaned weather data with standardized schema.

    Returns:
        None
    """

    # Log the start of the ingestion process
    print("Beginning PostgreSQL data ingestion...")

    # Connection string for the PostgreSQL instance.
    # We use 'host.docker.internal' to allow the Airflow container
    # to communicate with the database container on the host machine.
    connection_string = "postgresql://usuario_etl:password123@host.docker.internal:5433/clima_db"

    
    # Create the SQLAlchemy engine to manage database communications
    engine = create_engine(connection_string)
    
    # Load data into the target variable.
    # We use 'append' to preserve historical data across different runs.
    #'index=False' prevents pandas from creating a redundant ID column.
    try:
        df.to_sql('daily_weather_bogota', con=engine, if_exists='append', index=False)
        print("Data ingestion was successful!")
    except Exception as e:
        print(f"Error during database ingestion: {e}")
        raise
    
    


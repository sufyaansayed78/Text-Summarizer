from src.textsummarizer.logging import logger
from src.textsummarizer.pipeline.data_ingestion_pipeline import DataIngestionPipeline   
logger.info("Starting the main application...")

try :
    data_ingestion = DataIngestionPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info("Data ingestion completed successfully.")
except Exception as e:
    logger.exception(f"An error occurred in the main application: {e}")

















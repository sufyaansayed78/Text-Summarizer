from src.textsummarizer.config.configuration import ConfigurationManager
from src.textsummarizer.components.data_ingestion import DataIngestion
class DataIngestionPipeline:
    def __init__(self):
        pass
    def initiate_data_ingestion(self):
        data_ingestion_config = ConfigurationManager().get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)    
        
from src.textsummarizer.config.configuration import ConfigurationManager
from src.textsummarizer.components.data_transformation import DataTrasnformation
from pathlib import Path




class DataTransformationPipeline():
    def __init__(self):
        
        pass
    def initiate_data_transformation(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTrasnformation(config = data_transformation_config)   
        data_transformation.convert()









from src.textsummarizer.utils.common import read_yaml, create_directories
from src.textsummarizer.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from src.textsummarizer.entity.config_entity import DataIngestionConfig,DataTransformationConfig
from pathlib import Path
from src.textsummarizer.entity.config_entity import ModelTrainerConfig

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
    ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=(config.unzip_dir),
        )

        return data_ingestion_config
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=Path(config.root_dir),
            transformed_data_dir=Path(config.transformed_data_dir),
            tokenizer_name=config.tokenizer_name)
        return data_transformation_config
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=Path(config.root_dir),
            data_path=Path(config.data_path),
            model_ckpt=config.model_ckpt,
            num_train_epochs=config.num_train_epochs,
            warmup_steps=config.warmup_steps,
            per_device_train_batch_size=config.per_device_train_batch_size,
            weight_decay=config.weight_decay,
            logging_steps=config.logging_steps,
            evaluation_strategy=config.evaluation_strategy,
            eval_steps=config.eval_steps,
            save_steps=config.save_steps,
            gradient_accumulation_steps=config.gradient_accumulation_steps,
        )
        return model_trainer_config
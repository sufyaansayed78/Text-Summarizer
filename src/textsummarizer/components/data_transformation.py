from src.textsummarizer.logging import logger
from transformers import AutoTokenizer
from datasets import load_from_disk
from src.textsummarizer.entity.config_entity import DataTransformationConfig
class DataTrasnformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_name)

    def convert_examples_to_features(self,example_batch):
        input_encodings = self.tokenizer(example_batch['dialogue'] , max_length = 1024, truncation = True )

        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(example_batch['summary'], max_length = 128, truncation = True )

        return {
            'input_ids' : input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }
    
    def convert(self):
        dataset_samsum = load_from_disk(self.config.transformed_data_dir)
        logger.info(f"Dataset loaded from disk : {self.config.transformed_data_dir}")
        dataset_samsum_encoded = dataset_samsum.map(self.convert_examples_to_features, batched = True)
        dataset_samsum_encoded.save_to_disk(self.config.root_dir)
        logger.info(f"Dataset saved to disk : {self.config.transformed_data_dir}")


from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import Trainer, TrainingArguments
from transformers import DataCollatorForSeq2Seq
from datasets import load_from_disk
from src.textsummarizer.logging import logger
import torch
from src.textsummarizer.entity.config_entity import ModelTrainerConfig  
from pathlib import Path


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        logger.info("Loading the dataset from disk...")
        dataset = load_from_disk(str(self.config.data_path))

        logger.info("Loading the tokenizer and model...")
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt)

        logger.info("Setting up data collator...")
        data_collator = DataCollatorForSeq2Seq(tokenizer, model=model)

        logger.info("Setting up training arguments...")
        training_args = TrainingArguments(
            output_dir=str(self.config.root_dir),
            num_train_epochs=self.config.num_train_epochs,
            warmup_steps=self.config.warmup_steps,
            per_device_train_batch_size=self.config.per_device_train_batch_size,
            weight_decay=self.config.weight_decay,
            logging_steps=self.config.logging_steps,
            eval_strategy=self.config.evaluation_strategy,
            eval_steps=self.config.eval_steps,
            save_steps=int(float(self.config.save_steps)),
            gradient_accumulation_steps=self.config.gradient_accumulation_steps,
        )

        logger.info("Initializing Trainer...")
        trainer = Trainer(
            model=model,
            args=training_args,
            train_dataset=dataset["train"],
            eval_dataset=dataset["validation"],
            data_collator=data_collator,
            tokenizer=tokenizer,
        )

        logger.info("Starting training...")
        trainer.train()
        logger.info("Training completed.")
        model.save_pretrained(self.config.root_dir / "final_model")
        tokenizer.save_pretrained(self.config.root_dir / "final_model")












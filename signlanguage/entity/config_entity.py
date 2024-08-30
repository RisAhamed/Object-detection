import os
from dataclasses import dataclass
from datetime import datetime
from signlanguage.constant.training_pipeline import *

TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

@dataclass
class TrainingPipelineConfig:
    artifacts_dir: str = os.path.join(ATRIFACTS_DIR,TIMESTAMP)


training_pipeline_config: TrainingPipelineConfig=TrainingPipelineConfig()

@dataclass 
class DataIngestionConfig:
    data_ingestion_dir: str = os.path.join(
        training_pipeline_config.artifacts_dir,DATA_INGESTION_DIR_NAME
    )
    feature_store_file_path: str = os.path.join(
        data_ingestion_dir,DATA_INGESTION_FETURE_STORE
    )
    data_download_url : str = DATA_DOWNLOAD_URL


@dataclass
class DataValidationConfig:
    data_validation_dir: str = os.path.join(
        training_pipeline_config.artifacts_dir, DATA_VALIDATION_DIR_NAME
    )

    valid_status_file_dir: str = os.path.join(data_validation_dir, DATA_VALIDATION_STATUS_FILE)

    required_file_list = DATA_VALIDATION_REQUIRED_FILES

# from dataclasses import dataclass, field

# @dataclass
# class DataValidationConfig:
#     data_validation_dir: str = os.path.join(
#         training_pipeline_config.artifacts_dir, DATA_VALIDATION_DIR_NAME
#     )
#     valid_status_file_dir: str = os.path.join(data_validation_dir, DATA_VALIDATION_STATUS_FILE)
#     required_file_list: list = field(default_factory=lambda: DATA_VALIDATION_REQUIRED_FILES)  # Use default_factory


@dataclass
class ModelTrainerconfig:
    model_training_dir: str = os.path.join(
        training_pipeline_config.artifacts_dir,  MODEL_TRAINER_DIR_NAME
    )
    weight_name = MODEL_TRAINER_PRETRAINED_WEIGHT_NAME
    no_of_epochs = MODEL_TRAINER_NO_EPOCHS
    batch_size = MODEL_TRAINER_BATCH_SIZE


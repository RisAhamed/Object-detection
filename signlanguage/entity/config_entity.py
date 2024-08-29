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

    
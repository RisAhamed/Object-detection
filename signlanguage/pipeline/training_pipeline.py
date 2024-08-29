import os,sys
from signlanguage.logger import logger
from signlanguage.exception import SignException
from signlanguage.components.data_ingestion import DataIngestion
from signlanguage.entity.artifacts_entity import DataIngestionArtifacts
from signlanguage.entity.config_entity  import DataIngestionConfig



class TrainingPipeline:
    def __init__(self):
        self.data_ingestion_config= DataIngestionConfig()

    def start_data_ingestion(self) -> DataIngestionArtifacts:
        try:
            logger.info("<<<<<<<<<Started the data ingestion inside the Training_pipeline.py>>>>>>>")
            data_ingestion = DataIngestion(self.data_ingestion_config)
            data_ingestion_artifacts = data_ingestion.initiate_data_ingestion()
            logger.info("Ingestion is Compleed")

            return data_ingestion_artifacts
        except Exception as e:
            
            raise  SignException(e,sys)
        
    def run_pipeline(self)->None:
        try: 
            data_ingestion_artifact = self.start_data_ingestion()
        except Exception as e:
            raise SignException(e,sys)
        
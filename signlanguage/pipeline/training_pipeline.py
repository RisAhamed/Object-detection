import os,sys
from signlanguage.logger import logger
from signlanguage.exception import SignException
from signlanguage.components.data_ingestion import DataIngestion
from signlanguage.entity.artifacts_entity import DataIngestionArtifacts,DataValidationArtifacts
from signlanguage.entity.config_entity  import DataIngestionConfig,DataValidationConfig
from signlanguage.components.data_validation import DataValidation


class TrainingPipeline:
    def __init__(self):
        self.data_ingestion_config= DataIngestionConfig()
        self.data_validation_config = DataValidationConfig()

    def start_data_ingestion(self) -> DataIngestionArtifacts:
        try:
            logger.info("<<<<<<<<<Started the data ingestion inside the Training_pipeline.py>>>>>>>")
            data_ingestion = DataIngestion(self.data_ingestion_config)
            data_ingestion_artifacts = data_ingestion.initiate_data_ingestion()
            logger.info("Ingestion is Compleed")

            return data_ingestion_artifacts
        except Exception as e:
            
            raise  SignException(e,sys)

    def start_data_validation(
        self, data_ingestion_artifact: DataIngestionArtifacts
    ) -> DataValidationArtifacts:
        logger.info("Entered the start_data_validation method of TrainPipeline class")

        try:
            data_validation = DataValidation(
                data_ingestion_artifact=data_ingestion_artifact,
                data_validation_config=self.data_validation_config,
            )

            data_validation_artifact = data_validation.initiate_data_validation()

            logger.info("Performed the data validation operation")

            logger.info(
                "Exited the start_data_validation method of TrainPipeline class"
            )

            return data_validation_artifact

        except Exception as e:
            raise SignException(e, sys) from e
        
    def run_pipeline(self)->None:
        try: 
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
        except Exception as e:
            raise SignException(e,sys)
        
import os,sys
from signlanguage.configuration.s3_operations import S3Operation
from signlanguage.entity.config_entity import ModelPusherConfig
from signlanguage.entity.artifacts_entity import  ModelPusherArtifact,ModelTrainerArtifact

from signlanguage.exception import SignException
from signlanguage.logger import logger


class ModelPusher:
    def __init__(self,model_pusher_config: ModelPusherConfig,model_trainer_artifact : ModelTrainerArtifact,s3: S3Operation):
        
        self.model_pusher_config = model_pusher_config
        self.model_trainer_artifacts = model_trainer_artifact
        self.s3 = s3

    def initiate_model_pusher(self) -> ModelPusherArtifact:

        """
        Method Name :   initiate_model_pusher

        Description :   This method initiates model pusher. 
        
        Output      :    Model pusher artifact 
        """
        logger.info("Entered initiate_model_pusher method of Modelpusher class")
        try:
            # Uploading the best model to s3 bucket
            self.s3.upload_file(
                self.model_trainer_artifacts.trained_model_file_path,
                self.model_pusher_config.S3_MODEL_KEY_PATH,
                self.model_pusher_config.BUCKET_NAME,
                remove=False,
            )
            logger.info("Uploaded best model to s3 bucket")
            logger.info("Exited initiate_model_pusher method of ModelTrainer class")

            # Saving the model pusher artifacts
            model_pusher_artifact = ModelPusherArtifact(
                bucket_name=self.model_pusher_config.BUCKET_NAME,
                s3_model_path=self.model_pusher_config.S3_MODEL_KEY_PATH,
            )

            return model_pusher_artifact

        except Exception as e:
            raise SignException(e, sys) from e
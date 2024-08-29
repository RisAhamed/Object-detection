# from signlanguage.logger import logger
from signlanguage.logger import logger
from signlanguage.pipeline.training_pipeline import TrainingPipeline

logger.info("Message")
from signlanguage.exception import SignException

training_pipe= TrainingPipeline()
training_pipe.run_pipeline()
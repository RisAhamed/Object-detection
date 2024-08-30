import os, sys
import yaml
import zipfile
import shutil
from signlanguage.utils import read_yaml_file
from signlanguage.logger import logger
from signlanguage.exception import SignException
from signlanguage.entity.config_entity import ModelTrainerconfig
from signlanguage.entity.artifacts_entity import ModelTrainerArtifact

from pathlib import Path
class ModelTrainer:
    def __init__(
        self,
        model_trainer_config: ModelTrainerconfig,
    ):
        self.model_trainer_config = model_trainer_config

    def initiate_model_trainer(self,) -> ModelTrainerArtifact:
        logger.info("Entered initiate_model_trainer method of ModelTrainer class")

        try:
            logger.info("Unzipping data")
            # Unzipping the data using Python's zipfile module
            with zipfile.ZipFile('Sign_language_data.zip', 'r') as zip_ref:
                zip_ref.extractall('.')  # Extract to the current directory

            # Remove the zip file after extraction
            os.remove("Sign_language_data.zip")

            # Load the number of classes from the data.yaml file
            with open("data.yaml", 'r') as stream:
                num_classes = str(yaml.safe_load(stream)['nc'])

            model_config_file_name = self.model_trainer_config.weight_name.split(".")[0]
            print(model_config_file_name)

            from pathlib import Path

# Use a raw string or double backslashes for the file path
            path = str(Path(r"C:\Users\riswa\Desktop\AI\Object-detection\yolov5\models\yolov5s.yaml"))
            config = read_yaml_file(path)

            # config = read_yaml_file(f"yolov5\models\{model_config_file_name}.yaml")


            config['nc'] = int(num_classes)

            # Save the updated configuration
            with open(f'yolov5/models/custom_{model_config_file_name}.yaml', 'w') as f:
                yaml.dump(config, f)

            # Run the training command using Python's os module
            # os.system(
            #     f"cd yolov5 && python train.py --img 416 --batch {self.model_trainer_config.batch_size} "
            #     f"--epochs {self.model_trainer_config.no_of_epochs} --data ../data.yaml --cfg ./models/custom_yolov5s.yaml "
            #     f"--weights {self.model_trainer_config.weight_name} --name yolov5s_results --cache"
            # )

            # # Copy the best model to the specified directories using shutil
            # shutil.copy("yolov5/runs/train/yolov5s_results/weights/best.pt", "yolov5/")
            # os.makedirs(self.model_trainer_config.model_training_dir, exist_ok=True)
            # shutil.copy("yolov5/runs/train/yolov5s_results/weights/best.pt", self.model_trainer_config.model_training_dir)
            os.system(f"cd yolov5/ && python train.py --img 416 --batch {self.model_trainer_config.batch_size} --epochs {self.model_trainer_config.no_of_epochs} --data ../data.yaml --cfg ./models/custom_yolov5s.yaml --weights {self.model_trainer_config.weight_name} --name yolov5s_results  --cache")
            os.system("cp yolov5/runs/train/yolov5s_results/weights/best.pt yolov5/")
            os.makedirs(self.model_trainer_config.model_training_dir, exist_ok=True)
            os.system(f"cp yolov5/runs/train/yolov5s_results/weights/best.pt {self.model_trainer_config.model_training_dir}/")
           
            # Cleanup directories and files using shutil and os
            shutil.rmtree("yolov5/runs", ignore_errors=True)
            if os.path.exists("data.yaml"):
                os.remove("data.yaml")

            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path="yolov5/best.pt",
            )

            logger.info("Exited initiate_model_trainer method of ModelTrainer class")
            logger.info(f"Model trainer artifact: {model_trainer_artifact}")

            return model_trainer_artifact

        except Exception as e:
            raise SignException(e, sys)

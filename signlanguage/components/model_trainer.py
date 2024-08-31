import os
import sys
import yaml
import zipfile
import shutil
from pathlib import Path
from signlanguage.utils import read_yaml_file
from signlanguage.logger import logger
from signlanguage.exception import SignException
from signlanguage.entity.config_entity import ModelTrainerconfig
from signlanguage.entity.artifacts_entity import ModelTrainerArtifact

class ModelTrainer:
    def __init__(self, model_trainer_config: ModelTrainerconfig):
        self.model_trainer_config = model_trainer_config

    def initiate_model_trainer(self) -> ModelTrainerArtifact:
        logger.info("Entered initiate_model_trainer method of ModelTrainer class")

        try:
            # Unzipping the data using Python's zipfile module
            logger.info("Unzipping data")
            with zipfile.ZipFile('Sign_language_data.zip', 'r') as zip_ref:
                zip_ref.extractall('.')  # Extract to the current directory

            # Remove the zip file after extraction
            import os
            os.remove("Sign_language_data.zip")

            # Load the number of classes from the data.yaml file
            with open("data.yaml", 'r') as stream:
                num_classes = str(yaml.safe_load(stream)['nc'])

            # Get the model config file name from the weight file
            model_config_file_name = self.model_trainer_config.weight_name.split(".")[0]

            # Construct the file path using pathlib for cross-platform compatibility
            path = str(Path(r"C:\Users\riswa\Desktop\AI\Object-detection\yolov5\models\yolov5s.yaml"))

            config = read_yaml_file(path)
            # Update the number of classes in the configuration
            config['nc'] = int(num_classes)

            # Save the updated configuration
            import shutil
            import os

            with open(f'yolov5/models/custom_{model_config_file_name}.yaml', 'w') as f:
                yaml.dump(config, f)

            # Run the training script
            command = [
                "python", "train.py",
                "--img", "416",
                "--batch", str(self.model_trainer_config.batch_size),
                "--epochs", str(self.model_trainer_config.no_of_epochs),
                "--data", "../data.yaml",
                "--cfg", f"./models/custom_{model_config_file_name}.yaml",
                "--weights", self.model_trainer_config.weight_name,
                "--name", "yolov5s_results",
                "--cache"
            ]
            os.chdir("yolov5")  # Change to the yolov5 directory
            os.system(" ".join(command))  # Run the command in the current shell
            os.chdir("..")  # Go back to the parent directory

            # Copy the best model to the yolov5 directory using shutil for cross-platform compatibility
            # best_model_path = "yolov5/runs/train/yolov5s_results/weights/best.pt"
            # yolov5_dir = "yolov5/best.pt"
            # shutil.copy(best_model_path, yolov5_dir)

            # # Create the model training directory
            # os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True)

            # # Copy the best model to the model training directory
            # shutil.copy(best_model_path, os.path.join(self.model_trainer_config.model_trainer_dir, "best.pt"))

            
            best_model_path = "yolov5/runs/train/yolov5s_results/weights/best.pt"
            yolov5_dir = "yolov5/best.pt"

            # Use os.system to copy the best model file to the yolov5 directory
            os.system(f'copy "{best_model_path}" "{yolov5_dir}"' if os.name == 'nt' else f'cp "{best_model_path}" "{yolov5_dir}"')

            # Create the model training directory if it doesn't exist
            os.makedirs(self.model_trainer_config.model_training_dir, exist_ok=True)

            # Use os.system to copy the best model file to the model training directory
            os.system(f'copy "{best_model_path}" "{os.path.join(self.model_trainer_config.model_training_dir, "best.pt")}"' if os.name == 'nt' else f'cp "{best_model_path}" "{os.path.join(self.model_trainer_config.model_training_dir, "best.pt")}"')


            # (Optional) Clean up directories and files after training
            # shutil.rmtree('yolov5/runs', ignore_errors=True)
            # shutil.rmtree('train', ignore_errors=True)
            # shutil.rmtree('test', ignore_errors=True)
            # os.remove('data.yaml')

           

            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path="yolov5/best.pt",
            )

            logger.info("Exited initiate_model_trainer method of ModelTrainer class")
            logger.info(f"Model trainer artifact: {model_trainer_artifact}")

            return model_trainer_artifact

        except Exception as e:
            raise SignException(e, sys)

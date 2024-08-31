ATRIFACTS_DIR : str = "artifacts"


DATA_INGESTION_DIR_NAME : str = "dataingestion"

DATA_INGESTION_FETURE_STORE :  str = "Feature_store"

DATA_DOWNLOAD_URL : str = "https://github.com/RisAhamed/Object-detection/raw/main/Sign_language_data.zip"


DATA_VALIDATION_DIR_NAME: str = "datavalidation"

DATA_VALIDATION_STATUS_FILE : str = "Status.txt"

DATA_VALIDATION_REQUIRED_FILES  =['train',"test","data.yaml","valid"]


MODEL_TRAINER_DIR_NAME : str = "model_Trainer"
MODEL_TRAINER_PRETRAINED_WEIGHT_NAME : str = "yolo5s.pt"
MODEL_TRAINER_NO_EPOCHS: int = 1
MODEL_TRAINER_BATCH_SIZE: int =5

BUCKET_NAME ="riswan-sing-lang"
S3_MODEL_NAME ="best.pt"

from dataclasses import dataclass

@dataclass
class DataIngestionArtifacts:
    data_zip_file_path: str
    feature_store_path: str
    

@dataclass
class DataValidationArtifacts:
    validation_status: bool

@dataclass
class ModelTrainerArtifact:
    trained_model_file_path : str
    

@dataclass
class ModelPusherArtifact:
    bucket_name : str
    s3_model_path: str
    
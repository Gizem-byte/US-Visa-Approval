import os
from datetime import datetime
from datetime import date


"""Constants for the US Visa Prediction project.
   These constants are used throughout the project for various purposes.
   They include database names, collection names, and other configuration settings.
    These constants help maintain consistency and avoid hardcoding values in the codebase.
    They are typically defined in a separate module or file to keep the code organized and maintainable.
    Constants are usually written in uppercase letters to distinguish them from regular variables.
    This convention helps developers quickly identify constants in the code and understand their purpose.
    Constants are often used for configuration settings, file paths, database names, and other values that are unlikely to change frequently.
    By defining them in one place, it becomes easier to manage and update them as needed.
"""

DATABASE_NAME = "US_VISA" #Database name for MongoDB

## This is the default collection for general MongoDB operations.
COLLECTION_NAME = "visa_data" #Collection name for MongoDB

MONGODB_URL_KEY = "MONGODB_URL" #Connection string for MongoDB

PIPELINE_NAME: str = "usvisa" #Name of the pipeline for logging and tracking purposes in MLFlow

ARTIFACT_DIR:str ="artifact" #Directory where artifacts are stored after each pipeline run

MODEL_FILE_NAME = "model.pkl" #File name for the trained model artifact after each pipeline run

FILE_NAME: str ="Visadataset.csv" #File name for the dataset used in the project 

TRAIN_FILE_NAME: str = "train.csv" #File name for the training dataset after splitting

TEST_FILE_NAME: str = "test.csv" #File name for the testing dataset after splitting

TARGET_COLUMN = "case_status" #Target column in the dataset, which is the label we want to predict

CURRENT_YEAR = date.today().year 

PREPROCSSING_OBJECT_FILE_NAME = "preprocessing.pkl" #File name for the preprocessing object artifact after each pipeline run

SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml") #Path to the schema file for data validation and preprocessing


AWS_ACCESS_KEY_ID_ENV_KEY = "AWS_ACCESS_KEY_ID"
AWS_SECRET_ACCESS_KEY_ENV_KEY = "AWS_SECRET_ACCESS_KEY"
REGION_NAME = "eu-north-1"



"""Data Ingestion related constants start with DATA_INGESTION VAR NAME"""

# This is specific to the data ingestion pipeline. 
# Today, it points to the same collection, but in the future, 
# it might reference a dedicated ingestion collection (e.g., "visa_data_raw").
DATA_INGESTION_COLLECTION_NAME: str = "visa_data" #Collection name for MongoDB for data ingestion component 
DATA_INGESTION_DIR_NAME: str = "data_ingestion" #Directory name for data ingestion artifacts 
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store" #Directory name for feature store artifacts 
DATA_INGESTION_INGESTED_DIR: str = "ingested" #Directory name for ingested data artifacts 
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2 #Ratio for splitting the dataset into training and testing sets


"""
Data Validation realted contant start with DATA_VALIDATION VAR NAME

"""

DATA_VALIDATION_DIR_NAME: str = "data_validation" #Directory name for data validation artifacts
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift_report" #Directory name for drift report artifacts
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = "report.yaml" #File name for the drift report artifact



"""
Data Transformation ralated constant start with DATA_TRANSFORMATION VAR NAME
"""
DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation" #Directory name for data transformation artifacts
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "transformed" #Directory name for transformed data artifacts
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object" #Directory name for transformed object artifacts



"""
MODEL TRAINER related constant start with MODEL_TRAINER var name
"""
MODEL_TRAINER_DIR_NAME: str = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR: str = "trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME: str = "model.pkl"
MODEL_TRAINER_EXPECTED_SCORE: float = 0.6
MODEL_TRAINER_MODEL_CONFIG_FILE_PATH: str = os.path.join("config", "model.yaml")




"""
MODEL EVALUATION related constant 
"""
MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE: float = 0.02
MODEL_BUCKET_NAME = "usvisa-gizem-bucket2025"
MODEL_PUSHER_S3_KEY = "model-registry"


APP_HOST = "127.0.0.1"
APP_PORT = 8080
import os
from datetime import datetime


"""Constants for the US Visa Prediction project.
   These constants are used throughout the project for various purposes.
   They include database names, collection names, and other configuration settings.
    These constants help maintain consistency and avoid hardcoding values in the codebase.
    They are typically defined in a separate module or file to keep the code organized and maintainable.
    Constants are usually written in uppercase letters to distinguish them from regular variables.
    This convention helps developers quickly identify constants in the code and understand their purpose.
"""

DATABASE_NAME = "US_VISA"

COLLECTION_NAME = "visa_data"

MONGODB_URL_KEY = "MONGODB_URL" #Connection string for MongoDB

PIPELINE_NAME: str = "usvisa"

ARTIFACT_DIR:str ="artifact"

MODEL_FILE_NAME = "model.pkl"

FILE_NAME: str ="Visadataset.csv"

TRAIN_FILE_NAME: str = "train.csv"

TEST_FILE_NAME: str = "test.csv"



"""Data Ingestion related constants start with DATA_INGESTION VAR NAME"""

DATA_INGESTION_COLLECTION_NAME: str = "visa_data"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2


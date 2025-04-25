import os                   # For file/directory operations (e.g., creating folders)
import sys                  # For system-level operations (e.g., handling exceptions)
from pandas import DataFrame  # To work with tabular data (like spreadsheets)
from sklearn.model_selection import train_test_split  # To split data into train/test sets
from us_visa.entity.config_entity import DataIngestionConfig  # Configuration settings for data ingestion
from us_visa.entity.artifact_entity import DataIngestionArtifact  # Outputs of data ingestion (train/test paths)
from us_visa.exception import USvisaException  # Custom exception class for error handling
from us_visa.logger import logging             # For logging progress/errors
from us_visa.data_access.usvisa_data import USvisaData  # Class to fetch data from MongoDB



class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig=DataIngestionConfig()):
        """
        :param data_ingestion_config: configuration for data ingestion
        """
        try:
            #Initialize with a configuration object (uses values from constants)
            self.data_ingestion_config = data_ingestion_config
            
        except Exception as e:
            #Raise a custom exception if initialization fails
            raise USvisaException(e,sys)
        

    
    def export_data_into_feature_store(self)->DataFrame:
        """
        Method Name :   export_data_into_feature_store
        Description :   This method exports data from mongodb to csv file
        
        Output      :   data is returned as artifact of data ingestion components
        On Failure  :   Write an exception log and then raise an exception
        """
        try:
           
           logging.info("Exporting data from MongoDB")  # Log the start of the process
           usvisa_data = USvisaData()  # Create an object to interact with MongoDB
            # Fetch data from MongoDB using the collection name from the configuration
           dataframe = usvisa_data.export_collection_as_dataframe(
           collection_name=self.data_ingestion_config.collection_name)
           logging.info(f"Shape of dataframe: {dataframe.shape}")  # Log the size of the data
           # Get the path to save the CSV (from config, which uses constants like FILE_NAME)
           feature_store_file_path = self.data_ingestion_config.feature_store_file_path
           # Create directories if they don’t exist (e.g., `artifact/feature_store`)
           dir_path = os.path.dirname(feature_store_file_path)
           os.makedirs(dir_path, exist_ok=True)
           # Save the data to CSV (e.g., `Visadataset.csv`)
           dataframe.to_csv(feature_store_file_path, index=False, header=True)
           return dataframe  # Return the data for further processing
        
        except Exception as e:
          raise USvisaException(e, sys)  # Handle errors
        

     

    def split_data_as_train_test(self, dataframe: DataFrame) -> None:
        
      logging.info("Splitting data into train/test sets")  # Log the process
      try:
        # Split data using the ratio from the config (e.g., 0.2 for 20% test data)
        train_set, test_set = train_test_split(
            dataframe, 
            test_size=self.data_ingestion_config.train_test_split_ratio
        )
        # Create directories for train/test files (e.g., `artifact/ingested`)
        dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
        os.makedirs(dir_path, exist_ok=True)
        # Save train/test files (paths come from constants like TRAIN_FILE_NAME)
        train_set.to_csv(self.data_ingestion_config.training_file_path, index=False, header=True)
        test_set.to_csv(self.data_ingestion_config.testing_file_path, index=False, header=True)
      except Exception as e:
        raise USvisaException(e, sys)  # Handle errors

    
    def initiate_data_ingestion(self) ->DataIngestionArtifact:
        """
        Method Name :   initiate_data_ingestion
        Description :   This method initiates the data ingestion components of training pipeline 
        
        Output      :   train set and test set are returned as the artifacts of data ingestion components
        On Failure  :   Write an exception log and then raise an exception
        """
        logging.info("Entered initiate_data_ingestion method of Data_Ingestion class")

        try:
          # Step 1: Export data from MongoDB to CSV
          dataframe = self.export_data_into_feature_store()
          # Step 2: Split data into train/test sets
          self.split_data_as_train_test(dataframe)
          # Step 3: Create an artifact to pass outputs to the next pipeline stage
          data_ingestion_artifact = DataIngestionArtifact(
            trained_file_path=self.data_ingestion_config.training_file_path,
            test_file_path=self.data_ingestion_config.testing_file_path )
          return data_ingestion_artifact  # Return the artifact (train/test paths)
        
        except Exception as e:
          raise USvisaException(e, sys)  # Handle errors

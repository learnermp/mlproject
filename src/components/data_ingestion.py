import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass # used to create class variables

from src.exception import CustomException
from src.logger import logging
from src.components.data_transformation import DataTransformation, DataTransformationConfig


@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts','train.csv')        # train data will saved in this path
    test_data_path: str = os.path.join('artifacts','test.csv')         # these three inputs wwe are giving to data ingestion component
    raw_data_path: str = os.path.join('artifacts','data.csv')   # artifacts are basically folders. 

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):   # if data is stored in database, the code for reading that data will be written here
        logging.info("Entered data ingestion method or components")
        try:
            df = pd.read_csv(r'C:\Users\mriyu\OneDrive\Desktop\Data_Science-LAPTOP-GMML798J\1ML Projects\mlproject\notebook\data\stud.csv')
            # here to df the data source could be mySQL, mongoDB, any APIs or something else
            logging.info("Read the dataset asmdataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index =False, header =True)

            logging.info("train test split initiated")

            train_set, test_set = train_test_split(df, test_size= 0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index =False, header =True)

            test_set.to_csv(self.ingestion_config.test_data_path, index =False, header =True)

            logging.info("Ingestion of the data completed")

            return(
                self.ingestion_config.train_data_path, self.ingestion_config.test_data_path
            )
                    
        except Exception as e:
            raise CustomException
    
if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_data, test_data)


                     

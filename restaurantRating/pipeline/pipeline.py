
from datetime import datetime
import uuid
import sys,os
from restaurantRating.config.configuration import Configuration
from restaurantRating.logger import logging, get_log_file_name
from restaurantRating.exception import RestaurantRatingException
from typing import List
from restaurantRating.entity.artifact_entity import DataIngestionArtifact
from restaurantRating.entity.config_entity import DataIngestionConfig
from restaurantRating.component.data_ingestion import DataIngestion


# import os, sys
from collections import namedtuple
from datetime import datetime
import pandas as pd
from restaurantRating.constant import EXPERIMENT_DIR_NAME, EXPERIMENT_FILE_NAME


class Pipeline():
    
    def __init__(self, config: Configuration=Configuration() ) -> None:
        try:
            self.config = config
        except Exception as e:
            raise RestaurantRatingException(e, sys) from e

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()

        except Exception as e:
            raise RestaurantRatingException(e, sys) from e

   
    def run_pipeline(self):
        try:
            # data ingestion
            data_ingestion_artifact = self.start_data_ingestion()

        except Exception as e:
            raise RestaurantRatingException(e, sys) from e

    def run(self):
        try:
            self.run_pipeline()
        except Exception as e:
            raise e


import os
import sys

from restaurantRating.exception import RestaurantRatingException
from restaurantRating.util.util import load_object

import pandas as pd


class RestaurantRatingData:

    def __init__(self,
                Restaurant_Name: object, 
                Country_Code: int,  
                City: object, 
                Address: object, 
                Locality: object, 
                Locality_Verbose: object, 
                lon: float,
                lat: float,
                cost_for_two: int,  
                Currency: object, 
                Has_Table_booking: object, 
                Has_Online_delivery: object ,
                Is_delivering_now: object, 
                Switch_to_order_menu: object, 
                Price_Range: int,  
                Rating: float,
                Rating_color: object, 
                Review: object,
                Votes: int 
                ):
        try:

            self.Restaurant_Name: Restaurant_Name
            self.Country_Code: Country_Code  
            self.City: City
            self.Address: Address 
            self.Locality: Locality 
            self.Locality_Verbose: Locality_Verbose 
            self.lon: lon
            self.lat: lat
            self.cost_for_two: cost_for_two   
            self.Currency: Currency  
            self.Has_Table_booking: Has_Table_booking  
            self.Has_Online_delivery: Has_Online_delivery  
            self.Is_delivering_now: Is_delivering_now  
            self.Switch_to_order_menu: Switch_to_order_menu  
            self.Price_Range: Price_Range   
            self.Rating: Rating 
            self.Rating_color: Rating_color  
            self.Review: Review 
            self.Votes: Votes

        except Exception as e:
            raise RestaurantRatingException(e, sys) from e

    def get_restaurant_rating_input_data_frame(self):

        try:
            restaurant_rating_input_dict = self.get_housing_data_as_dict()
            return pd.DataFrame(restaurant_rating_input_dict)
        except Exception as e:
            raise RestaurantRatingException(e, sys) from e

    def get_restaurant_rating_data_as_dict(self):
        try:
            input_data = {
                "cost_for_two": [self.cost_for_two],   
                "Price_Range": [self.Price_Range],    
                "Votes": [self.Votes], 
                "Has_Table_booking": [self.Has_Table_booking],  
                "Has_Online_delivery": [self.Has_Online_delivery],  
                "Is_delivering_now": [self.Is_delivering_now],  
                "Switch_to_order_menu": [self.Switch_to_order_menu],  
                "Rating_color": [self.Rating_color],  
                "Review": [self.Review]}
            return input_data
        except Exception as e:
            raise RestaurantRatingException(e, sys)


class RestaurantRatingPredictor:

    def __init__(self, model_dir: str):
        try:
            self.model_dir = model_dir
        except Exception as e:
            raise RestaurantRatingException(e, sys) from e

    def get_latest_model_path(self):
        try:
            folder_name = list(map(int, os.listdir(self.model_dir)))
            latest_model_dir = os.path.join(self.model_dir, f"{max(folder_name)}")
            file_name = os.listdir(latest_model_dir)[0]
            latest_model_path = os.path.join(latest_model_dir, file_name)
            return latest_model_path
        except Exception as e:
            raise RestaurantRatingException(e, sys) from e

    def predict(self, X):
        try:
            model_path = self.get_latest_model_path()
            model = load_object(file_path=model_path)
            restaurant_rating = model.predict(X)
            return restaurant_rating
        except Exception as e:
            raise RestaurantRatingException(e, sys) from e
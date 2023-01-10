from flask import Flask
import sys
import os
from restaurantRating.logger import logging
from restaurantRating.exception import RestaurantRatingException

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    try: 
        raise Exception("we are raising exception")
    except Exception as e:
        restaurant = RestaurantRatingException(e,sys)
        logging.info(restaurant.error_message)
        logging.info("testing logging info")

    return "Hello Otti"

if __name__ =="__main__":
    app.run()
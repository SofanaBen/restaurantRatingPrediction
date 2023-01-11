from restaurantRating.pipeline.pipeline import Pipeline
from restaurantRating.exception import RestaurantRatingException
from restaurantRating.logger import logging

def main():
    try:
        
        pipeline = Pipeline()
        pipeline.run_pipeline()

        logging.info("main function execution completed.")
     
    except Exception as e:
        logging.error(f"{e}")
        print(e)



if __name__=="__main__":
    main()

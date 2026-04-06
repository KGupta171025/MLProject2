import sys
from src.mlproject2.logger import logging
from src.mlproject2.exception import CustomException


if __name__=="__main__":
    logging.info("This execition is started!")

    try:
        a=1/0
    except Exception as e:
        logging.info("Custom Error Exception!")
        raise CustomException(e,sys)

import logging
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
logger = logging.getLogger('eCommerce')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("eCommerce.log")
format = '%(asctime)s : %(name)s : %(levelname)s : %(message)s'
formatter = logging.Formatter(format)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def writeLog(message, level):
    if level == "INFO":
        logger.info(message)
    elif level == "ERROR":
        logger.error(message)
    elif level == "WARNING":
        logger.warning(message)
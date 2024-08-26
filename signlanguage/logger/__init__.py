# signlanguage/logger.py

import os
import logging
from datetime import datetime

class Logger:
    def __init__(self, log_dir="./logs"):
        self.log_dir = log_dir
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

    def create_logger(self):
        log_filename = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_log.log"
        log_filepath = os.path.join(self.log_dir, log_filename)

        logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
        logger = logging.getLogger("signlanguage_logger")
        logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler(log_filepath)
        stream_handler = logging.StreamHandler()

        file_handler.setFormatter(logging.Formatter(logging_str))
        stream_handler.setFormatter(logging.Formatter(logging_str))

        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

        return logger

logger_obj = Logger()
logger = logger_obj.create_logger()
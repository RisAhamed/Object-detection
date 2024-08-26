# from signlanguage.logger import logger
from signlanguage.logger import logger

logger.info("Message")
from signlanguage.exception import SignException

try :
    x  =1/0
except Exception as e:
    import sys
    raise SignException(e,sys)
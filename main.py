import logging
import time
# from logging.handlers import RotatingFileHandler
from os import environ

from subclasses.subclass import Subclass

### LOGGING ###
logging.basicConfig(filename='master.log',
                    format='%(asctime)s %(module)s.%(funcName)s %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
# maxBytes=1000000 -> 1MB
# handler = RotatingFileHandler('master.log', maxBytes=1000000, backupCount=0)
# logger.addHandler(handler)


sc = Subclass()

if __name__ == '__main__':
    if environ.get('ENV') == 'dev':
        print(' *** Running in ENV {}'.format(environ.get('ENV')))
        debug = True
    while True:
        logger.info('__main__ logging info')
        sc.test_log_info()
        sc.test_log_warning()
        time.sleep(20)

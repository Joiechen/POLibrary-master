import logging
import os.path
import time

class Logger(object):
    def __init__(self,logger):
        """
        Save the log to specify location
        Sepcify the logger level
        :param logger:
        """

        #Create logger file
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        #Create a handle for write logger
        now = time.strftime("%Y-%m-%d_%H_%M_%S_")
        log_path = os.path.dirname(os.path.abspath('.'))+'/logs/'
        log_name = log_path + now + '.log'

        filehandle = logging.FileHandler(log_name, encoding="utf-8")
        filehandle.setLevel(logging.INFO)

        #Create a handle for input logging console
        consolehandle = logging.StreamHandler()
        consolehandle.setLevel(logging.INFO)

        #format the output handle
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        filehandle.setFormatter(formatter)
        consolehandle.setFormatter(formatter)

        #Add the handle for logger
        self.logger.addHandler(filehandle)
        self.logger.addHandler(consolehandle)

    def getlog(self):
        return self.logger
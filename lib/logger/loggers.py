from logging.config import fileConfig
from typing import Optional
import logging
import threading

fileConfig("lib/logger/logger.conf")

class takelogger:
    def __init__(self,loggerName,threadName=None, threadID=None,formt=None):
        self.loggerName = loggerName
        self.threadID = threadID 
        self.threadName = threadName 
        self.logger = logging.getLogger(loggerName)
        
        if formt is not None:
            self.threadName = threadName
            self.threadID = threadID
            self.handler = logging.FileHandler("efc.log","a+",encoding="utf-8")
            self.formatter = logging.Formatter(fmt="%(asctime)s --- [%(name)s] => %(levelname)s:%(levelno)s (%(message)s) | thn {0} | thd {1} | procn %(processName)s | procd %(process)s".format(self.threadName,self.threadID))
            self.handler.setFormatter(self.formatter)
            self.logger.handlers.clear()
            self.logger.addHandler(self.handler)
            
        if threadName is None or threadID is None:
            return
        else:
            self.threadName = threadName
            self.threadID = threadID
            self.handler = logging.FileHandler("efc.log","a+",encoding="utf-8")
            self.formatter = logging.Formatter(fmt="%(asctime)s --- [%(name)s] => %(levelname)s:%(levelno)s (%(message)s) | thn {0} | thd {1} | procn %(processName)s | procd %(process)s".format(self.threadName,self.threadID))
            self.handler.setFormatter(self.formatter)
            self.logger.handlers.clear()
            self.logger.addHandler(self.handler)
        
    
    def debug(self,message: Optional[str]):
        self.logger.debug(message)
        
    def info(self,message: Optional[str]):
        self.logger.info(message)
        
    def warning(self,message: Optional[str]):
        self.logger.warning(message)
        
    def error(self,message: Optional[str]):
        self.logger.error(message)
        
    def critical(self,message: Optional[str]):
        self.logger.critical(message)

logger =takelogger("efc")
logger.debug("DF")

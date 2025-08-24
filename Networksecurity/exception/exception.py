import sys
from Networksecurity.logging import logger

class NetworkSecurityException(Exception):
    def __init__(self,error_message,error_details:sys):
        self.error_message=error_message
        _,_,exc_tb=error_details.exc_info()#It is a traceback object which tells where error has occured at which line
    

        self.lineno=exc_tb.tb_lineno#Line number of error
        self.file_name=exc_tb.tb_frame.f_code.co_filename#File name where it happened

    def __str__(self):
        return "Error occured in pyhton script name [{0}] line number [{1}] error message[{2}]".format(
        self.file_name,self.lineno, str(self.error_message))

        
#You deliberately trigger a ZeroDivisionError (1 / 0)
#The except block catches it and raises your custom exception with all the context
if __name__=='__main__':
    try:
        logger.logging.info("Enter the try block")
        a=1/0
        print("This will not be printed",a)
    except Exception as e:
        raise NetworkSecurityException(e,sys)


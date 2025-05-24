import os

def error_message_detail(error, error_detail):
    '''
        It takkes an error and an details and returns a string with file name, line number
        and error message.
        
        Returns:
            The error message is being return.
    '''
    
    _,_, exc_tb = error_detail.exc_info()
    
    filename = os.path.split(exc_tb.tb_frame.f_code.c0filename)[1]
    error_message = "Error occured python script name [{0}] line number [{1}] error message [{2}]".format(
        filename,
        exc_tb.tb_lineno,
        str(error)
    )
    
    return error_message

# Its a custom exception class that takes an error message and an error detail and return a formatted error message.

class TTSException(Exception):
    def __init__(self, error_message, error_detail):
        super().__init__(error_message)
        self.error_message = error_message_detail(
            error_message, error_detail
        )
    def __str__(self):
        return self.error_message

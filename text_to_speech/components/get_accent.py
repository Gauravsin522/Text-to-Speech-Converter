from text_to_speech.exception import TTSException
from text_to_speech.logger import logger
import sys

def get_accent_tld(user_input):
    '''
        It takes a user and returns the top level domain (tld) for the accent the user wants.
        
        Args:
            user_input: The user's text input
            
        Returns:
            The tld is being returned
        
    '''
    
    try:
        accent_input = {
            'Indian':'co.in',
            'Austrialian':"co.au",
            'South_Africa' : 'co.za',
            'British':'co.uk',
            'Canadian':"ca",
            'Irish':'ie',
            'Spanish':"es"
        }
        
        tld = accent_input.get(user_input)
        return tld
    except Exception as e:
        raise TTSException(e,sys)
    
def get_accent_message():
    '''
    It returns list of accents.
    
    Returns:
        A list of accents.
    '''
    try:
        accent = ['Indian',"Australian","South Africa", 'British', "Canadian", "Irish", 'Spanish']
        return accent
    
    except Exception as e:
        raise TTSException(e, sys) from e
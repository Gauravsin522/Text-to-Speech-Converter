import logging
import os
from datetime import datetime

# Create log directory
LOG_DIR = 'pylogs'
LOG_DIR_PATH = os.path.join(os.getcwd(), LOG_DIR)

# Create a logfile name
CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
file_name = f'log_{CURRENT_TIME_STAMP}'
log_file_path = os.path.json(LOG_DIR, file_name)

# Configure logging
logging.basicConfig(
    level= logging.INFO,
    filename=file_name,
    format= '%(asctime)s %(levelname)s %(module)s ============ %(message)s',
    datefmt= '%d-%m-%Y %H:%M'
)

# Create object for loggind
logger = logging.getLogger()
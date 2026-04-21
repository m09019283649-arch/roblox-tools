import logging
from logging.handlers import RotatingFileHandler

# Define a logger instance
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a rotating file handler
handler = RotatingFileHandler('app.log', maxBytes=5*1024*1024, backupCount=3)
handler.setLevel(logging.DEBUG)

# Create a formatter and set it for the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)

# Example of using the logger
if __name__ == '__main__':
    logger.info('Logger setup complete.')
    logger.debug('This is a debug message.')
    logger.warning('This is a warning message.')
    logger.error('This is an error message.')
    logger.critical('This is a critical message.')

import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='app.log', max_bytes=5*1024*1024, backup_count=5):
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)

    if not logger.hasHandlers():
        # Create log directory if it doesn't exist
        log_dir = os.path.dirname(log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # Setup rotating file handler
        handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        logger.addHandler(handler)
    return logger

if __name__ == '__main__':
    logger = setup_logger('logs/application.log')
    logger.info('Logger setup complete.')
    logger.warning('This is a warning message.')
    logger.error('This is an error message.')
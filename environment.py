import os
import logging
import logging.config
from dotenv import load_dotenv

def setup_logging():
    # Ensure the logs directory exists
    logs_dir = 'logs'
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    # Define logging configuration
    logging_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '%(asctime)s - %(levelname)s - %(message)s'
            },
        },
        'handlers': {
            'file_handler': {
                'class': 'logging.FileHandler',
                'filename': os.path.join(logs_dir, 'app.log'),
                'formatter': 'standard',
                'level': 'DEBUG',
            },
            'console_handler': {
                'class': 'logging.StreamHandler',
                'formatter': 'standard',
                'level': 'INFO',
            },
        },
        'loggers': {
            '': {
                'handlers': ['file_handler', 'console_handler'],
                'level': 'DEBUG',
                'propagate': True,
            },
        },
    }

    # Configure logging
    logging.config.dictConfig(logging_config)

def load_environment_variables():
    # Load environment variables from .env file
    load_dotenv()

    # Access environment variables
    development_env = os.getenv('DEVELOPMENT_ENV')
    api_key = os.getenv('API_KEY')

    # Log the values
    logging.info(f"Development Environment: {development_env}")
    logging.info(f"API Key: {api_key}")

if __name__ == "__main__":
    setup_logging()
    load_environment_variables()
    logging.info("This is an info message")
    logging.error("This is an error message")

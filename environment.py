import os
import logging
from dotenv import load_dotenv

def setup_logging():
    # Ensure the logs directory exists
    os.makedirs('logs', exist_ok=True)

    # Configure logging
    logging.basicConfig(
        filename='logs/app.log',
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

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
    logging.error("This is an error message")

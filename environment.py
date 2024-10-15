from dotenv import load_dotenv
import os

def load_environment_variables():
    # Load environment variables from .env file
    load_dotenv()

    # Access environment variables
    development_env = os.getenv('DEVELOPMENT_ENV')
    api_key = os.getenv('API_KEY')

    # Log the values
    print(f"Development Environment: {development_env}")
    print(f"API Key: {api_key}")

if __name__ == "__main__":
    load_environment_variables()

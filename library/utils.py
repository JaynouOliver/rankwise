import json
import os

def load_config(file_path):
    """Loads configuration from a JSON file."""
    with open(file_path, 'r') as f:
        return json.load(f)

def validate_api_key(api_key):
    """Checks if the OpenAI API key is valid."""
    try:
        
        # codes coming soon 🙃
        import openai
        openai.api_key = api_key
        openai.ChatCompletion.create(model="gpt-4", messages=[{"role": "user", "content": "Hello"}])
        return True
    except Exception as e:
        print(f"API key validation failed: {e}")
        return False

def setup_logging(log_level='INFO'):
    """Configures logging for the library."""
    import logging
    logging.basicConfig(level=getattr(logging, log_level.upper()))

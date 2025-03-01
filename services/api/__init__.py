
"""
API services package initialization
"""
from services.api.openai import test_openai_connection
from services.api.gemini import test_gemini_connection
from services.api.deepseek import test_deepseek_connection


def test_api_connection(engine, api_key):
    """Test connection to the specified API
    
    Args:
        engine (str): Engine to test
        api_key (str): API key to use
        
    Returns:
        tuple: (success, message)
    """
    if engine == "OpenAI":
        return test_openai_connection(api_key)
    elif engine == "Gemini 2.0":
        return test_gemini_connection(api_key)
    elif engine == "DeepSeek V3":
        return test_deepseek_connection(api_key)
    else:
        return False, f"Unknown engine: {engine}"

"""
Gemini API integration for translation (simulated)
"""
import time
import random


def translate_with_gemini(text, context, api_key):
    """Translate text using Gemini API (simulated)
    
    Args:
        text (str): Text to translate
        context (str): Translation context
        api_key (str): Gemini API key
        
    Returns:
        tuple: (translated_text, token_count)
    """
    # Simulate API call delay
    time.sleep(1)
    
    # Simulate token usage based on input length
    token_count = len(text) // 4 + random.randint(10, 50)
    
    # For simulation, just return the original text with a prefix
    translated = f"[Gemini translation] {text}"
    
    return translated, token_count


def test_gemini_connection(api_key):
    """Test connection to Gemini API (simulated)
    
    Args:
        api_key (str): Gemini API key
        
    Returns:
        tuple: (success, message)
    """
    # Simulate API call delay
    time.sleep(0.5)
    
    # Check if API key looks valid (for simulation purposes)
    if len(api_key) < 5:
        return False, "Invalid API key format"
    
    # Simulate successful connection
    return True, "Connection successful"

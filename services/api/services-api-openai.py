"""
OpenAI API integration for translation
"""
import requests


def translate_with_openai(text, context, api_key):
    """Translate text using OpenAI API
    
    Args:
        text (str): Text to translate
        context (str): Translation context
        api_key (str): OpenAI API key
        
    Returns:
        tuple: (translated_text, token_count)
    """
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": context},
            {"role": "user", "content": text}
        ],
        "temperature": 0.3
    }
    
    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers=headers,
        json=payload,
        timeout=30
    )
    
    if response.status_code == 200:
        response_json = response.json()
        
        # Get token usage
        token_count = 0
        if "usage" in response_json:
            token_count = response_json["usage"]["total_tokens"]
            
        # Get translated text
        translated = response_json["choices"][0]["message"]["content"].strip()
        
        return translated, token_count
    else:
        # Extract error message from response
        error_message = f"Error {response.status_code}"
        try:
            error_json = response.json()
            if "error" in error_json and "message" in error_json["error"]:
                error_message = error_json["error"]["message"]
        except:
            if response.text:
                error_message = response.text[:100]
        
        raise Exception(f"OpenAI API Error: {error_message}")


def test_openai_connection(api_key):
    """Test connection to OpenAI API
    
    Args:
        api_key (str): OpenAI API key
        
    Returns:
        tuple: (success, message)
    """
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": "Test connection"}
        ],
        "max_tokens": 5
    }
    
    try:
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=10
        )
        
        if response.status_code == 200:
            return True, "Connection successful"
        else:
            error_message = f"Error {response.status_code}"
            try:
                error_json = response.json()
                if "error" in error_json and "message" in error_json["error"]:
                    error_message = error_json["error"]["message"]
            except:
                if response.text:
                    error_message = response.text[:100]
            
            return False, error_message
    
    except Exception as e:
        return False, str(e)

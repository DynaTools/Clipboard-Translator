
"""
OpenAI API integration for translation
"""
import requests


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

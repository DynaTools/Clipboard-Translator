"""
Translation service for text translation
"""
from services.api.openai import translate_with_openai
from services.api.gemini import translate_with_gemini
from services.api.deepseek import translate_with_deepseek


def translate_text(text, source_lang, target_lang, tone, context, engine, api_key):
    """Translate text using the specified engine
    
    Args:
        text (str): Text to translate
        source_lang (str): Source language
        target_lang (str): Target language
        tone (str): Translation tone
        context (str): Additional context for translation
        engine (str): Translation engine to use
        api_key (str): API key for the translation service
        
    Returns:
        tuple: (translated_text, token_count)
    """
    # Format the context if not provided
    if not context:
        context = f"Traduza de {source_lang} para {target_lang} em tom {tone}."
    else:
        context = f"{context} Traduza de {source_lang} para {target_lang} em tom {tone}."
    
    # Route to the appropriate translation service
    if engine == "OpenAI":
        return translate_with_openai(text, context, api_key)
    elif engine == "Gemini 2.0":
        return translate_with_gemini(text, context, api_key)
    elif engine == "DeepSeek V3":
        return translate_with_deepseek(text, context, api_key)
    else:
        # Default to OpenAI if engine not recognized
        return translate_with_openai(text, context, api_key)

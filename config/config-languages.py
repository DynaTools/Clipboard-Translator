"""
Language definitions for the translation application
"""

def get_languages():
    """Return a list of supported languages"""
    return [
        "Português",
        "Inglês",
        "Espanhol",
        "Francês", 
        "Italiano",
        "Alemão", 
        "Japonês", 
        "Chinês", 
        "Russo", 
        "Árabe",
        "Coreano",
        "Holandês",
        "Grego",
        "Sueco",
        "Hindi",
        "Turco"
    ]

# Mapping between language names and language codes
LANGUAGE_CODES = {
    "Português": "pt",
    "Inglês": "en",
    "Espanhol": "es",
    "Francês": "fr",
    "Italiano": "it",
    "Alemão": "de",
    "Japonês": "ja",
    "Chinês": "zh",
    "Russo": "ru",
    "Árabe": "ar",
    "Coreano": "ko",
    "Holandês": "nl",
    "Grego": "el",
    "Sueco": "sv",
    "Hindi": "hi",
    "Turco": "tr"
}

def get_language_code(language_name):
    """Convert a language name to a language code"""
    return LANGUAGE_CODES.get(language_name, "en")

def get_language_name(language_code):
    """Convert a language code to a language name"""
    for name, code in LANGUAGE_CODES.items():
        if code == language_code:
            return name
    return "Inglês"  # Default

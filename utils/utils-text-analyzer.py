"""
Text analysis utilities for clipboard content
"""


def is_code(text):
    """Detect if text appears to be code to avoid translating code
    
    Args:
        text (str): Text to analyze
        
    Returns:
        bool: True if text appears to be code, False otherwise
    """
    # Indicators of code content
    code_indicators = [
        "function", "def ", "class ", "import ", "<script", "<html",
        "{ }", "[]", "{}", "()", "headers", "payload", "const ", "var ",
        "let ", "=>", "->", "#include", "namespace", "public:", "private:",
        "@Override", "package ", "using ", "pragma", "typedef", "sudo ",
        "return ", "val ", "fun ", "interface ", "impl", "trait", "module"
    ]
    
    # Check for code indicators
    text_lower = text.lower()
    for indicator in code_indicators:
        if indicator in text_lower:
            return True
    
    # Check for high concentration of special characters
    symbols = sum(text.count(s) for s in ["{", "}", "[", "]", "(", ")", 
                                         "<", ">", ";", "=", "+", "-", 
                                         "*", "/", "\\", "|", "&", "^", 
                                         "%", "$", "#", "@", "!"])
    
    total_chars = len(text)
    if total_chars > 0 and (symbols / total_chars) > 0.08:  # 8% threshold
        return True
    
    # Check for indentation patterns common in code
    lines = text.split("\n")
    indented_lines = sum(1 for line in lines if line.startswith(("    ", "\t")))
    if len(lines) > 3 and indented_lines / len(lines) > 0.3:  # 30% of lines indented
        return True
    
    return False


def count_words(text):
    """Count words in text
    
    Args:
        text (str): Text to analyze
        
    Returns:
        int: Number of words
    """
    return len(text.split())


def detect_language(text):
    """Attempt to detect the language of text (simplified)
    
    Args:
        text (str): Text to analyze
        
    Returns:
        str: Detected language or "unknown"
    """
    # This is a very simplified language detection
    # In a real application, use a proper language detection library
    
    # Character sets that are distinctive for certain languages
    language_markers = {
        "Português": ["ção", "ões", "á", "é", "ê", "ã", "õ", "ç"],
        "Inglês": ["the", "and", "that", "have", "with"],
        "Espanhol": ["ción", "que", "ñ", "á", "é", "í", "ó", "ú"],
        "Francês": ["les", "des", "que", "dans", "est", "ê", "ç", "à", "â", "î", "ï"],
        "Italiano": ["gli", "sono", "che", "per", "questa"],
        "Alemão": ["der", "die", "das", "und", "ist", "ß", "ä", "ö", "ü"],
    }
    
    # Simple scoring system
    scores = {lang: 0 for lang in language_markers}
    
    text_lower = text.lower()
    
    for lang, markers in language_markers.items():
        for marker in markers:
            if marker in text_lower:
                scores[lang] += 1
    
    # Find language with highest score
    max_score = 0
    detected_lang = "unknown"
    
    for lang, score in scores.items():
        if score > max_score:
            max_score = score
            detected_lang = lang
    
    # Require a minimum score to make a determination
    if max_score < 2:
        return "unknown"
    
    return detected_lang

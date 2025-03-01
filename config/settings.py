"""
Settings manager for the Clipboard Translator
"""
import os
import json


class Settings:
    """Manages application settings and persistence"""
    
    CONFIG_FILE = "translator_config.json"
    
    def __init__(self):
        """Initialize settings with defaults"""
        # Default settings
        self.source_lang = "Português"
        self.target_lang = "Inglês"
        self.api_engine = "OpenAI"
        self.api_key = ""
        self.tone = "neutro"
        self.token_count = 0
        
        # Load existing settings if available
        self.load()
    
    def load(self):
        """Load settings from config file"""
        if not os.path.exists(self.CONFIG_FILE):
            return
            
        try:
            with open(self.CONFIG_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                
                # Update settings from file
                self.source_lang = data.get("source_lang", self.source_lang)
                self.target_lang = data.get("target_lang", self.target_lang)
                self.api_engine = data.get("api_engine", self.api_engine)
                self.api_key = data.get("api_key", self.api_key)
                self.tone = data.get("tone", self.tone)
                self.token_count = data.get("token_count", self.token_count)
        except Exception as e:
            print(f"Error loading settings: {str(e)}")
    
    def save(self):
        """Save settings to config file"""
        try:
            with open(self.CONFIG_FILE, "w", encoding="utf-8") as f:
                data = {
                    "source_lang": self.source_lang,
                    "target_lang": self.target_lang,
                    "api_engine": self.api_engine,
                    "api_key": self.api_key,
                    "tone": self.tone,
                    "token_count": self.token_count
                }
                json.dump(data, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {str(e)}")
    
    def reset(self):
        """Reset settings to default values"""
        self.source_lang = "Português"
        self.target_lang = "Inglês"
        self.api_engine = "OpenAI"
        self.api_key = ""
        self.tone = "neutro"
        self.token_count = 0
        
        # Save the reset settings
        self.save()
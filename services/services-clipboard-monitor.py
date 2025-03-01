"""
Clipboard monitoring service for the translator
"""
import threading
import time
import pyperclip

from services.translator import translate_text
from utils.text_analyzer import is_code


class ClipboardMonitor:
    """Monitors clipboard for text to translate"""
    
    def __init__(self, on_text_detected=None, on_translation_complete=None, on_error=None):
        """Initialize the clipboard monitor
        
        Args:
            on_text_detected: Callback when text is detected
            on_translation_complete: Callback when translation is complete
            on_error: Callback when an error occurs
        """
        self.on_text_detected = on_text_detected
        self.on_translation_complete = on_translation_complete
        self.on_error = on_error
        
        self.monitoring = False
        self.last_clipboard = ""
        self.monitor_thread = None
        
        # Translation settings
        self.api_key = ""
        self.source_lang = ""
        self.target_lang = ""
        self.tone = ""
        self.context = ""
        self.engine = ""
    
    def start(self, api_key, source_lang, target_lang, tone, context, engine):
        """Start monitoring the clipboard
        
        Args:
            api_key: API key for translation service
            source_lang: Source language
            target_lang: Target language
            tone: Translation tone
            context: Translation context
            engine: Translation engine
        """
        if self.monitoring:
            return
            
        # Set translation settings
        self.api_key = api_key
        self.source_lang = source_lang
        self.target_lang = target_lang
        self.tone = tone
        self.context = context
        self.engine = engine
        
        # Start monitoring
        self.monitoring = True
        self.monitor_thread = threading.Thread(target=self._monitor_loop)
        self.monitor_thread.daemon = True
        self.monitor_thread.start()
    
    def stop(self):
        """Stop monitoring the clipboard"""
        self.monitoring = False
        if self.monitor_thread:
            self.monitor_thread.join(timeout=1.0)
            self.monitor_thread = None
    
    def _monitor_loop(self):
        """Main monitoring loop"""
        while self.monitoring:
            try:
                # Get current clipboard content
                current_clipboard = pyperclip.paste()
                
                # Check if it's new content and not empty
                if (current_clipboard != self.last_clipboard and
                        current_clipboard.strip() and
                        not is_code(current_clipboard)):
                    
                    # Notify text detected
                    if self.on_text_detected:
                        self.on_text_detected(current_clipboard)
                    
                    # Translate text
                    translated, token_count = translate_text(
                        text=current_clipboard,
                        source_lang=self.source_lang,
                        target_lang=self.target_lang,
                        tone=self.tone,
                        context=self.context,
                        engine=self.engine,
                        api_key=self.api_key
                    )
                    
                    if translated:
                        # Store as last clipboard to prevent loops
                        self.last_clipboard = translated
                        
                        # Copy to clipboard
                        pyperclip.copy(translated)
                        
                        # Notify translation complete
                        if self.on_translation_complete:
                            self.on_translation_complete(
                                current_clipboard, translated, token_count)
            
            except Exception as e:
                # Notify error
                if self.on_error:
                    self.on_error(str(e))
            
            # Sleep to reduce CPU usage
            time.sleep(0.5)

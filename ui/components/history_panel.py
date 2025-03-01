"""
History panel component for tracking translations
"""
import tkinter as tk
from tkinter import ttk, scrolledtext
from datetime import datetime

class HistoryPanelComponent(ttk.LabelFrame):
    """Component for displaying translation history"""
    
    def __init__(self, parent):
        super().__init__(parent, text="Translation History", padding=10)
        
        # Top frame with buttons
        self.button_frame = ttk.Frame(self)
        self.button_frame.pack(fill=tk.X, pady=(0, 5))
        
        # Clear history button
        self.clear_btn = ttk.Button(
            self.button_frame,
            text="Clear History",
            command=self._clear_history
        )
        self.clear_btn.pack(side=tk.LEFT)
        
        # Copy last button
        self.copy_btn = ttk.Button(
            self.button_frame,
            text="Copy Last",
            command=self._copy_last_translation
        )
        self.copy_btn.pack(side=tk.RIGHT)
        
        # History text area
        self.history_text = scrolledtext.ScrolledText(
            self,
            height=6,
            wrap=tk.WORD,
            font=("Helvetica", 9)
        )
        self.history_text.pack(fill=tk.BOTH, expand=True)
        
        # Initialize history list
        self.history = []
    
    def add_entry(self, source_lang, target_lang, original, translated):
        """Add a new entry to the translation history"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        # Create a formatted entry
        entry = (
            f"[{timestamp}] {source_lang} → {target_lang}\n"
            f"Original: {original}\n"
            f"Translated: {translated}\n"
            f"{'-' * 60}\n"
        )
        
        # Add to internal history list
        self.history.append({
            'timestamp': timestamp,
            'source_lang': source_lang,
            'target_lang': target_lang,
            'original': original,
            'translated': translated
        })
        
        # Display in text area
        self.history_text.insert(tk.END, entry)
        self.history_text.see(tk.END)  # Scroll to the end
    
    def _clear_history(self):
        """Clear the translation history"""
        self.history = []
        self.history_text.delete(1.0, tk.END)
    
    def _copy_last_translation(self):
        """Copy the most recent translation to clipboard"""
        if not self.history:
            return
        
        last_entry = self.history[-1]
        translated_text = last_entry['translated']
        
        # Copy to clipboard
        self.clipboard_clear()
        self.clipboard_append(translated_text)
        
        # Flash the history text to indicate successful copy
        bg = self.history_text.cget("background")
        self.history_text.config(background="#e6ffe6")  # Light green flash
        self.after(200, lambda: self.history_text.config(background=bg))
    
    def get_history(self):
        """Get the translation history list"""
        return self.history
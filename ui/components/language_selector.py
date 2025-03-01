"""
Language selection component for translation
"""
import tkinter as tk
from tkinter import ttk
from config.languages import get_languages

class LanguageSelectorComponent(ttk.LabelFrame):
    """Component for selecting source and target languages"""
    
    def __init__(self, parent, on_swap=None):
        super().__init__(parent, text="Translation Languages", padding=10)
        
        self.on_swap = on_swap
        self.languages = get_languages()
        
        # Create language selection frame
        content_frame = ttk.Frame(self)
        content_frame.pack(fill=tk.X)
        
        # Source language
        source_frame = ttk.Frame(content_frame)
        source_frame.pack(side=tk.LEFT, fill=tk.Y, expand=True)
        
        ttk.Label(source_frame, text="Source Language").pack(anchor=tk.W, pady=(0, 5))
        
        self.source_lang = ttk.Combobox(
            source_frame,
            values=self.languages,
            state="readonly",
            width=15
        )
        self.source_lang.set("Português")
        self.source_lang.pack(fill=tk.X)
        
        # Arrows and swap button
        arrows_frame = ttk.Frame(content_frame, padding=(15, 0))
        arrows_frame.pack(side=tk.LEFT)
        
        # Add some vertical spacing for alignment
        ttk.Label(arrows_frame, text="").pack(pady=5)
        
        # Arrow label
        arrow_label = ttk.Label(arrows_frame, text="→", font=("Arial", 14))
        arrow_label.pack()
        
        # Swap button
        swap_button = ttk.Button(
            arrows_frame,
            text="⇄",
            width=3,
            command=self._swap_languages
        )
        swap_button.pack(pady=2)
        
        # Target language
        target_frame = ttk.Frame(content_frame)
        target_frame.pack(side=tk.RIGHT, fill=tk.Y, expand=True)
        
        ttk.Label(target_frame, text="Target Language").pack(anchor=tk.W, pady=(0, 5))
        
        self.target_lang = ttk.Combobox(
            target_frame,
            values=self.languages,
            state="readonly",
            width=15
        )
        self.target_lang.set("Inglês")
        self.target_lang.pack(fill=tk.X)
    
    def _swap_languages(self):
        """Swap source and target languages"""
        source = self.source_lang.get()
        target = self.target_lang.get()
        
        self.source_lang.set(target)
        self.target_lang.set(source)
        
        # Call the callback if provided
        if self.on_swap:
            self.on_swap()
    
    def get_source_language(self):
        """Get the current source language"""
        return self.source_lang.get()
    
    def get_target_language(self):
        """Get the current target language"""
        return self.target_lang.get()
    
    def set_source_language(self, language):
        """Set the source language"""
        if language in self.languages:
            self.source_lang.set(language)
    
    def set_target_language(self, language):
        """Set the target language"""
        if language in self.languages:
            self.target_lang.set(language)
"""
API configuration component for translation services
"""
import tkinter as tk
from tkinter import ttk, messagebox
import threading

from services.api import test_api_connection


class ApiConfigComponent(ttk.LabelFrame):
    """Component for API configuration and testing"""
    
    def __init__(self, parent, on_engine_change=None, on_test_connection=None):
        super().__init__(parent, text="AI Configuration", padding=10)
        
        self.on_engine_change = on_engine_change
        self.on_test_connection = on_test_connection
        
        # Container for the component content
        content_frame = ttk.Frame(self)
        content_frame.pack(fill=tk.X, expand=True)
        
        # Left side - AI Engine selector
        engine_frame = ttk.Frame(content_frame)
        engine_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 15))
        
        ttk.Label(engine_frame, text="AI Engine").pack(anchor=tk.W, pady=(0, 5))
        
        # AI engine selection
        self.available_engines = ['OpenAI', 'Gemini 2.0', 'DeepSeek V3']
        
        self.ai_engine = ttk.Combobox(
            engine_frame,
            values=self.available_engines,
            state="readonly",
            width=15
        )
        self.ai_engine.set(self.available_engines[0])
        self.ai_engine.pack(fill=tk.X, pady=(0, 10))
        self.ai_engine.bind("<<ComboboxSelected>>", self._on_engine_selected)
        
        # Token usage display
        token_frame = ttk.LabelFrame(engine_frame, text="Token Usage", padding=5)
        token_frame.pack(fill=tk.X, pady=(5, 0))
        
        self.token_display = ttk.Label(
            token_frame,
            text="0 tokens used this month",
            anchor=tk.CENTER
        )
        self.token_display.pack(fill=tk.X, pady=5)
        
        # Right side - API Key
        api_frame = ttk.Frame(content_frame)
        api_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        ttk.Label(api_frame, text="API Key").pack(anchor=tk.W, pady=(0, 5))
        
        # API input with toggle visibility
        api_input_frame = ttk.Frame(api_frame)
        api_input_frame.pack(fill=tk.X)
        
        self.api_entry = ttk.Entry(api_input_frame, show="*")
        self.api_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        # Visibility toggle button
        self.show_key = False
        self.toggle_btn = ttk.Button(
            api_input_frame,
            text="⌕",
            width=3,
            command=self._toggle_visibility
        )
        self.toggle_btn.pack(side=tk.RIGHT, padx=(5, 0))
        
        # Test API button
        test_button_frame = ttk.Frame(api_frame)
        test_button_frame.pack(fill=tk.X, pady=(10, 0), anchor=tk.E)
        
        self.test_button = ttk.Button(
            test_button_frame,
            text="Test Connection",
            command=self._test_connection,
            style="Primary.TButton"
        )
        self.test_button.pack(side=tk.RIGHT)
    
    def _toggle_visibility(self):
        """Toggle API key visibility"""
        self.show_key = not self.show_key
        if self.show_key:
            self.api_entry.config(show="")
            self.toggle_btn.config(text="●")
        else:
            self.api_entry.config(show="*")
            self
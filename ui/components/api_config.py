
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
            self.toggle_btn.config(text="⌕")
    
    def _on_engine_selected(self, event=None):
        """Handle engine selection event"""
        if self.on_engine_change:
            self.on_engine_change()
    
    def _test_connection(self):
        """Test the API connection with the current settings"""
        api_key = self.api_entry.get().strip()
        if not api_key:
            messagebox.showwarning("API Test", "Please enter an API key.")
            return
            
        engine = self.ai_engine.get()
        
        # Disable the test button during testing
        self.test_button.config(state=tk.DISABLED, text="Testing...")
        
        # Use threading to prevent UI freezing
        def test_connection():
            success, message = test_api_connection(engine, api_key)
            
            # Re-enable button in the main thread
            self.after(0, lambda: self.test_button.config(state=tk.NORMAL, text="Test Connection"))
            
            # Show result
            if success:
                self.after(0, lambda: messagebox.showinfo("API Test", "Connection successful!"))
            else:
                self.after(0, lambda: messagebox.showerror("API Test", f"Connection failed: {message}"))
            
            # Call the callback if provided
            if self.on_test_connection:
                self.after(0, lambda: self.on_test_connection(success, message))
        
        # Start the test in a separate thread
        thread = threading.Thread(target=test_connection)
        thread.daemon = True
        thread.start()
    
    def get_engine(self):
        """Get the current AI engine"""
        return self.ai_engine.get()
    
    def get_api_key(self):
        """Get the API key"""
        return self.api_entry.get().strip()
    
    def set_engine(self, engine):
        """Set the AI engine"""
        if engine in self.available_engines:
            self.ai_engine.set(engine)
    
    def set_api_key(self, api_key):
        """Set the API key"""
        self.api_entry.delete(0, tk.END)
        self.api_entry.insert(0, api_key)
    
    def update_token_count(self, count):
        """Update token usage display"""
        self.token_display.config(text=f"{count:,} tokens used this month")

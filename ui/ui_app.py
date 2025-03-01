"""
Main application window for Clipboard Translator AI
"""
import tkinter as tk
from tkinter import ttk

from ui.styles import apply_styles
from ui.components.header import HeaderComponent
from ui.components.language_selector import LanguageSelectorComponent
from ui.components.api_config import ApiConfigComponent
from ui.components.tone_selector import ToneSelectorComponent
from ui.components.context_editor import ContextEditorComponent
from ui.components.history_panel import HistoryPanelComponent
from ui.components.status_bar import StatusBarComponent

from services.clipboard_monitor import ClipboardMonitor
from config.settings import Settings


class TranslatorApp:
    """Main application class for Clipboard Translator AI"""
    
    def __init__(self, root):
        self.root = root
        self.settings = Settings()
        
        # Apply theme and styles
        self.style = apply_styles(root)
        
        # Create main frame with scrollbar
        self.main_container = ttk.Frame(root)
        self.main_container.pack(fill=tk.BOTH, expand=True)
        
        # Add a canvas for scrolling
        self.canvas = tk.Canvas(self.main_container)
        self.scrollbar = ttk.Scrollbar(self.main_container, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        
        # Add mousewheel scrolling
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        
        # Create main container with padding
        self.main_frame = ttk.Frame(self.scrollable_frame, padding="12 12 12 12")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Initialize UI components
        self._init_components()
        
        # Initialize clipboard monitor
        self.clipboard_monitor = ClipboardMonitor(
            self._on_text_detected,
            self._on_translation_complete,
            self._on_error
        )
        
        # Load saved settings
        self._load_settings()
    
    def _on_mousewheel(self, event):
        """Handle mousewheel scrolling"""
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
    def _init_components(self):
        """Initialize all UI components"""
        # Header with title and author info
        self.header = HeaderComponent(self.main_frame)
        self.header.pack(fill=tk.X, pady=(0, 10))
        
        # First row: Language selector and tone selector side by side
        first_row = ttk.Frame(self.main_frame)
        first_row.pack(fill=tk.X, pady=5)
        
        # Language selector (left side)
        left_frame = ttk.Frame(first_row)
        left_frame.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        
        self.lang_selector = LanguageSelectorComponent(
            left_frame, 
            on_swap=self._on_language_swap
        )
        self.lang_selector.pack(fill=tk.BOTH, expand=True)
        
        # Tone selector (right side)
        right_frame = ttk.Frame(first_row)
        right_frame.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=(5, 0))
        
        self.tone_selector = ToneSelectorComponent(right_frame)
        self.tone_selector.pack(fill=tk.BOTH, expand=True)
        
        # API Configuration
        self.api_config = ApiConfigComponent(
            self.main_frame,
            on_engine_change=self._on_engine_change,
            on_test_connection=self._on_test_connection
        )
        self.api_config.pack(fill=tk.X, pady=5)
        
        # Context editor with reduced height
        self.context_editor = ContextEditorComponent(
            self.main_frame,
            on_apply=self._on_context_apply
        )
        self.context_editor.pack(fill=tk.BOTH, expand=False, pady=5)
        
        # Control buttons (moved up before history panel)
        self._create_control_buttons()
        
        # Translation history with fixed height
        self.history_panel = HistoryPanelComponent(self.main_frame)
        self.history_panel.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Status bar
        self.status_bar = StatusBarComponent(self.root)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def _create_control_buttons(self):
        """Create control buttons for the application"""
        control_frame = ttk.Frame(self.main_frame)
        control_frame.pack(fill=tk.X, pady=5)
        
        # Create a grid layout for more consistent sizing and spacing
        control_frame.columnconfigure(0, weight=1)  # RESTART button column
        control_frame.columnconfigure(1, weight=1)  # STOP button column
        control_frame.columnconfigure(2, weight=2)  # Spacer column
        control_frame.columnconfigure(3, weight=1)  # RUN button column
        
        # Define buttons with consistent padding
        button_padding = 5
        
        self.restart_button = ttk.Button(
            control_frame, 
            text="RESTART", 
            command=self.restart_app,
            style="Secondary.TButton"
        )
        self.restart_button.grid(row=0, column=0, padx=button_padding, pady=5, sticky="ew")
        
        self.stop_button = ttk.Button(
            control_frame, 
            text="STOP", 
            command=self.stop_monitoring,
            state=tk.DISABLED,
            style="Danger.TButton"
        )
        self.stop_button.grid(row=0, column=1, padx=button_padding, pady=5, sticky="ew")
        
        self.run_button = ttk.Button(
            control_frame, 
            text="RUN", 
            command=self.start_monitoring,
            style="Primary.TButton"
        )
        self.run_button.grid(row=0, column=3, padx=button_padding, pady=5, sticky="ew")
    
    def _load_settings(self):
        """Load saved settings into UI components"""
        # Load source and target languages
        if self.settings.source_lang:
            self.lang_selector.set_source_language(self.settings.source_lang)
        if self.settings.target_lang:
            self.lang_selector.set_target_language(self.settings.target_lang)
            
        # Load API settings
        if self.settings.api_engine:
            self.api_config.set_engine(self.settings.api_engine)
        if self.settings.api_key:
            self.api_config.set_api_key(self.settings.api_key)
            
        # Load tone setting
        if self.settings.tone:
            self.tone_selector.set_tone(self.settings.tone)
            
        # Update token usage display
        self.api_config.update_token_count(self.settings.token_count)
    
    def _save_settings(self):
        """Save current settings to config file"""
        self.settings.source_lang = self.lang_selector.get_source_language()
        self.settings.target_lang = self.lang_selector.get_target_language()
        self.settings.api_engine = self.api_config.get_engine()
        self.settings.api_key = self.api_config.get_api_key()
        self.settings.tone = self.tone_selector.get_tone()
        self.settings.save()
    
    def start_monitoring(self):
        """Start monitoring the clipboard"""
        # Validate API key
        api_key = self.api_config.get_api_key()
        if not api_key:
            self.status_bar.show_error("Please enter an API key")
            return
            
        # Save current settings
        self._save_settings()
        
        # Update UI state
        self.run_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        
        # Start monitoring
        source_lang = self.lang_selector.get_source_language()
        target_lang = self.lang_selector.get_target_language()
        tone = self.tone_selector.get_tone()
        context = self.context_editor.get_context()
        engine = self.api_config.get_engine()
        
        self.clipboard_monitor.start(
            api_key=api_key,
            source_lang=source_lang,
            target_lang=target_lang,
            tone=tone,
            context=context,
            engine=engine
        )
        
        self.status_bar.set_status(
            f"Monitoring clipboard ({source_lang} → {target_lang}, tone: {tone})")
    
    def stop_monitoring(self):
        """Stop monitoring the clipboard"""
        self.clipboard_monitor.stop()
        
        # Update UI state
        self.run_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.status_bar.set_status("Stopped")
    
    def restart_app(self):
        """Restart the application"""
        self.stop_monitoring()
        self._save_settings()
        
        # Use Python's exec to restart the application
        import sys
        import os
        python = sys.executable
        os.execl(python, python, *sys.argv)
    
    def on_close(self):
        """Handle window close event"""
        self.stop_monitoring()
        self._save_settings()
        self.root.destroy()
    
    # Event handlers
    def _on_language_swap(self):
        """Handle language swap event"""
        pass  # Already handled by the language selector
    
    def _on_engine_change(self):
        """Handle API engine change event"""
        pass  # Updates handled by components
    
    def _on_test_connection(self, success, message):
        """Handle API connection test result"""
        if success:
            self.status_bar.set_status("API connection successful")
        else:
            self.status_bar.show_error(f"API connection failed: {message}")
    
    def _on_context_apply(self):
        """Handle context application event"""
        self.status_bar.set_status("Context applied for translations")
    
    def _on_text_detected(self, text):
        """Handle detected clipboard text"""
        self.status_bar.set_status("Translating...")
        
    def _on_translation_complete(self, original, translated, token_count):
        """Handle completed translation"""
        # Update token count
        self.settings.token_count += token_count
        self.api_config.update_token_count(self.settings.token_count)
        
        # Add to history
        source = self.lang_selector.get_source_language()
        target = self.lang_selector.get_target_language()
        self.history_panel.add_entry(source, target, original, translated)
        
        # Update status
        self.status_bar.set_status("Translation complete")
    
    def _on_error(self, error_message):
        """Handle translation error"""
        self.status_bar.show_error(error_message)

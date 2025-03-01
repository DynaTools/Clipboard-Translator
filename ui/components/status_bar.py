"""
Status bar component for displaying application status
"""
import tkinter as tk
from tkinter import ttk


class StatusBarComponent(ttk.Frame):
    """Status bar component for the application"""
    
    def __init__(self, parent):
        super().__init__(parent)
        
        # Status variable
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        
        # Status label
        self.status_label = ttk.Label(
            self,
            textvariable=self.status_var,
            style="Status.TLabel",
            anchor=tk.W,
            padding=(10, 5)
        )
        self.status_label.pack(fill=tk.X)
        
        # Default status color
        self.normal_fg = self.status_label.cget("foreground")
        self.error_fg = "#e74c3c"  # Red color for errors
    
    def set_status(self, message):
        """Set the status message"""
        self.status_var.set(message)
        # Reset to normal color
        self.status_label.configure(foreground=self.normal_fg)
    
    def show_error(self, message):
        """Show an error message in the status bar"""
        self.status_var.set(f"Error: {message}")
        # Set error color
        self.status_label.configure(foreground=self.error_fg)
    
    def clear(self):
        """Clear the status bar"""
        self.status_var.set("")
        # Reset to normal color
        self.status_label.configure(foreground=self.normal_fg)
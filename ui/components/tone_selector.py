
"""
Tone selection component for translation
"""
import tkinter as tk
from tkinter import ttk


class ToneSelectorComponent(ttk.LabelFrame):
    """Component for selecting translation tone"""
    
    def __init__(self, parent):
        super().__init__(parent, text="Translation Tone", padding=10)
        
        self.tone_var = tk.StringVar(value="neutro")
        
        # Create a more modern-looking tone selector with better spacing
        content_frame = ttk.Frame(self)
        content_frame.pack(fill=tk.X)
        
        # Create radio buttons with consistent spacing
        tones = [
            ("Neutro", "neutro"),
            ("Formal", "formal"),
            ("Técnico", "técnico"),
            ("Coloquial", "coloquial")
        ]
        
        # Use a grid layout for better control
        for i, (text, value) in enumerate(tones):
            radio = ttk.Radiobutton(
                content_frame,
                text=text,
                variable=self.tone_var,
                value=value,
                padding=(10, 5)
            )
            radio.grid(row=0, column=i, padx=10, sticky=tk.W)
        
        # Configure the grid to expand evenly
        for i in range(len(tones)):
            content_frame.columnconfigure(i, weight=1)
    
    def get_tone(self):
        """Get the current tone selection"""
        return self.tone_var.get()
    
    def set_tone(self, tone):
        """Set the tone selection"""
        self.tone_var.set(tone)

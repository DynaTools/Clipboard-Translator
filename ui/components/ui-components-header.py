"""
Header component with title and author info
"""
import tkinter as tk
from tkinter import ttk
import webbrowser


class HeaderComponent(ttk.Frame):
    """Header component with title, logo and author info"""
    
    def __init__(self, parent):
        super().__init__(parent)
        
        # Create logo image if available
        try:
            self.logo_img = tk.PhotoImage(file="assets/logo.png")
            self.logo_img = self.logo_img.subsample(4, 4)  # Scale down the logo
            logo_label = ttk.Label(self, image=self.logo_img)
            logo_label.pack(side=tk.LEFT, padx=(0, 10))
        except:
            # No logo available, continue without it
            pass
        
        # App title with custom styling
        title_frame = ttk.Frame(self)
        title_frame.pack(side=tk.LEFT, fill=tk.Y)
        
        title_label = ttk.Label(
            title_frame, 
            text="CLIPBOARD TRANSLATOR AI", 
            style="Header.TLabel"
        )
        title_label.pack(anchor=tk.W)
        
        # Author info with LinkedIn button
        author_frame = ttk.Frame(title_frame)
        author_frame.pack(anchor=tk.W, fill=tk.X)
        
        author_label = ttk.Label(
            author_frame, 
            text="by Paulo A. Giavoni", 
            style="Subheader.TLabel"
        )
        author_label.pack(side=tk.LEFT)
        
        # LinkedIn button with custom styling
        linkedin_button = tk.Button(
            author_frame, 
            text="in", 
            font=("Arial", 9, "bold"),
            bg="#0077B5", 
            fg="white",
            width=2, 
            height=1,
            relief=tk.FLAT,
            command=self._open_linkedin
        )
        linkedin_button.pack(side=tk.LEFT, padx=(10, 0))
    
    def _open_linkedin(self):
        """Open LinkedIn profile in default browser"""
        webbrowser.open("https://www.linkedin.com/in/paulogiavoni/")

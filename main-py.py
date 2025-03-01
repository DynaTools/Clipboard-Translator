"""
Clipboard Translator AI - Main Entry Point
Author: Paulo A. Giavoni
"""
import tkinter as tk
from ui.app import TranslatorApp

def main():
    """Initialize and start the application"""
    root = tk.Tk()
    root.title("Clipboard Translator AI")
    
    # Set minimum window size
    root.minsize(640, 700)
    
    # Set icon if available
    try:
        root.iconphoto(True, tk.PhotoImage(file='assets/logo.png'))
    except:
        pass
    
    app = TranslatorApp(root)
    
    # Set up keyboard shortcuts
    root.bind("<Control-r>", lambda event: app.start_monitoring())
    root.bind("<Control-s>", lambda event: app.stop_monitoring())
    
    # Handle window close
    root.protocol("WM_DELETE_WINDOW", app.on_close)
    
    # Start the application
    root.mainloop()

if __name__ == "__main__":
    main()

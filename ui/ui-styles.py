"""
Styles and themes for the Clipboard Translator UI
"""
import tkinter as tk
from tkinter import ttk

def apply_styles(root):
    """Apply custom styles to the application"""
    style = ttk.Style()
    
    # Color palette
    colors = {
        'primary': '#3498db',        # Blue
        'primary_dark': '#2980b9',
        'secondary': '#95a5a6',      # Light gray
        'secondary_dark': '#7f8c8d',
        'success': '#2ecc71',        # Green
        'success_dark': '#27ae60',
        'danger': '#e74c3c',         # Red
        'danger_dark': '#c0392b',
        'warning': '#f39c12',        # Orange
        'warning_dark': '#d35400',
        'background': '#f8f9fa',     # Light background
        'card_bg': '#ffffff',        # Card background
        'text': '#2c3e50',           # Dark text
        'text_light': '#7f8c8d',     # Light text
        'border': '#dfe6e9'          # Border color
    }
    
    # Configure Tkinter default colors
    root.configure(background=colors['background'])
    
    # Configure ttk styles
    style.configure('TFrame', background=colors['background'])
    style.configure('Card.TFrame', background=colors['card_bg'], 
                   relief=tk.RAISED, borderwidth=1)
    
    # Configure Label styles
    style.configure('TLabel', background=colors['background'], 
                   foreground=colors['text'], font=('Helvetica', 10))
    style.configure('Header.TLabel', font=('Helvetica', 16, 'bold'), 
                   foreground=colors['primary'])
    style.configure('Subheader.TLabel', font=('Helvetica', 12),
                   foreground=colors['text'])
    style.configure('Status.TLabel', background=colors['card_bg'],
                   foreground=colors['text_light'], padding=5)
    
    # Configure Button styles
    style.configure('TButton', font=('Helvetica', 10), padding=5)
    
    style.configure('Primary.TButton', 
                   background=colors['primary'],
                   foreground='white')
    style.map('Primary.TButton',
             background=[('active', colors['primary_dark'])])
    
    style.configure('Secondary.TButton', 
                   background=colors['secondary'],
                   foreground='white')
    style.map('Secondary.TButton',
             background=[('active', colors['secondary_dark'])])
    
    style.configure('Success.TButton', 
                   background=colors['success'],
                   foreground='white')
    style.map('Success.TButton',
             background=[('active', colors['success_dark'])])
    
    style.configure('Danger.TButton', 
                   background=colors['danger'],
                   foreground='white')
    style.map('Danger.TButton',
             background=[('active', colors['danger_dark'])])
    
    style.configure('Warning.TButton', 
                   background=colors['warning'],
                   foreground='white')
    style.map('Warning.TButton',
             background=[('active', colors['warning_dark'])])
    
    # Configure Combobox styles
    style.configure('TCombobox', 
                   fieldbackground=colors['card_bg'],
                   background=colors['background'])
    
    # Configure Frame with padding
    style.configure('Padded.TFrame', padding=10)
    
    # Configure LabelFrame
    style.configure('TLabelframe', 
                   background=colors['background'],
                   foreground=colors['text'])
    style.configure('TLabelframe.Label', 
                   background=colors['background'],
                   foreground=colors['primary'],
                   font=('Helvetica', 10, 'bold'))
    
    # Separator style
    style.configure('TSeparator', background=colors['border'])
    
    return style

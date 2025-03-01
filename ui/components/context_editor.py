"""
Context editor component for translation prompts
"""
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import os

class ContextEditorComponent(ttk.LabelFrame):
    """Component for editing and managing translation context"""
    
    def __init__(self, parent, on_apply=None):
        super().__init__(parent, text="Context & Grammar", padding=10)
        
        self.on_apply = on_apply
        
        # Text area for context editing
        self.context_text = scrolledtext.ScrolledText(
            self,
            height=7,
            wrap=tk.WORD,
            font=("Helvetica", 10)
        )
        self.context_text.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Default context text
        default_context = "Traduza o texto mantendo o mesmo significado e contexto."
        self.context_text.insert(tk.END, default_context)
        
        # Buttons for context actions
        button_frame = ttk.Frame(self)
        button_frame.pack(fill=tk.X)
        
        # Load template button
        self.load_btn = ttk.Button(
            button_frame,
            text="Load Template",
            command=self._load_template
        )
        self.load_btn.pack(side=tk.LEFT, padx=(0, 5))
        
        # Save template button
        self.save_btn = ttk.Button(
            button_frame,
            text="Save Template",
            command=self._save_template
        )
        self.save_btn.pack(side=tk.LEFT, padx=5)
        
        # Clear button
        self.clear_btn = ttk.Button(
            button_frame,
            text="Clear",
            command=self._clear_context
        )
        self.clear_btn.pack(side=tk.LEFT, padx=5)
        
        # Apply button
        self.apply_btn = ttk.Button(
            button_frame,
            text="Apply Context",
            command=self._apply_context,
            style="Primary.TButton"
        )
        self.apply_btn.pack(side=tk.RIGHT)
    
    def _clear_context(self):
        """Clear the context text area"""
        self.context_text.delete(1.0, tk.END)
    
    def _save_template(self):
        """Save the current context as a template"""
        content = self.context_text.get(1.0, tk.END).strip()
        if not content:
            messagebox.showwarning("Warning", "Context is empty")
            return
            
        try:
            with open("context_template.txt", "w", encoding="utf-8") as f:
                f.write(content)
            messagebox.showinfo("Success", "Context saved as 'context_template.txt'")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save template: {str(e)}")
    
    def _load_template(self):
        """Load a context template from file"""
        if not os.path.exists("context_template.txt"):
            messagebox.showinfo("Info", "No template file found")
            return
            
        try:
            with open("context_template.txt", "r", encoding="utf-8") as f:
                content = f.read()
                
            self._clear_context()
            self.context_text.insert(tk.END, content)
        except Exception as e:
            messagebox.showerror("Error", f"Could not load template: {str(e)}")
    
    def _apply_context(self):
        """Apply the current context for translations"""
        if self.on_apply:
            self.on_apply()
    
    def get_context(self):
        """Get the current context text"""
        return self.context_text.get(1.0, tk.END).strip()
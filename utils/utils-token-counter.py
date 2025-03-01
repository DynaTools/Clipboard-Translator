"""
Token usage tracking utilities
"""
import os
import json
from datetime import datetime, date


class TokenCounter:
    """Track token usage across sessions"""
    
    USAGE_FILE = "token_usage.json"
    
    def __init__(self):
        self.monthly_usage = {}
        self.load_usage()
    
    def load_usage(self):
        """Load usage data from file"""
        if not os.path.exists(self.USAGE_FILE):
            self.monthly_usage = {}
            return
            
        try:
            with open(self.USAGE_FILE, "r", encoding="utf-8") as f:
                self.monthly_usage = json.load(f)
        except Exception as e:
            print(f"Error loading token usage: {str(e)}")
            self.monthly_usage = {}
    
    def save_usage(self):
        """Save usage data to file"""
        try:
            with open(self.USAGE_FILE, "w", encoding="utf-8") as f:
                json.dump(self.monthly_usage, f, indent=4)
        except Exception as e:
            print(f"Error saving token usage: {str(e)}")
    
    def add_tokens(self, count, engine="OpenAI"):
        """Add token usage for current month
        
        Args:
            count (int): Number of tokens used
            engine (str): AI engine used
        """
        # Get current month key
        current_month = date.today().strftime("%Y-%m")
        
        # Initialize if needed
        if current_month not in self.monthly_usage:
            self.monthly_usage[current_month] = {}
        
        if engine not in self.monthly_usage[current_month]:
            self.monthly_usage[current_month][engine] = 0
        
        # Add token count
        self.monthly_usage[current_month][engine] += count
        
        # Save updated usage
        self.save_usage()
    
    def get_current_month_usage(self, engine=None):
        """Get token usage for current month
        
        Args:
            engine (str, optional): AI engine to filter by
            
        Returns:
            int: Token count for current month
        """
        current_month = date.today().strftime("%Y-%m")
        
        if current_month not in self.monthly_usage:
            return 0
        
        if engine:
            return self.monthly_usage[current_month].get(engine, 0)
        else:
            return sum(self.monthly_usage[current_month].values())
    
    def get_total_usage(self, engine=None):
        """Get total token usage across all months
        
        Args:
            engine (str, optional): AI engine to filter by
            
        Returns:
            int: Total token count
        """
        total = 0
        
        for month, engines in self.monthly_usage.items():
            if engine:
                total += engines.get(engine, 0)
            else:
                total += sum(engines.values())
        
        return total
    
    def get_usage_by_month(self, engine=None):
        """Get token usage breakdown by month
        
        Args:
            engine (str, optional): AI engine to filter by
            
        Returns:
            dict: Monthly token usage
        """
        if engine:
            return {
                month: engines.get(engine, 0)
                for month, engines in self.monthly_usage.items()
            }
        else:
            return {
                month: sum(engines.values())
                for month, engines in self.monthly_usage.items()
            }

from datetime import datetime
class Note:
    """
        a class for a Note object, containing fields code, text, and timestamp
    """
    def __init__(self, code: int, text: str, timestamp: datetime = None):
        
        self.code = code
        self.text = text
        self.timestamp = timestamp or datetime.now() # you can choose the timestamp, but is current date if not specified
    
    def __eq__(self, other): 
        return ((self.code == other.code) and (self.text == other.text))
    
    def __str__(self):
        return f"Note {self.code}: {self.text}, timestamp: {self.timestamp}"
    
    def __repr__(self):
        return f"Note(code = {self.code}, text = {self.text}, timestamp = {self.timestamp})"
    
    

    
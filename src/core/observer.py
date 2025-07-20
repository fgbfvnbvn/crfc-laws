from datetime import datetime
from typing import Dict, List

class Observer:
    """Implementation of Observer mechanics"""
    
    def __init__(self, name: str, state: Dict):
        self.name = name
        self.state = state
        self.measurements = []
    
    def measure(self, system) -> Dict:
        """Perform measurement on a system"""
        pass
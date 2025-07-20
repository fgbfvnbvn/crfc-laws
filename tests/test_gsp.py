import unittest
from datetime import datetime
from src.analysis.gsp_detector import GSPDetector

class TestGSPDetection(unittest.TestCase):
    def setUp(self):
        self.detector = GSPDetector()
        
    def test_gsp_state_detection(self):
        state = {
            'attention': 0.3,
            'relaxation': 0.8,
            'context': 'smoke_break'
        }
        context = {
            'location': 'outdoor',
            'time': datetime.now(),
            'previous_activity': 'coding'
        }
        
        result = self.detector.analyze_state(state, context)
        self.assertTrue('is_gsp_state' in result)
        self.assertTrue('metrics' in result)
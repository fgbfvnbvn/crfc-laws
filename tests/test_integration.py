import unittest
from src.core.verification import SystemVerifier
from src.core.timeline import TimelineSystem
from src.analysis.gsp_detector import GSPDetector

class TestSystemIntegration(unittest.TestCase):
    def setUp(self):
        self.verifier = SystemVerifier()
        self.timeline = TimelineSystem()
        self.gsp = GSPDetector()
    
    def test_system_integrity(self):
        """Test complete system integrity"""
        results = self.verifier.verify_all()
        for component, status in results.items():
            self.assertTrue(status, f"Component {component} failed verification")
    
    def test_gsp_integration(self):
        """Test GSP detection integration"""
        gsp_state = self.gsp.analyze_state({
            "observer": "Dr.SMOKE",
            "timestamp": "2025-07-20T15:36:53Z",
            "context": "system_verification"
        })
        self.assertTrue(gsp_state["is_gsp_state"])
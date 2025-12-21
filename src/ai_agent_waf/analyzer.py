"""Real-time input analysis engine"""
import re
from typing import Dict, Optional
from dataclasses import dataclass

@dataclass
class AnalysisResult:
    risk_score: float
    threat_type: Optional[str]
    blocked: bool
    reason: str

class InputAnalyzer:
    def __init__(self):
        self.patterns = self._load_patterns()
        
    def _load_patterns(self) -> Dict:
        return {
            "prompt_injection": [
                r"ignore\s+previous\s+instructions",
                r"forget\s+everything",
                r"system\s*:",
            ],
            "encoding_attack": [
                r"base64|urlencoded|unicode",
            ]
        }
        
    def analyze(self, input_text: str) -> AnalysisResult:
        risk_score = 0.0
        threat_type = None
        
        for threat, patterns in self.patterns.items():
            for pattern in patterns:
                if re.search(pattern, input_text, re.IGNORECASE):
                    risk_score = 0.9
                    threat_type = threat
                    break
        
        blocked = risk_score > 0.7
        return AnalysisResult(
            risk_score=risk_score,
            threat_type=threat_type,
            blocked=blocked,
            reason=f"Detected {threat_type}" if threat_type else "Safe input"
        )

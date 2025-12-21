"""Input blocking and response system"""
from .analyzer import InputAnalyzer, AnalysisResult

class InputBlocker:
    def __init__(self):
        self.analyzer = InputAnalyzer()
        
    def process_input(self, input_text: str) -> tuple[bool, AnalysisResult]:
        """Process input and determine if it should be blocked"""
        result = self.analyzer.analyze(input_text)
        return result.blocked, result

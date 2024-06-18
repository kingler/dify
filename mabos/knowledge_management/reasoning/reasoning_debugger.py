import os
import sys
from typing import List, Dict, Any

from reasoning_engine import ReasoningEngine
from reasoning_explainer import ReasoningExplained

class ReasoningDebugger:
    def __init__(self, engine: ReasoningEngine):
        self.engine = engine
        self.explained = ReasoningExplained(engine)

    def debug_reasoning(self, query: str, facts: List[str]) -> Dict[str, Any]:
        result = self.engine.reason(query, facts)
        explanation = self.explained.explain_reasoning(query, facts)
        
        debug_info = {
            "query": query,
            "facts": facts,
            "result": result,
            "explanation": explanation
        }
        
        return debug_info
        
    def print_debug_info(self, debug_info: Dict[str, Any]):
        print(f"Query: {debug_info['query']}")
        print(f"Facts: {debug_info['facts']}")
        print(f"Result: {debug_info['result']}")
        print(f"Explanation: {debug_info['explanation']}")

if __name__ == "__main__":
    engine = ReasoningEngine()
    debugger = ReasoningDebugger(engine)

    query = "What is the capital of France?"
    facts = [
        "Paris is the capital of France.",
        "France is a country in Europe."
    ]

    debug_info = debugger.debug_reasoning(query, facts)
    debugger.print_debug_info(debug_info)

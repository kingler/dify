from typing import Dict, List


class Beliefs:
    def __init__(self):
        self.user_preferences: Dict[str, List[str]] = {}
        self.user_goals: Dict[str, List[str]] = {}
        self.user_feedback: Dict[str, List[str]] = {}
        self.business_models: Dict[str, Dict[str, str]] = {}
        self.product_descriptions: Dict[str, Dict[str, str]] = {}
        
        
    def update_beliefs(self, user_id: str, data: Dict[str, List[str]]):
        for key, value in data.items():
            if key == "user_preferences":
                self.beliefs.user_preferences[user_id] = value
            elif key == "user_goals":
                self.beliefs.user_goals[user_id] = value
            elif key == "user_feedback":
                self.beliefs.user_feedback[user_id] = value
            elif key == "business_models":
                self.beliefs.business_models[user_id] = value
            elif key == "product_descriptions":
                self.beliefs.product_descriptions[user_id] = value

class Desires:
    def __init__(self):
        self.user_preferences: List[str] = []
        self.user_goals: List[str] = []
        self.business_models: List[str] = []
        self.product_descriptions: List[str] = []
   
    def generate_desires(self, user_id: str):
        self.desires.user_preferences = self.beliefs.user_preferences[user_id]
        self.desires.user_goals = self.beliefs.user_goals[user_id]
        self.desires.business_models = list(self.beliefs.business_models[user_id].keys())
        self.desires.product_descriptions = list(self.beliefs.product_descriptions[user_id].keys())
   
        
class Intentions:
    def __init__(self):
        self.onboarding_steps: List[str] = []
        
        
        
        
   

    
    

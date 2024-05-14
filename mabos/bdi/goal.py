from pydantic import BaseModel, Field
from typing import List
from knowledge import Ontology
from action import Action

class Goal(BaseModel):
    name: str
    description: str
    priority: int
    subgoals: List['Goal'] = Field(default_factory=list)
    actions: List[Action] = Field(default_factory=list)

    def add_subgoal(self, subgoal: 'Goal'):
        self.subgoals.append(subgoal)

    def add_action(self, action: Action):
        self.actions.append(action)

    def reason_and_update(self, ontology: Ontology):
        # Perform reasoning based on the ontology and update the goal
        pass


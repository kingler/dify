from pydantic import BaseModel
from typing import List

from ..ontology import Ontology
from ..knowledge import KnowledgeGraph
from bdi.plans import Plan
from ..tasks import Task
from ..action import Action
from owlrl import DeductiveClosure

class Reasoning(BaseModel):
    ontology: Ontology
    knowledge_graph: KnowledgeGraph
    
    def __init__(self, ontology, knowledge_graph):
        self.ontology = ontology
        self.knowledge_graph = knowledge_graph

    def reason(self, plan: Plan, task: Task, action: Action, user, onboarding_step):
        reasoning_methods = self.select_reasoning_methods(plan, task, action)
        for method in reasoning_methods:
            getattr(self, f"{method}_reasoning")(plan, task, action, user, onboarding_step)

    def user_preference_reasoning(self, user):
        user_preferences = self.knowledge_graph.query(f"SELECT ?preference WHERE {{ ?user :hasPreference ?preference . ?user :userId '{user.id}' }}")
        # Process user preferences
        return user_preferences

    def update_knowledge_graph(self, data):
        for item in data:
            self.knowledge_graph.update(f"INSERT DATA {{ {item} }}")

    def update_entities_with_conclusions(self, plan, task, action, conclusions):
        updated_plan = self.update_plan_with_conclusions(plan, conclusions)
        updated_task = self.update_task_with_conclusions(task, conclusions)
        updated_action = self.update_action_with_conclusions(action, conclusions)
        return updated_plan, updated_task, updated_action

    def select_reasoning_methods(self, plan, task, action):
         # Example logic to select appropriate reasoning methods
        methods = ["user_preference"]
        if plan.name == "Strategic Plan":
            methods.append("strategic_decision_making")
        if task.name == "Market Analysis":
            methods.append("operational_optimization")
        if action.name == "Competitor Analysis":
            methods.append("risk_assessment")
        return methods

    def update_plan_with_conclusions(self, plan: Plan, conclusions: List[str]) -> Plan:
        # Example logic to update plan with conclusions
        for conclusion in conclusions:
            plan.details += f"\nConclusion: {conclusion}"
        return plan

    def update_task_with_conclusions(self, task: Task, conclusions: List[str]) -> Task:
        # Example logic to update task with conclusions
        for conclusion in conclusions:
            task.details += f"\nConclusion: {conclusion}"
        return task

    def update_action_with_conclusions(self, action: Action, conclusions: List[str]) -> Action:
        # Example logic to update action with conclusions
        for conclusion in conclusions:
            action.details += f"\nConclusion: {conclusion}"
        return action

# Example definitions for ontology and knowledge graph
my_ontology = Ontology()  # Initialize your Ontology instance
my_knowledge_graph = KnowledgeGraph()  # Initialize your KnowledgeGraph instance

# Initialize Reasoning with ontology and knowledge graph
reasoning = Reasoning(ontology=my_ontology, knowledge_graph=my_knowledge_graph)

# Define a plan, task, and action
plan = Plan(name="Strategic Plan")
task = Task(name="Market Analysis")
action = Action(name="Competitor Analysis")

# Apply reasoning
reasoning.reason(plan, task, action, user=my_user, onboarding_step=my_onboarding_step)
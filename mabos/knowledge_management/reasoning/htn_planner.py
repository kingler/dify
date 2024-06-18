import json
from typing import List, Dict, Any

from ...goal_management.goal import Goal
from goal_plan_tree import GoalPlanTree
from htn_planner import HTNPlanner
from reasoning_engine import ReasoningEngine
from reasoning_explainer import ReasoningExplainer
from skills import Skill

class CaseBasedReasoner:
    def __init__(self, htn_planner: HTNPlanner, reasoning_engine: ReasoningEngine, reasoning_explainer: ReasoningExplainer):
        self.htn_planner = htn_planner
        self.reasoning_engine = reasoning_engine
        self.reasoning_explainer = reasoning_explainer
        self.case_base: List[Dict[str, Any]] = []

    def load_case_base(self, file_path: str):
        with open(file_path, 'r') as f:
            self.case_base = json.load(f)

    def save_case_base(self, file_path: str):
        with open(file_path, 'w') as f:
            json.dump(self.case_base, f, indent=2)

    def retrieve_cases(self, goal: Goal) -> List[Dict[str, Any]]:
        # Retrieve relevant cases from the case base based on the goal
        relevant_cases = [case for case in self.case_base if case['goal'] == goal.to_dict()]
        return relevant_cases

    def adapt_case(self, case: Dict[str, Any], current_state: Dict[str, Any]) -> GoalPlanTree:
        # Adapt the retrieved case to the current state
        adapted_goal_plan_tree = GoalPlanTree.from_dict(case['goal_plan_tree'])
        # Modify the adapted_goal_plan_tree based on the current_state
        return adapted_goal_plan_tree

    def execute_plan(self, goal_plan_tree: GoalPlanTree) -> bool:
        # Execute the adapted plan using the HTN planner
        success = self.htn_planner.execute_plan(goal_plan_tree)
        return success

    def store_case(self, goal: Goal, goal_plan_tree: GoalPlanTree):
        # Store the new case in the case base
        new_case = {
            'goal': goal.to_dict(),
            'goal_plan_tree': goal_plan_tree.to_dict()
        }
        self.case_base.append(new_case)

    def reason(self, goal: Goal, current_state: Dict[str, Any]) -> bool:
        # Retrieve relevant cases from the case base
        relevant_cases = self.retrieve_cases(goal)

        if relevant_cases:
            # Adapt the most similar case to the current state
            adapted_goal_plan_tree = self.adapt_case(relevant_cases[0], current_state)

            # Execute the adapted plan
            success = self.execute_plan(adapted_goal_plan_tree)

            if success:
                # Store the new case in the case base
                self.store_case(goal, adapted_goal_plan_tree)
                return True
            else:
                # If the adapted plan fails, fall back to the HTN planner
                return self.htn_planner.plan_and_execute(goal, current_state)
        else:
            # If no relevant cases are found, use the HTN planner
            return self.htn_planner.plan_and_execute(goal, current_state)

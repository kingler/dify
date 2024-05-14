from mabos.reasoning import Reasoning

class Agent:
    def __init__(self, beliefs, desires, intentions):
        ...
        self.reasoning = Reasoning(self.beliefs, self.desires, self.intentions)

    def make_decision(self, goal):
        plan = self.reasoning.goal_based_reasoning(goal)
        if plan:
            self.intentions.append(plan)
            self.execute_plan(plan)

    def receive_feedback(self, feedback):
        self.reasoning.adaptability_learning(feedback)
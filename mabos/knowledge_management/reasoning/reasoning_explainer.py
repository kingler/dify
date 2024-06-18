from typing import List

from .reasoning_engine import Reasoning
from ...agents.agent import Agent
from ...plan_management.plan import Plan
from ...task_management.task import Task
from ...task_management.action import Action

class ReasoningExplainer:
    def __init__(self, reasoning: Reasoning):
        """
        Initialize the ReasoningExplainer with the given Reasoning object.

        Args:
            reasoning (Reasoning): The Reasoning object to be used for generating explanations.
        """
        self.reasoning = reasoning

    def explain_reasoning_process(self, agent: Agent, plan: Plan, task: Task, action: Action) -> str:
        """
        Generate an explanation of the reasoning process for the given agent, plan, task, and action.

        Args:
            agent (Agent): The agent for which the reasoning process is being explained.
            plan (Plan): The plan being reasoned about.
            task (Task): The task being reasoned about.
            action (Action): The action being reasoned about.

        Returns:
            str: The explanation of the reasoning process.
        """
        explanation = "Reasoning Process Explanation:\n"
        explanation += self.explain_belief_reasoning(agent)
        explanation += self.explain_desire_reasoning(agent)
        explanation += self.explain_intention_reasoning(agent)
        explanation += self.explain_goal_reasoning(agent)
        explanation += self.explain_plan_reasoning(plan)
        explanation += self.explain_task_reasoning(task)
        explanation += self.explain_action_reasoning(action)
        return explanation

    def explain_belief_reasoning(self, agent: Agent) -> str:
        """
        Generate an explanation of the belief reasoning process for the given agent.

        Args:
            agent (Agent): The agent for which the belief reasoning process is being explained.

        Returns:
            str: The explanation of the belief reasoning process.
        """
        explanation = "Belief Reasoning:\n"
        beliefs = agent.get_beliefs()
        for belief in beliefs:
            explanation += f"- Belief: {belief.description}, Certainty: {belief.certainty}, Source: {belief.source}\n"
        return explanation

    def explain_desire_reasoning(self, agent: Agent) -> str:
        """
        Generate an explanation of the desire reasoning process for the given agent.

        Args:
            agent (Agent): The agent for which the desire reasoning process is being explained.

        Returns:
            str: The explanation of the desire reasoning process.
        """
        explanation = "Desire Reasoning:\n"
        desires = agent.get_desires()
        for desire in desires:
            explanation += f"- Desire: {desire.description}, Priority: {desire.priority}\n"
        return explanation

    def explain_intention_reasoning(self, agent: Agent) -> str:
        """
        Generate an explanation of the intention reasoning process for the given agent.

        Args:
            agent (Agent): The agent for which the intention reasoning process is being explained.

        Returns:
            str: The explanation of the intention reasoning process.
        """
        explanation = "Intention Reasoning:\n"
        intentions = agent.get_intentions()
        for intention in intentions:
            explanation += f"- Intention: {intention.description}, Status: {intention.status}\n"
        return explanation

    def explain_goal_reasoning(self, agent: Agent) -> str:
        """
        Generate an explanation of the goal reasoning process for the given agent.

        Args:
            agent (Agent): The agent for which the goal reasoning process is being explained.

        Returns:
            str: The explanation of the goal reasoning process.
        """
        explanation = "Goal Reasoning:\n"
        goals = agent.get_goals()
        for goal in goals:
            explanation += f"- Goal: {goal.description}, Priority: {goal.priority}, Deadline: {goal.deadline}, Status: {goal.status}\n"
        return explanation

    def explain_plan_reasoning(self, plan: Plan) -> str:
        """
        Generate an explanation of the plan reasoning process for the given plan.

        Args:
            plan (Plan): The plan for which the reasoning process is being explained.

        Returns:
            str: The explanation of the plan reasoning process.
        """
        explanation = "Plan Reasoning:\n"
        explanation += f"- Plan: {plan.description}\n"
        explanation += f"- Actions: {', '.join([action.description for action in plan.actions])}\n"
        return explanation

    def explain_task_reasoning(self, task: Task) -> str:
        """
        Generate an explanation of the task reasoning process for the given task.

        Args:
            task (Task): The task for which the reasoning process is being explained.

        Returns:
            str: The explanation of the task reasoning process.
        """
        explanation = "Task Reasoning:\n"
        explanation += f"- Task: {task.description}\n"
        explanation += f"- Status: {task.status}\n"
        return explanation

    def explain_action_reasoning(self, action: Action) -> str:
        """
        Generate an explanation of the action reasoning process for the given action.

        Args:
            action (Action): The action for which the reasoning process is being explained.

        Returns:
            str: The explanation of the action reasoning process.
        """
        explanation = "Action Reasoning:\n"
        explanation += f"- Action: {action.description}\n"
        explanation += f"- Status: {action.status}\n"
        return explanation

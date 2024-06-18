from ..agents.agent import Agent
from ..task_management.task import Task
from typing import List

class Goal:
    def __init__(self, goal_id: str, description: str, priority: int, parent_goal: 'Goal' = None, goal_type: str = None, preconditions: List[str] = None, postconditions: List[str] = None, effects: List[str] = None, metrics: List[str] = None):
        """
        Initializes a Goal object with the given parameters.

        Parameters:
            goal_id (str): The unique identifier for the goal.
            description (str): A description of the goal.
            priority (int): The priority level of the goal.
            parent_goal (Goal, optional): The parent goal if this goal has one. Defaults to None.
            goal_type (str, optional): The type of the goal. Defaults to None.
            preconditions (List[str], optional): The preconditions required for the goal. Defaults to None.
            postconditions (List[str], optional): The postconditions achieved after the goal. Defaults to None.
            effects (List[str], optional): The effects of achieving the goal. Defaults to None.
            metrics (List[str], optional): The metrics associated with the goal. Defaults to None.
        """
        self.goal_id = goal_id
        self.description = description
        self.goal_type = goal_type
        self.priority = priority
        self.preconditions = preconditions
        self.postconditions = postconditions
        self.effects = effects
        self.metrics = metrics
        self.parent_goal = parent_goal
        self.sub_goals: List['Goal'] = []
        self.tasks: List[Task] = []
        
    def add_sub_goal(self, sub_goal: 'Goal'):
        """
        Adds a sub-goal to the list of sub-goals for this goal.

        Parameters:
            sub_goal (Goal): The sub-goal to be added.

        Returns:
            None
        """
        self.sub_goals.append(sub_goal)
        sub_goal.parent_goal = self    

    def is_achieved(self, agent: Agent) -> bool:
        """
        Check if all tasks associated with this goal have been completed by the given agent.

        Args:
            agent (Agent): The agent whose tasks are being checked.

        Returns:
            bool: True if all tasks are completed, False otherwise.
        """
        for task in self.tasks:
            if not task.is_completed:
                return False
        return True
    
    def add_task(self, task: Task):
        """
        Adds a task to the list of tasks for this goal.

        Parameters:
            task (Task): The task to be added.

        Returns:
            None
        """
        self.tasks.append(task)
        
    def set_and_decomposition(self, sub_goals: List['Goal']):
        """
        Sets the list of sub-goals for this goal and updates the parent_goal attribute of each sub-goal.

        Parameters:
            sub_goals (List['Goal']): A list of sub-goals to be set for this goal.

        Returns:
            None
        """
        self.sub_goals = sub_goals
        for sub_goal in sub_goals:
            sub_goal.parent_goal = self

    def set_or_decomposition(self, sub_goals: List['Goal']):
        """
        Sets the list of sub-goals for this goal and updates the parent_goal attribute of each sub-goal.

        Parameters:
            sub_goals (List['Goal']): A list of sub-goals to be set for this goal.

        Returns:
            None
        """
        self.sub_goals = sub_goals
        for sub_goal in sub_goals:
            sub_goal.parent_goal = self

    def add_dependency(self, dependent_goal: 'Goal'):
        """
        Adds a dependency to the list of dependencies for this goal.

        Parameters:
            dependent_goal (Goal): The goal that this goal depends on.

        Returns:
            None
        """
        self.dependencies.append(dependent_goal)
        
    def update_status(self):
        """
        Updates the status of the goal based on the status of its sub-goals.

        This function checks the status of each sub-goal of the current goal and updates the status of the goal accordingly.
        If all sub-goals are achieved, the status of the goal is set to "achieved".
        If any sub-goal is in progress, the status of the goal is set to "in_progress".
        If none of the sub-goals are achieved or in progress, the status of the goal is set to "pending".

        Parameters:
            self (Goal): The goal object whose status is being updated.

        Returns:
            None
        """
        if all(sub_goal.is_achieved() for sub_goal in self.sub_goals):
            self.status = "achieved"
        elif any(sub_goal.status == "in_progress" for sub_goal in self.sub_goals):
            self.status = "in_progress"
        else:
            self.status = "pending"    
            
    def update_priority(self, new_priority: int):
        """
        Update the priority of the goal and propagate the priority changes to its sub-goals.

        Parameters:
            new_priority (int): The new priority value to be set for the goal.

        Returns:
            None
        """
        self.priority = new_priority
        
        # Propagate priority changes to sub-goals
        for sub_goal in self.sub_goals:
            sub_goal.update_priority(new_priority)
        
    def detect_conflicts(self, other_goal: 'Goal') -> bool:
        """
        Detect conflicts between two goals based on their descriptions, preconditions, or effects.

        Parameters:
            other_goal (Goal): The goal object to compare with.

        Returns:
            bool: True if there is a conflict, False otherwise.
        """
        if self.description == other_goal.description:
            return True
        
        # Check for conflicts based on preconditions
        for precondition in self.preconditions:
            if precondition in other_goal.preconditions:
                return True
        
        # Check for conflicts based on effects
        for effect in self.effects:
            if effect in other_goal.effects:
                return True
        
        return False

    def resolve_conflict(self, other_goal: 'Goal'):
        """
        Resolve conflicts between two goals using goal negotiation or replanning strategies.

        Parameters:
            other_goal (Goal): The goal object with which the conflict needs to be resolved.

        Returns:
            None
        """
        # Goal negotiation strategy
        if self.priority > other_goal.priority:
            # Prioritize the current goal and modify the other goal
            other_goal.modify_goal(self)
        elif self.priority < other_goal.priority:
            # Prioritize the other goal and modify the current goal
            self.modify_goal(other_goal)
        else:
            # If priorities are equal, use a replanning strategy
            self.replan_goal(other_goal)
            other_goal.replan_goal(self)

    def modify_goal(self, higher_priority_goal: 'Goal'):
        """
        Modify the current goal to resolve conflicts with a higher priority goal.

        Parameters:
            higher_priority_goal (Goal): The goal with higher priority.

        Returns:
            None
        """
        # Modify the current goal's preconditions, effects, or description to resolve conflicts
        pass

    def replan_goal(self, other_goal: 'Goal'):
        """
        Replan the current goal to resolve conflicts with another goal.

        Parameters:
            other_goal (Goal): The goal with which the conflict needs to be resolved.

        Returns:
            None
        """
        # Replan the current goal by modifying its sub-goals or creating new sub-goals
        pass

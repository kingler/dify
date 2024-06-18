from typing import List
from ..task_management.action import Action
from ..agents.agent import Agent

class PathNotFoundException(Exception):
       """Exception raised when no path to the goal is found."""
       pass

class NoSuitableAgentFoundException(Exception):
    """Exception raised when no suitable agent is found for an action."""
    pass

class Plan:
    def __init__(self, plan_id: str, goal_id: str, actions: List[Action], 
                 priority: int = 0, preconditions: List[str] = None, 
                 postconditions: List[str] = None, constraints: List[str] = None):
        
        self.plan_id = plan_id
        self.goal_id = goal_id
        self.actions = actions
        self.priority = priority
        self.preconditions = preconditions or []
        self.postconditions = postconditions or []
        self.constraints = constraints or []
        self.status = "pending"

    def execute(self, agents: List['Agent']):
        if self.check_preconditions():
            self._set_status("in_progress")
            
            for action in self.actions:
                agent = self.select_agent(action, agents)
                action.execute(agent)
                
                if action.status != "completed":
                    self.repair(action)
            
            self._set_status("completed")
            self.evaluate_plan()
            
        else:
            self._set_status("failed")
            self.adapt_to_precondition_failure()

    def _set_status(self, status: str):
        self.status = status

    def check_preconditions(self) -> bool:
        # Check if all preconditions are satisfied
        return all(self.preconditions)


    def evaluate_plan(self):
        # Evaluate the success or effectiveness of the plan
        actual_outcomes = self.get_actual_outcomes()
        success_rate = self.calculate_success_rate(actual_outcomes)
        effectiveness_score = self.calculate_effectiveness_score(actual_outcomes)

        # Print the success rate and effectiveness score
        print(f"Plan success rate: {success_rate}")
        print(f"Plan effectiveness score: {effectiveness_score}")

        # Compare actual outcomes with postconditions
        for outcome, postcondition in zip(actual_outcomes, self.postconditions):
            if outcome != postcondition:
                print(f"Postcondition mismatch: Expected {postcondition}, got {outcome}")

    def adapt(self, new_goal: str):
        # Adapt the plan based on goal changes
        self.goal_id = new_goal
        new_actions = self.generate_actions_for_goal(new_goal)
        self.actions = self.merge_actions(self.actions, new_actions)
        self.update_preconditions_and_postconditions()

    def generate_actions_for_goal(self, goal: str) -> List[Action]:
        actions = []
        if goal == "Increase Sales":
            actions.extend([
                Action(name="Market Analysis", priority=1),
                Action(name="Advertising Campaign", priority=2),
                Action(name="Customer Feedback Collection", priority=3)
            ])
        elif goal == "Improve Customer Service":
            actions.extend([
                Action(name="Staff Training", priority=1),
                Action(name="Upgrade Support Systems", priority=2),
                Action(name="Review Customer Interaction", priority=3)
            ])
        elif goal == "Expand Market Reach":
            actions.extend([
                Action(name="Open New Branches", priority=1),
                Action(name="Partnership Development", priority=2),
                Action(name="International Marketing", priority=3)
            ])
        elif goal == "Enhance Product Quality":
            actions.extend([
                Action(name="Research and Development", priority=1),
                Action(name="Quality Assurance", priority=2),
                Action(name="Product Testing", priority=3)
            ])
        else:
            actions.extend([
                Action(name="General Review", priority=1),
                Action(name="Strategy Planning", priority=2)
            ])
        return actions    
    
    def merge_actions(self, current_actions: List[Action], 
                      new_actions: List[Action]) -> List[Action]:
        
        merged_actions = []
        current_action_idx = 0
        new_action_index = 0

        while current_action_idx < len(current_actions) and new_action_index < len(new_actions):
            current_action = current_actions[current_action_idx]
            new_action = new_actions[new_action_index]

            if current_action.priority >= new_action.priority:
                merged_actions.append(current_action)
            else:
                merged_actions.append(new_action)
                new_action_index += 1

            current_action_idx += 1

        merged_actions.extend(current_actions[current_action_idx:])
        merged_actions.extend(new_actions[new_action_index:])

        return self.optimize_action_sequence(merged_actions)

    def update_preconditions_and_postconditions(self):
        for action in self.actions:
            for precond in action.preconditions:
                if not self.satisfies_condition(precond):
                    if satisfying_actions := self.find_satisfying_actions(precond):
                        index = self.actions.index(action)
                        self.actions[index:index] = satisfying_actions 
                    else:
                        self.actions.remove(action)
                        break
            
            for postcondition in action.postconditions:
                if self.satisfies_condition(postcondition):
                    action.postconditions.remove(postcondition)
        
        self.preconditions = [precondition for action in self.actions for precondition in action.preconditions]
        self.postconditions = [postcondition for action in self.actions for postcondition in action.postconditions]

    def adapt_to_precondition_failure(self):

        for action in self.actions[:]:
            for precond in action.preconditions:
                if not self.satisfies_condition(precond):
                    if satisfying_actions := self.find_satisfying_actions(precond):
                        
                        if satisfying_actions:
                            action_index = self.actions.index(action) 
                            self.actions[action_index:action_index] = satisfying_actions
                    else:
                        self.actions.remove(action)
                        break  # Exit the loop as the action list has been modified

        # Optimize the modified plan
        self.actions = self.optimize_action_sequence(self.actions)

    def merge(self, other_plan: 'Plan') -> 'Plan':
        # Merge the current plan with another plan
        merged_actions = self.merge_actions(self.actions, other_plan.actions)
        merged_constraints = self.constraints + other_plan.constraints
        merged_constraints = self.constraints + other_plan.constraints
        return Plan(plan_id=f"{self.plan_id}_{other_plan.plan_id}",
                    goal_id=self.goal_id,
                    actions=merged_actions,
                    constraints=merged_constraints,
                    preconditions=self.preconditions + other_plan.preconditions,
                    postconditions=self.postconditions + other_plan.postconditions)
def select_agent(self, action: Action, agents: List['Agent']) -> 'Agent':
    best_agent = None
    max_suitability_score = -1

    for agent in agents:
        if not agent.available:
            continue

        suitability_score = 0

        if set(action.required_capabilities).issubset(agent.capabilities):
            suitability_score += 1

        if action.name in agent.experience:
            suitability_score += agent.experience[action.name]
        if agent.current_workload < agent.max_workload:
            suitability_score += 1
            
        if suitability_score > max_suitability_score:
            max_suitability_score = suitability_score
            best_agent = agent

    if best_agent is None:
        raise NoSuitableAgentFoundException("No suitable agent found for the action.")
    else:
        return best_agent  # Return the best suitable agent found # Placeholder implementation

    def repair(self, failed_action: Action):
        alternative_action = self.find_alternative_action(failed_action)
        if alternative_action:
            self.actions[self.actions.index(failed_action)] = alternative_action
        else:
            self.replan(failed_action)

    def find_alternative_action(self, failed_action: Action) -> Action:
        alternative_actions = []
        for action in self.available_actions:
            if (action.effects == failed_action.effects and
                all(precondition in self.current_state for precondition in action.preconditions or []) and
                all(constraint.satisfied(action) for constraint in self.constraints)):
                alternative_actions.append(action)
        
        if alternative_actions:
            best_alternative = min(alternative_actions, key=lambda a: a.cost)
            return best_alternative
        else:
            return None

    def replan(self, failed_action: Action):
        current_state = self.get_current_state()
        new_plan = self.generate_plan(current_state, self.goal_id)
        self.actions = self.actions[:self.actions.index(failed_action)] + new_plan.actions

    def generate_plan(self, current_state: List[str], goal: str) -> 'Plan':
        open_set = [current_state]
        came_from = {}
        g_score = {current_state: 0}
        f_score = {current_state: self.heuristic(current_state, goal)}

        while open_set:
            current = min(open_set, key=lambda state: f_score[state])
            if current == goal:
                return self.reconstruct_path(came_from, current)

            open_set.remove(current)
            for neighbor in self.get_neighbors(current):
                tentative_g_score = g_score[current] + self.distance(current, neighbor)
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + self.heuristic(neighbor, goal)
                    if neighbor not in open_set:
                        open_set.append(neighbor)

        raise PathNotFoundException("No path found to goal")

    def get_current_state(self) -> List[str]:
        environment_state = self.environment.get_current_state()
        return environment_state

    def decompose(self) -> List['Plan']:
        sub_plans = []
        for action in self.actions:
            sub_plan = self.create_sub_plan(action)
            if sub_plan:
                sub_plans.append(sub_plan)
        return sub_plans

    def create_sub_plan(self, action: Action) -> 'Plan':
        sub_plan = Plan(name=f"Sub-plan for {action.name}")
        sub_actions = []
        
        if action.name == "Market Research":
            sub_actions.append(Action(name="Conduct Surveys"))
            sub_actions.append(Action(name="Analyze Competitors"))
            sub_actions.append(Action(name="Identify Target Customers"))
        elif action.name == "Product Development":
            sub_actions.append(Action(name="Design Product"))
            sub_actions.append(Action(name="Prototype Creation"))
            sub_actions.append(Action(name="User Testing"))

        sub_actions[1].add_precondition(sub_actions[0])
        sub_actions[2].add_precondition(sub_actions[1])
        
        sub_plan.actions = sub_actions
        sub_plan.preconditions = action.preconditions
        sub_plan.postconditions = action.postconditions
        sub_plan.constraints = action.constraints
        
        return sub_plan
    
    def satisfies_condition(self, condition: str) -> bool:
        current_state = self.get_current_state()
        return condition in current_state

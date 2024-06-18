from pydantic import BaseModel
from typing import List

from mabos.event_management.event import Event

from ..ontology.ontology import Ontology
from ..knowledge_graph import KnowledgeGraph
from ...plan_management.plan import Plan
from ...task_management.task import Task
from ...task_management.action import Action
from ...agents.agent import Agent
from ...bdi.belief import Belief
from ...bdi.desire import Desire
from ...bdi.intention import Intention



def deliberate(self, agent: Agent, event: Event) -> None:
    """
    Perform deliberation based on the event.

    Args:
        agent (Agent): The agent performing the deliberation.
        event (Event): The event triggering the deliberation.

    Returns:
        None
    """
    pass


def ensure_knowledge_consistency(self) -> None:
    """
    Ensure knowledge consistency.

    Returns:
        None
    """
    pass


def ensure_knowledge_completeness(self) -> None:
    """
    Ensure knowledge completeness.

    Returns:
        None
    """
    pass


def reason(self, agent: Agent, plan: Plan, task: Task, action: Action, user, onboarding_step) -> None:
    """
    Perform reasoning.

    Args:
        agent (Agent): The agent performing the reasoning.
        plan (Plan): The plan being reasoned about.
        task (Task): The task being reasoned about.
        action (Action): The action being reasoned about.
        user: The user interacting with the agent.
        onboarding_step: The current onboarding step of the agent.

    Returns:
        None
    """
    pass
from ...goal_management.goal import Goal
from .goal_plan_tree import GoalPlanTree
from .htn_planner import HTNPlanner
from .case_based_reasoner import CaseBasedReasoner
from ..utils.indexing import IndexManager
from ..utils.caching import CacheManager
from ..learning.reasoning_learner import ReasoningLearner
from ..logging.reasoning_logger import ReasoningLogger
from .reasoning_debugger import ReasoningDebugger
from .reasoning_explainer import ReasoningExplainer

class Reasoning:
    ontology: Ontology
    knowledge_graph: KnowledgeGraph
    goal_plan_tree: GoalPlanTree
    htn_planner: HTNPlanner
    case_based_reasoner: CaseBasedReasoner
    index_manager: IndexManager
    cache_manager: CacheManager
    reasoning_learner: ReasoningLearner
    reasoning_logger: ReasoningLogger
    reasoning_debugger: ReasoningDebugger
    reasoning_explainer: ReasoningExplainer
    
    def __init__(self, ontology, knowledge_graph):
        """
        Initializes the Reasoning object with the provided ontology and knowledge graph.
        
        Args:
            ontology: The ontology to be used for reasoning.
            knowledge_graph: The knowledge graph to be used for reasoning.

        Returns:
            None
        """
        self.ontology = ontology
        self.knowledge_graph = knowledge_graph
        self.goal_plan_tree = GoalPlanTree(ontology)
        self.htn_planner = HTNPlanner(ontology)
        self.case_based_reasoner = CaseBasedReasoner(ontology, knowledge_graph)
        self.index_manager = IndexManager(knowledge_graph)
        self.cache_manager = CacheManager()
        self.reasoning_learner = ReasoningLearner()
        self.reasoning_logger = ReasoningLogger()
        self.reasoning_debugger = ReasoningDebugger()
        self.reasoning_explainer = ReasoningExplainer()

    def reason(self, agent: Agent, plan: Plan, task: Task, action: Action, user, onboarding_step):
        """
        Perform reasoning based on the agent's beliefs, desires, and intentions.

        Args:
            agent (Agent): The agent object for which reasoning is being performed.
            plan (Plan): The plan object for which reasoning is being performed.
            task (Task): The task object for which reasoning is being performed.
            action (Action): The action object for which reasoning is being performed.
            user: The user object for which reasoning is being performed.
            onboarding_step: The onboarding step object for which reasoning is being performed.

        Returns:
            None

        Description:
            This function performs reasoning based on the agent's beliefs, desires, and intentions. It first
            reasons the agent's beliefs, desires, and intentions using the `reason_beliefs`, `reason_desires`,
            and `reason_intentions` methods respectively. It then incorporates goal hierarchy and goal-oriented
            reasoning by calling the `reason_goals` method and applying advanced goal-oriented reasoning
            techniques using the `apply_goal_plan_tree_search`, `apply_htn_planning`, and
            `apply_case_based_reasoning` methods. The agent's state is updated based on the reasoning results
            using the `update_beliefs`, `update_desires`, `update_intentions`, and `update_goals` methods.
            Additional reasoning methods are applied using the `select_reasoning_methods` method and the
            corresponding `_reasoning` methods. Query performance is optimized using the `optimize_query_performance`
            method. Learning mechanisms are incorporated using the `incorporate_learning` method. Finally, the
            reasoning process is logged, debugged, and explained using the `log_reasoning_process`,
            `debug_reasoning_process`, and `explain_reasoning_process` methods of the `reasoning_logger`,
            `reasoning_debugger`, and `reasoning_explainer` objects respectively.
        """
        # Perform reasoning based on the agent's beliefs, desires, and intentions
        beliefs = self.reason_beliefs(agent)
        desires = self.reason_desires(agent, beliefs)
        intentions = self.reason_intentions(agent, beliefs, desires)

        # Incorporate goal hierarchy and goal-oriented reasoning
        goals = self.reason_goals(agent, beliefs, desires, intentions)
        self.prioritize_goals(goals)
        self.apply_goal_oriented_reasoning(agent, goals, beliefs)

        # Apply advanced goal-oriented reasoning techniques
        self.apply_goal_plan_tree_search(agent, goals)
        self.apply_htn_planning(agent, goals)
        self.apply_case_based_reasoning(agent, goals)

        # Update the agent's state based on the reasoning results
        agent.update_beliefs(beliefs)
        agent.update_desires(desires)
        agent.update_intentions(intentions)
        agent.update_goals(goals)

        # Apply additional reasoning methods
        reasoning_methods = self.select_reasoning_methods(plan, task, action)
        for method in reasoning_methods:
            getattr(self, f"{method}_reasoning")(plan, task, action, user, onboarding_step)

        # Optimize query performance
        self.optimize_query_performance()

        # Incorporate learning mechanisms
        self.incorporate_learning()

        # Logging, debugging, and explainable AI
        self.reasoning_logger.log_reasoning_process(agent, plan, task, action)
        self.reasoning_debugger.debug_reasoning_process(agent, plan, task, action)
        self.reasoning_explainer.explain_reasoning_process(agent, plan, task, action)

    def reason_beliefs(self, agent: Agent) -> List[Belief]:
        """
        Perform reasoning to update the agent's beliefs based on the knowledge graph.

        Args:
            agent (Agent): The agent whose beliefs are being updated.

        Returns:
            List[Belief]: A list of new beliefs derived from the knowledge graph.

        This function queries the knowledge graph to derive new beliefs. It constructs a query to retrieve
        the belief ID, description, certainty, source, and timestamp from the graph. The query is executed
        using the `query` method of the `knowledge_graph` object.

        For each result, the function checks if the belief is consistent with the agent's existing beliefs
        by calling the `is_belief_consistent` method of the `Reasoning` class. If the belief is consistent,
        a new `Belief` object is created with the retrieved information and added to the `new_beliefs` list.

        Finally, the function returns the `new_beliefs` list containing the new beliefs derived from the
        knowledge graph.
        """
        # Perform reasoning to update the agent's beliefs based on the knowledge graph
        new_beliefs = []
        
        # Query the knowledge graph to derive new beliefs
        belief_query = "SELECT ?belief_id ?description ?certainty ?source ?timestamp WHERE { ?belief rdf:type :Belief . ?belief :hasId ?belief_id . ?belief :hasDescription ?description . ?belief :hasCertainty ?certainty . ?belief :hasSource ?source . ?belief :hasTimestamp ?timestamp }"
        belief_results = self.knowledge_graph.query(belief_query)
        
        for result in belief_results:
            belief_id = result["belief_id"]
            description = result["description"]
            certainty = float(result["certainty"])
            source = result["source"]
            timestamp = float(result["timestamp"])
            
            # Check if the belief is consistent with the agent's existing beliefs
            if self.is_belief_consistent(agent, belief_id):
                new_belief = Belief(belief_id, description, certainty, source, timestamp)
                new_beliefs.append(new_belief)
        
        return new_beliefs

    def is_belief_consistent(self, agent: Agent, belief_id: str) -> bool:
        """
        Check if a belief is consistent with the agent's existing beliefs.

        Args:
            agent (Agent): The agent whose beliefs are being checked.
            belief_id (str): The ID of the belief to check for consistency.

        Returns:
            bool: True if the belief is consistent with the agent's existing beliefs, False otherwise.

        This function retrieves the agent's existing beliefs and checks if the given belief is consistent with them. It does this by calling the `are_beliefs_contradictory` method of the `ontology` object, passing in the belief ID. The function returns the negation of the result of this method call.

        """
        # Check if the belief is consistent with the agent's existing beliefs
        existing_beliefs = agent.get_beliefs()
        # End of Selection
        return not self.ontology.are_beliefs_contradictory(belief_id)

    def reason_desires(self, agent: Agent, beliefs: List[Belief]) -> List[Desire]:
        # Perform reasoning to update the agent's desires based on its beliefs and goals
        new_desires = []
        
        # Query the ontology to generate desires based on the agent's beliefs and goals
        for belief in beliefs:
            desire_ids = self.ontology.get_desires_from_belief(belief.belief_id)
            for desire_id in desire_ids:
                desire_description = self.ontology.get_desire_description(desire_id)
                desire_priority = self.ontology.get_desire_priority(desire_id)
                activation_condition = self.ontology.get_desire_activation_condition(desire_id)
                completion_condition = self.ontology.get_desire_completion_condition(desire_id)
                deadline = self.ontology.get_desire_deadline(desire_id)
                
                # Check if the desire is achievable given the agent's current beliefs
                if self.is_desire_achievable(agent, desire_id, beliefs):
                    new_desire = Desire(desire_id, desire_description, desire_priority, activation_condition, completion_condition, deadline)
                    new_desires.append(new_desire)
        
        return new_desires

    def is_desire_achievable(self, agent: Agent, desire_id: str, beliefs: List[Belief]) -> bool:
        # Check if the desire is achievable given the agent's current beliefs
        required_beliefs = self.ontology.get_required_beliefs_for_desire(desire_id)
        for required_belief in required_beliefs:
            if not any(belief.belief_id == required_belief for belief in beliefs):
                return False
        return True

    def reason_intentions(self, agent: Agent, beliefs: List[Belief], desires: List[Desire]) -> List[Intention]:
        # Perform reasoning to update the agent's intentions based on its beliefs and desires
        new_intentions = []
        
        # Query the ontology to generate intentions based on the agent's beliefs and desires
        for desire in desires:
            intention_ids = self.ontology.get_intentions_from_desire(desire.desire_id)
            for intention_id in intention_ids:
                intention_description = self.ontology.get_intention_description(intention_id)
                intention_actions = self.ontology.get_intention_actions(intention_id)
                intention_goal = self.ontology.get_intention_goal(intention_id)
                intention_preconditions = self.ontology.get_intention_preconditions(intention_id)
                intention_postconditions = self.ontology.get_intention_postconditions(intention_id)
                
                # Check if the intention is feasible given the agent's current beliefs
                if self.is_intention_feasible(agent, intention_id, beliefs):
                    new_intention = Intention(intention_id, intention_description, intention_actions, intention_goal, intention_preconditions, intention_postconditions, "inactive")
                    new_intentions.append(new_intention)
        
        return new_intentions

    def is_intention_feasible(self, agent: Agent, intention_id: str, beliefs: List[Belief]) -> bool:
        # Check if the intention is feasible given the agent's current beliefs
        required_beliefs = self.ontology.get_required_beliefs_for_intention(intention_id)
        for required_belief in required_beliefs:
            if not any(belief.belief_id == required_belief for belief in beliefs):
                return False
        return True

    def reason_goals(self, agent: Agent, beliefs: List[Belief], desires: List[Desire], intentions: List[Intention]) -> List[Goal]:
        # Perform reasoning to generate goals based on the agent's beliefs, desires, and intentions
        new_goals = []
        
        # Query the ontology to generate goals based on the agent's beliefs, desires, and intentions
        for desire in desires:
            goal_ids = self.ontology.get_goals_from_desire(desire.desire_id)
            for goal_id in goal_ids:
                goal_description = self.ontology.get_goal_description(goal_id)
                goal_priority = self.ontology.get_goal_priority(goal_id)
                goal_deadline = self.ontology.get_goal_deadline(goal_id)
                
                # Check if the goal is relevant given the agent's current beliefs and intentions
                if self.is_goal_relevant(agent, goal_id, beliefs, intentions):
                    new_goal = Goal(goal_id, goal_description, goal_priority, goal_deadline, "inactive")
                    new_goals.append(new_goal)
        
        return new_goals

    def is_goal_relevant(self, agent: Agent, goal_id: str, beliefs: List[Belief], intentions: List[Intention]) -> bool:
        """
        Check if the goal is relevant given the agent's current beliefs and intentions.
        
        Args:
            agent (Agent): The agent to check goal relevance for.
            goal_id (str): The ID of the goal to check relevance for.
            beliefs (List[Belief]): The agent's current beliefs.
            intentions (List[Intention]): The agent's current intentions.
        
        Returns:
            bool: True if the goal is relevant, False otherwise.
        """
        required_beliefs = self.ontology.get_required_beliefs_for_goal(goal_id)
        for required_belief in required_beliefs:
            if not any(belief.belief_id == required_belief for belief in beliefs):
                return False
        
        required_intentions = self.ontology.get_required_intentions_for_goal(goal_id)
        for required_intention in required_intentions:
            if not any(intention.intention_id == required_intention for intention in intentions):
                return False
        
        return True

    def prioritize_goals(self, goals: List[Goal]):
        """
        Prioritize goals based on their priority and deadline.

        Args:
            goals (List[Goal]): A list of Goal objects to be prioritized.

        Returns:
            None. The input list of goals is sorted in-place.
        """
        goals.sort(key=lambda goal: (goal.priority, goal.deadline), reverse=True)

    def apply_goal_oriented_reasoning(self, agent: Agent, goals: List[Goal], beliefs: List[Belief]):
        # Apply goal-oriented reasoning techniques to select and pursue goals
        for goal in goals:
            if goal.status == "inactive":
                # Check if the goal's preconditions are satisfied
                if self.are_goal_preconditions_satisfied(goal, beliefs):
                    # Activate the goal
                    goal.status = "active"
                    
                    # Select plans to achieve the goal
                    plans = self.select_plans_for_goal(goal, beliefs)
                    
                    # Execute the selected plans
                    for plan in plans:
                        self.execute_plan(agent, plan)
                        
                    # Check if the goal is achieved
                    if self.is_goal_achieved(goal, beliefs):
                        goal.status = "achieved"
                    else:
                        goal.status = "failed"

    def are_goal_preconditions_satisfied(self, goal: Goal, beliefs: List[Belief]) -> bool:
        """
        Check if the goal's preconditions are satisfied given the agent's current beliefs.

        Args:
            goal (Goal): The goal object to check.
            beliefs (List[Belief]): The list of beliefs representing the agent's current knowledge.

        Returns:
            bool: True if all preconditions of the goal are satisfied, False otherwise.
        """
        # Check if the goal's preconditions are satisfied given the agent's current beliefs
        preconditions = self.ontology.get_goal_preconditions(goal.goal_id)
        for precondition in preconditions:
            if not any(belief.belief_id == precondition for belief in beliefs):
                return False
        return True

    def select_plans_for_goal(self, goal: Goal, beliefs: List[Belief]) -> List[Plan]:
        """
        Selects plans to achieve a given goal based on the agent's current beliefs.

        Args:
            goal (Goal): The goal to achieve.
            beliefs (List[Belief]): The list of beliefs representing the agent's current knowledge.

        Returns:
            List[Plan]: A list of selected plans that are applicable to achieve the goal.
        """
        # Select plans to achieve the goal based on the agent's current beliefs
        plan_ids = self.ontology.get_plans_for_goal(goal.goal_id)
        selected_plans = []
        for plan_id in plan_ids:
            if self.is_plan_applicable(plan_id, beliefs):
                plan_description = self.ontology.get_plan_description(plan_id)
                plan_actions = self.ontology.get_plan_actions(plan_id)
                selected_plan = Plan(plan_id, plan_description, plan_actions)
                selected_plans.append(selected_plan)
        return selected_plans

    def is_plan_applicable(self, plan_id: str, beliefs: List[Belief]) -> bool:
        """
        Check if a plan is applicable given the agent's current beliefs.

        Args:
            plan_id (str): The ID of the plan to check applicability for.
            beliefs (List[Belief]): The list of beliefs representing the agent's current knowledge.

        Returns:
            bool: True if the plan is applicable, False otherwise.
        """
        # Check if the plan is applicable given the agent's current beliefs
        required_beliefs = self.ontology.get_required_beliefs_for_plan(plan_id)
        for required_belief in required_beliefs:
            if not any(belief.belief_id == required_belief for belief in beliefs):
                return False
        return True

    def is_goal_achieved(self, goal: Goal, beliefs: List[Belief]) -> bool:
        """
        Check if a goal is achieved given the agent's current beliefs.

        Args:
            goal (Goal): The goal object to check.
            beliefs (List[Belief]): The list of beliefs representing the agent's current knowledge.

        Returns:
            bool: True if the goal is achieved, False otherwise.
        """
        # Check if the goal is achieved given the agent's current beliefs
        postconditions = self.ontology.get_goal_postconditions(goal.goal_id)
        for postcondition in postconditions:
            if not any(belief.belief_id == postcondition for belief in beliefs):
                return False
        return True

    def execute_plan(self, agent: Agent, plan: Plan):
        """
        Execute the actions defined in the plan.

        Args:
            agent (Agent): The agent carrying out the plan.
            plan (Plan): The plan containing the actions to be executed.
        """
        # Execute the actions defined in the plan
        for action in plan.actions:
            self.execute_action(agent, action)
            
    def execute_action(self, agent: Agent, action: Action):
        """
        Execute the action and update the agent's beliefs and knowledge graph
        Args:
            agent (Agent): The agent performing the action.
            action (Action): The action to be executed.
        """
        action_output = self.ontology.execute_action(action.action_id)
        
        agent.update_beliefs(action_output)
        self.update_knowledge_graph(action_output)
        
    def update_knowledge_graph(self, data):
        """
        Updates the knowledge graph with the provided data.

        Args:
            data (List[str]): A list of RDF triples to be inserted into the knowledge graph.

        Returns:
            None
        """
        for item in data:
            self.knowledge_graph.update(f"INSERT DATA {{ {item} }}")


    def user_preference_reasoning(self, user):
        """
        Retrieves user preferences from the knowledge graph based on the user ID.

        Args:
            user (User): The user object containing the user ID.

        Returns:
            list: A list of user preferences retrieved from the knowledge graph.
        """
        user_preferences = self.knowledge_graph.query(f"SELECT ?preference WHERE {{ ?user :hasPreference ?preference . ?user :userId '{user.id}' }}")

        return user_preferences

    def update_entities_with_conclusions(self, plan, task, action, conclusions):
        """
        Updates the plan, task, and action entities with the provided conclusions.

        Args:
            plan (Plan): The plan entity to be updated with conclusions.
            task (Task): The task entity to be updated with conclusions.
            action (Action): The action entity to be updated with conclusions.
            conclusions (List[str]): A list of conclusions to be added to the entities.

        Returns:
            tuple: A tuple containing the updated plan, task, and action entities.
        """
        updated_plan = self.update_plan_with_conclusions(plan, conclusions)
        updated_task = self.update_task_with_conclusions(task, conclusions)
        updated_action = self.update_action_with_conclusions(action, conclusions)
        return updated_plan, updated_task, updated_action

    def select_reasoning_methods(self, plan, task, action):
        """
        Selects appropriate reasoning methods based on the given plan, task, and action.

        Args:
            plan (Plan): The plan to consider for selecting reasoning methods.
            task (Task): The task to consider for selecting reasoning methods.
            action (Action): The action to consider for selecting reasoning methods.

        Returns:
            list: A list of selected reasoning methods.
        """
        methods = ["user_preference"]
        if plan.name == "Strategic Plan":
            methods.append("strategic_decision_making")
        if task.name == "Market Analysis":
            methods.append("operational_optimization")
        if action.name == "Competitor Analysis":
            methods.append("risk_assessment")
        return methods

    def update_plan_with_conclusions(self, plan: Plan, conclusions: List[str]) -> Plan:
        """
        Updates a plan with the given conclusions.

        Args:
            plan (Plan): The plan to update.
            conclusions (List[str]): The list of conclusions to add to the plan.

        Returns:
            Plan: The updated plan with the conclusions appended to its details.
        """
        for conclusion in conclusions:
            plan.details += f"\nConclusion: {conclusion}"
        return plan

    def update_task_with_conclusions(self, task: Task, conclusions: List[str]) -> Task:
        """
        Updates the given task with the provided conclusions.

        Args:
            task (Task): The task to be updated.
            conclusions (List[str]): The conclusions to be added to the task.

        Returns:
            Task: The updated task with the conclusions appended to its details.
        """
        # Example logic to update task with conclusions
        for conclusion in conclusions:
            task.details += f"\nConclusion: {conclusion}"
        return task

    def update_action_with_conclusions(self, action: Action, conclusions: List[str]) -> Action:
        """
        Updates the given action with the provided conclusions.

        Args:
            action (Action): The action to be updated.
            conclusions (List[str]): The list of conclusions to be added to the action.

        Returns:
            Action: The updated action with the conclusions appended to its details.
        """
        # Example logic to update action with conclusions
        for conclusion in conclusions:
            action.details += f"\nConclusion: {conclusion}"
        return action

    def update_ontology(self, task: Task):
        """
        Updates the ontology with the output and context of a completed task.

        Args:
            task (Task): The completed task containing the output and context to update the ontology with.

        Returns:
            None
        """
        self.ontology.update(task.output, task.context)

    def deliberate(self, agent: Agent, event: Event):
        """
        Deliberates on an event and updates the agent's beliefs, performs goal-oriented reasoning, and selects and executes plans.

        Args:
            agent (Agent): The agent to deliberate on.
            event (Event): The event to trigger belief updates and goal-oriented reasoning.

        Returns:
            None
        """
        # Trigger belief update based on the event
        self.update_beliefs(agent, event)
        
        # Perform goal-oriented reasoning
        self.goal_oriented_reasoning(agent)
        
        # Select and execute plans
        self.plan_selection_and_execution(agent)
        
    def update_beliefs(self, agent: Agent, event: Event):
        """
        Update the agent's beliefs based on the event.

        Args:
            agent (Agent): The agent whose beliefs are being updated.
            event (Event): The event containing the belief updates.
        """
        for belief_update in event.belief_updates:
            self.knowledge_graph.update(f"INSERT DATA {{ {belief_update} }}")

        new_beliefs = self.reason_beliefs(agent)
        agent.update_beliefs(new_beliefs)
        
    def goal_oriented_reasoning(self, agent: Agent):
        """
        Perform goal-oriented reasoning based on the agent's beliefs and desires.

        Args:
            agent (Agent): The agent object for which goal-oriented reasoning is performed.

        Returns:
            None

        Description:
            This function performs goal-oriented reasoning by applying goal selection rules
            based on the agent's beliefs and desires. It first retrieves the agent's beliefs
            and desires using the `get_beliefs` and `get_desires` methods respectively.
            The `apply_goal_selection_rules` method is then called to select goals based on
            the beliefs and desires. The selected goals are used to update the agent's
            intentions using the `reason_intentions` method. Finally, the agent's intentions
            are updated using the `update_intentions` method.

        Note:
            This function assumes that the agent object has the necessary methods for
            retrieving beliefs and desires, and for updating intentions.
        """
        # Perform goal-oriented reasoning based on the agent's beliefs and desires
        beliefs = agent.get_beliefs()
        desires = agent.get_desires()
        
        # Apply goal selection rules
        selected_goals = self.apply_goal_selection_rules(beliefs, desires)
        
        # Update the agent's intentions based on the selected goals
        new_intentions = self.reason_intentions(agent, beliefs, selected_goals)
        agent.update_intentions(new_intentions)
        
    def plan_selection_and_execution(self, agent: Agent):
        """
        Select plans based on the agent's intentions and beliefs
        """
        # Select plans based on the agent's intentions and beliefs
        intentions = agent.get_intentions()
        beliefs = agent.get_beliefs()
        
        # Apply plan selection rules
        selected_plans = self.apply_plan_selection_rules(intentions, beliefs)
        
        # Execute the selected plans
        for plan in selected_plans:
            self.execute_plan(agent, plan)
            
    def apply_goal_selection_rules(self, beliefs: List[Belief], desires: List[Desire]) -> List[Desire]:
        """
        Apply goal selection rules based on beliefs and desires.

        Args:
            beliefs (List[Belief]): A list of beliefs.
            desires (List[Desire]): A list of desires.

        Returns:
            List[Desire]: A list of selected desires based on the goal selection rules.
        """
        # Apply goal selection rules based on beliefs and desires
        selected_goals = []
        
        # Example rule: Select desires with high priority and matching beliefs
        for desire in desires:
            if desire.priority > 5 and self.ontology.is_desire_supported_by_beliefs(desire.desire_id, beliefs):
                selected_goals.append(desire)
        
        return selected_goals
        
    def apply_plan_selection_rules(self, intentions: List[Intention], beliefs: List[Belief]) -> List[Plan]:
        """
        Apply plan selection rules based on intentions and beliefs.

        Args:
            intentions (List[Intention]): The list of intentions.
            beliefs (List[Belief]): The list of beliefs.

        Returns:
            List[Plan]: The list of selected plans that fulfill the intentions and are feasible based on beliefs.
        """
        # Apply plan selection rules based on intentions and beliefs
        selected_plans = []
        
        # Example rule: Select plans that fulfill the intentions and are feasible based on beliefs
        for intention in intentions:
            plan_ids = self.ontology.get_plans_for_intention(intention.intention_id)
            for plan_id in plan_ids:
                if self.ontology.is_plan_feasible(plan_id, beliefs):
                    plan_description = self.ontology.get_plan_description(plan_id)
                    plan_actions = self.ontology.get_plan_actions(plan_id)
                    selected_plan = Plan(plan_id, plan_description, plan_actions)
                    selected_plans.append(selected_plan)
        
        return selected_plans
        
    def execute_plan(self, agent: Agent, plan: Plan):
        """
        Execute the actions defined in the plan.

        Args:
            agent (Agent): The agent executing the plan.
            plan (Plan): The plan containing the actions to be executed.
        """
        for action in plan.actions:
            self.execute_action(agent, action)
            
    def execute_action(self, agent: Agent, action: Action):
        """
        Execute the specified action and update the agent's beliefs and knowledge graph.
        
        Args:
            agent (Agent): The agent executing the action.
            action (Action): The action to be executed.
        """
        action_output = self.ontology.execute_action(action.action_id)
        
        agent.update_beliefs(action_output)
        self.update_knowledge_graph(action_output)

        
    def update_knowledge_graph(self, data):
        """
        Update the knowledge graph with the provided data.

        Args:
            data (list): A list of data items to be inserted into the knowledge graph.
        """
        for item in data:
            self.knowledge_graph.update(f"INSERT DATA {{ {item} }}")
        
    def ensure_knowledge_consistency(self):
        """
        Ensure consistency of the ontology and knowledge graph.
        
        This method performs consistency checks on the ontology and knowledge graph.
        If any inconsistencies are found, it resolves them using the respective
        resolve_inconsistencies methods of the ontology and knowledge graph.
        """
        # Perform consistency checks on the ontology and knowledge graph
        inconsistencies = self.ontology.check_consistency()
        if inconsistencies:
            # Handle inconsistencies in the ontology
            self.ontology.resolve_inconsistencies(inconsistencies)
        
        inconsistencies = self.knowledge_graph.check_consistency()
        if inconsistencies:
            # Handle inconsistencies in the knowledge graph
            self.knowledge_graph.resolve_inconsistencies(inconsistencies)

        
    def ensure_knowledge_completeness(self):
        """
        Ensures the knowledge completeness of the ontology and knowledge graph.

        This function performs completeness checks on the ontology and knowledge graph.
        If any missing elements are found, it handles them by adding the missing elements
        to the respective ontology or knowledge graph.

        Parameters:
            self (Reasoning): The Reasoning object.

        Returns:
            None

        Example Usage:
            reasoning = Reasoning(ontology=my_ontology, knowledge_graph=my_knowledge_graph)
            reasoning.ensure_knowledge_completeness()

        Example Definitions:
            my_ontology = Ontology()  # Initialize your Ontology instance
            my_knowledge_graph = KnowledgeGraph()  # Initialize your KnowledgeGraph instance

        Example Usage with Initialization:
            reasoning = Reasoning(ontology=my_ontology, knowledge_graph=my_knowledge_graph)
            agent = Agent(agent_id="agent1", ontology=my_ontology, knowledge_graph=my_knowledge_graph)
            event = Event(belief_updates=[Belief("new_belief", "New Belief Description")])
            reasoning.deliberate(agent, event)
            reasoning.ensure_knowledge_consistency()
            reasoning.ensure_knowledge_completeness()
            plan = Plan(name="Strategic Plan")
            task = Task(name="Market Analysis")
            action = Action(name="Competitor Analysis")
            reasoning.reason(agent, plan, task, action)
        """
        # Perform completeness checks on the ontology and knowledge graph
        missing_elements = self.ontology.check_completeness()
        if missing_elements:
            # Handle missing elements in the ontology
            self.ontology.add_missing_elements(missing_elements)
        
        missing_elements = self.knowledge_graph.check_completeness()
        if missing_elements:
            # Handle missing elements in the knowledge graph
            self.knowledge_graph.add_missing_elements(missing_elements)
        
        # Example definitions for ontology and knowledge graph
        my_ontology = Ontology()  # Initialize your Ontology instance
        my_knowledge_graph = KnowledgeGraph()  # Initialize your KnowledgeGraph instance

        # Initialize Reasoning with ontology and knowledge graph
        reasoning = Reasoning(ontology=my_ontology, knowledge_graph=my_knowledge_graph)

        agent = Agent(agent_id="agent1", ontology=my_ontology, knowledge_graph=my_knowledge_graph)

        # Example event
        event = Event(belief_updates=[Belief("new_belief", "New belief description")])

        # Perform deliberation based on the event
        reasoning.deliberate(agent, event)

        # Ensure knowledge consistency and completeness
        reasoning.ensure_knowledge_consistency()
        reasoning.ensure_knowledge_completeness()

        # Define a plan, task, and action
        plan = Plan(name="Strategic Plan")
        task = Task(name="Market Analysis")
        action = Action(name="Competitor Analysis")

        # Apply reasoning
        reasoning.reason(agent, plan, task, action)


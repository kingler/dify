from typing import List, Dict, Any, TYPE_CHECKING
from ..goal_management.goal import Goal
from ..plan_management.plan import Plan
from ..task_management.task import Task
from ..knowledge_management.reasoning.reasoning_engine import Reasoning
from ..knowledge_management.knowledge_base import KnowledgeBase
from ..knowledge_management.knowledge_graph import KnowledgeGraph
from ..communication.communication import AgentCommunication
from ..communication.negotiation.contract_net_protocol import ContractNetProtocol
from ..communication.negotiation.auction_based_negotiation import AuctionBasedNegotiation
from ..communication.group_formation import GroupFormation
from ..communication.negotiation.multi_issue_negotiation import MultiIssueNegotiation
from ..communication.negotiation.integrative_negotiation import IntegrativeNegotiation
from skills.skills import Skill

if TYPE_CHECKING:
    from .agent import Agent

class BaseAgent:
    def __init__(self, agent_id: str, knowledge_base: KnowledgeBase, knowledge_graph: KnowledgeGraph):
        self.agent_id = agent_id
        self.knowledge_base = knowledge_base
        self.knowledge_graph = knowledge_graph
        self.goals: List[Goal] = []
        self.plans: List[Plan] = []
        self.beliefs: dict = {}
        self.communication = AgentCommunication(self, knowledge_base, knowledge_graph)
        self.reasoning = Reasoning(knowledge_base, knowledge_graph)

    def perceive(self, environment):
        # Perceive the environment and update beliefs
        percepts = environment.get_percepts(self)
        self.update_beliefs(percepts)

    def reason(self):
        # Perform reasoning based on current beliefs and goals
        self.reasoning.reason()

    def plan(self):
        # Generate plans to achieve goals
        self.plans = self.reasoning.generate_plans(self.goals)

    def act(self, environment):
        # Execute plans and perform actions in the environment
        for plan in self.plans:
            self.execute_plan(plan, environment)

    def communicate(self, other_agents):
        # Communicate with other agents
        for agent in other_agents:
            self.communication.send_message(agent, self.beliefs)
            received_message = self.communication.receive_message(agent)
            self.process_message(received_message)

    def update_beliefs(self, percepts):
        # Update beliefs based on percepts
        for percept in percepts:
            self.beliefs[percept] = percepts[percept]

    def execute_plan(self, plan, environment):
        # Execute a plan in the environment
        for action in plan.actions:
            environment.execute_action(self, action)

    def process_message(self, message):
        # Process received message and update beliefs and goals
        if message.type == 'inform':
            self.update_beliefs(message.content)
        elif message.type == 'request':
            self.goals.append(message.content)

class SpecializedAgent(BaseAgent):
    def __init__(self, agent_id: str, knowledge_base: KnowledgeBase, knowledge_graph: KnowledgeGraph):
        super().__init__(agent_id, knowledge_base, knowledge_graph)
        self.contract_net_protocol = ContractNetProtocol(self)
        self.auction_based_negotiation = AuctionBasedNegotiation(self)
        self.group_formation = GroupFormation(self)
        self.multi_issue_negotiation = MultiIssueNegotiation(self)
        self.integrative_negotiation = IntegrativeNegotiation(self)
        self.proposals = []
        self.counter_proposals = []
        self.agreements = []
        self.reputation_scores = {}
        self.interaction_history = []
        self.communication_strategies = {}
        self.dify_agent_id = [] # Optional mapping to Dify agent

    # Additional methods specific to SpecializedAgent can be added here

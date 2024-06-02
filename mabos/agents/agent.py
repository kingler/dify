from typing import List, Dict, Any, TYPE_CHECKING
from ..goal_management.goal import Goal
from ..planning.plan import Plan
from ..task_management.task import Task
from ..knowledge_management.reasoning_engine import Reasoning
from ..knowledge_management.core.knowledge_base import KnowledgeBase
from ..knowledge_management.core.knowledge_graph import KnowledgeGraph
from ..communication.communication import AgentCommunication
from ..communication.negotiation.contract_net_protocol import ContractNetProtocol
from ..communication.negotiation.auction_based_negotiation import AuctionBasedNegotiation
from ..communication.group_formation import GroupFormation
from ..communication.negotiation.multi_issue_negotiation import MultiIssueNegotiation
from ..communication.negotiation.integrative_negotiation import IntegrativeNegotiation
from skills.skills import Skill

if TYPE_CHECKING:
    from .agent import Agent

def receive_proposal(self, sender: Agent, proposal: Dict[str, Any]):
       # Evaluate the proposal based on the agent's goals and beliefs
       if self.is_proposal_acceptable(proposal):
           self.send_agreement(sender, proposal)
           self.reinforce_communication_strategy(sender, proposal)
       else:
           counter_proposal = self.generate_counter_proposal(proposal)
           self.send_counter_proposal(sender, counter_proposal)
           self.adjust_communication_strategy(sender, proposal)

def receive_agreement(self, sender: Agent, agreement: Dict[str, Any]):
       # Update the agent's beliefs and plans based on the agreement
       self.update_beliefs(agreement)
       self.revise_plans(agreement)
       self.reinforce_communication_strategy(sender, agreement)

class Agent:
    def __init__(self, agent_id: str, knowledge_base: KnowledgeBase, knowledge_graph: KnowledgeGraph):
        self.agent_id = agent_id
        self.capabilities = []
        self.skills = []
        self.knowledge_base = knowledge_base
        self.knowledge_graph = knowledge_graph
        self.goals: List[Goal] = []
        self.plans: List[Plan] = []
        self.beliefs: dict = {}
        self.communication = AgentCommunication(self, knowledge_base, knowledge_graph)
        self.reasoning = Reasoning(knowledge_base, knowledge_graph)
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

    def is_proposal_acceptable(self, proposal):
        # Evaluate if a proposal is acceptable based on beliefs and goals
        # Implement specific evaluation logic based on the agent's criteria
        pass

    def generate_counter_proposal(self, proposal):
        # Generate a counter-proposal based on the received proposal
        # Implement specific counter-proposal generation logic
        pass

    def send_agreement(self, sender, proposal):
        # Send an agreement message to the sender
        agreement_message = {'type': 'agree', 'content': proposal}
        self.communication.send_message(sender, agreement_message)

    def send_counter_proposal(self, sender, counter_proposal):
        # Send a counter-proposal message to the sender
        counter_proposal_message = {'type': 'counter-propose', 'content': counter_proposal}
        self.communication.send_message(sender, counter_proposal_message)

    def reinforce_communication_strategy(self, sender, proposal):
        # Reinforce the communication strategy based on successful agreement
        # Implement specific reinforcement learning logic
        pass

    def adjust_communication_strategy(self, sender, proposal):
        # Adjust the communication strategy based on unsuccessful proposal
        # Implement specific adjustment logic
        pass

    def update_beliefs(self, agreement):
        # Update beliefs based on the agreement
        for belief, value in agreement.items():
            self.beliefs[belief] = value

    def revise_plans(self, agreement):
        # Revise plans based on the agreement
        # Implement specific plan revision logic
        pass
        
    def detect_conflict(self, other_agent: 'Agent') -> bool:
         # Check for conflicting goals or beliefs
         for goal in self.goals:
             if goal in other_agent.goals:
                 if self.reasoning.is_goal_conflicting(goal, other_agent.beliefs):
                     return True
         for belief, value in self.beliefs.items():
             if belief in other_agent.beliefs:
                 if value != other_agent.beliefs[belief]:
                     return True
         return False

    def resolve_conflict(self, other_agent: 'Agent'):
         # Initiate negotiation or compromise to resolve conflicts
         if self.detect_conflict(other_agent):
             # Identify negotiation issues
             issues = self.identify_negotiation_issues(other_agent)
             
             # Initiate multi-issue negotiation
             negotiation_proposal = self.generate_multi_issue_proposal(issues, other_agent)
             self.communicate(negotiation_proposal, other_agent)
             
             # Wait for response and handle accordingly
             response = self.receive_message(other_agent)
             if response['performative'] == 'agree':
                 # Negotiation successful, update beliefs and goals
                 agreement = response['content']
                 self.finalize_agreement(agreement, other_agent)
                 self.reinforce_communication_strategy(other_agent, negotiation_proposal)
             elif response['performative'] == 'counter-propose':
                 # Handle counter-proposal
                 counter_proposal = response['content']
                 self.handle_counter_proposal(counter_proposal, other_agent)
                 self.adjust_communication_strategy(other_agent, negotiation_proposal)
             else:
                 # Negotiation failed, consider alternative resolution methods
                 self.find_alternative_resolution(other_agent)
                 self.adjust_communication_strategy(other_agent, negotiation_proposal)
         else:
             # No conflict detected, continue normal execution
             pass
             
    def identify_negotiation_issues(self, other_agent: 'Agent') -> List[str]:
        # Identify the issues to be negotiated based on conflicting goals and beliefs
        issues = []
        for goal in self.goals:
            if goal in other_agent.goals and self.reasoning.is_goal_conflicting(goal, other_agent.beliefs):
                issues.append(goal)
        for belief, value in self.beliefs.items():
            if belief in other_agent.beliefs and value != other_agent.beliefs[belief]:
                issues.append(belief)
        return issues
        
    def generate_multi_issue_proposal(self, issues: List[str], other_agent: 'Agent') -> Dict[str, Any]:
        # Generate a multi-issue proposal considering the identified issues and the agent's preferences
        proposal = {}
        for issue in issues:
            if isinstance(issue, Goal):
                proposal[issue] = self.reasoning.generate_goal_proposal(issue, other_agent.beliefs)
            else:
                proposal[issue] = self.reasoning.generate_belief_proposal(issue, other_agent.beliefs)
        return proposal
        
    def handle_counter_proposal(self, counter_proposal: Dict[str, Any], other_agent: 'Agent'):
        # Evaluate and adjust the proposal based on the received counter-proposal
        adjusted_proposal = self.integrative_negotiation.adjust_proposal(counter_proposal, other_agent)
        self.communicate(adjusted_proposal, other_agent)
        
        # Wait for response and handle accordingly
        response = self.receive_message(other_agent)
        if response['performative'] == 'agree':
            # Negotiation successful, update beliefs and goals
            agreement = response['content']
            self.finalize_agreement(agreement, other_agent)
            self.reinforce_communication_strategy(other_agent, adjusted_proposal)
        elif response['performative'] == 'counter-propose':
            # Handle further counter-proposals recursively
            self.handle_counter_proposal(response['content'], other_agent)
            self.adjust_communication_strategy(other_agent, adjusted_proposal)
        else:
            # Negotiation failed, consider alternative resolution methods
            self.find_alternative_resolution(other_agent)
            self.adjust_communication_strategy(other_agent, adjusted_proposal)
            
    def finalize_agreement(self, agreement: Dict[str, Any], other_agent: 'Agent'):
        # Update beliefs and goals based on the finalized agreement
        for issue, value in agreement.items():
            if isinstance(issue, Goal):
                self.update_goal(issue, value)
            else:
                self.update_belief(issue, value)
        
        # Notify the other agent about the finalized agreement
        confirmation_message = {'performative': 'confirm', 'content': agreement}
        self.communicate(confirmation_message, other_agent)
        
    def update_reputation(self, agent_id: str, score: float, source_agent_id: str):
         # Update direct reputation score
         self.reputation_scores[agent_id] = score
         self.interaction_history.append((agent_id, score))

         # Update indirect reputation scores based on information from other agents
         for other_agent_id, other_agent_score in self.reputation_scores.items():
             if other_agent_id != agent_id:
                 indirect_score = other_agent_score * self.trust_level(source_agent_id)
                 self.reputation_scores[agent_id] += indirect_score    

    def reinforce_communication_strategy(self, other_agent: 'Agent', proposal: Dict[str, Any]):
        # Reinforce successful communication strategies
        if other_agent.agent_id not in self.communication_strategies:
            self.communication_strategies[other_agent.agent_id] = {}
        
        for issue, value in proposal.items():
            if issue not in self.communication_strategies[other_agent.agent_id]:
                self.communication_strategies[other_agent.agent_id][issue] = {}
            
            if value not in self.communication_strategies[other_agent.agent_id][issue]:
                self.communication_strategies[other_agent.agent_id][issue][value] = 0
            
            self.communication_strategies[other_agent.agent_id][issue][value] += 1

    def adjust_communication_strategy(self, other_agent: 'Agent', proposal: Dict[str, Any]):
        # Adjust unsuccessful communication strategies
        if other_agent.agent_id not in self.communication_strategies:
            self.communication_strategies[other_agent.agent_id] = {}
        
        for issue, value in proposal.items():
            if issue not in self.communication_strategies[other_agent.agent_id]:
                self.communication_strategies[other_agent.agent_id][issue] = {}
            
            if value not in self.communication_strategies[other_agent.agent_id][issue]:
                self.communication_strategies[other_agent.agent_id][issue][value] = 0
            
            self.communication_strategies[other_agent.agent_id][issue][value] -= 1

    def select_communication_strategy(self, other_agent: 'Agent', issue: str) -> Any:
        # Select the most successful communication strategy for a given issue and agent
        if other_agent.agent_id in self.communication_strategies and issue in self.communication_strategies[other_agent.agent_id]:
            strategies = self.communication_strategies[other_agent.agent_id][issue]
            return max(strategies, key=strategies.get)
        else:
            return None
        
    def synchronize_with_dify(self, dify_agent: 'DifyAgent'):
        if self.dify_agent_id == dify_agent.agent_id:
            # Synchronize attributes
            self.beliefs.update(dify_agent.skills)  # Example synchronization logic
            # Add more synchronization logic as needed       

class DifyAgent:
    def __init__(self, agent_id: str, skills: List[str], mabos_agent_id: str = None):
        self.agent_id = agent_id
        self.skills = skills
        self.mabos_agent_id = mabos_agent_id  # Optional mapping to MABOS agent

    def synchronize_with_mabos(self, mabos_agent: 'Agent'):
        if self.mabos_agent_id == mabos_agent.agent_id:
            # Synchronize attributes
            self.skills.extend(mabos_agent.beliefs.keys())  # Example synchronization logic
            # Add more synchronization logic as needed
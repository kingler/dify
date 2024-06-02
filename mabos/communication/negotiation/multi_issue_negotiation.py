from typing import Dict, Any
from ...agents.agent import Agent

class MultiIssueNegotiation:
    def __init__(self, agent: Agent):
        self.agent = agent
        self.proposals = []
        self.counter_proposals = []
        self.agreements = []

    def evaluate_proposal(self, proposal: Dict[str, Any]) -> bool:
        # Evaluate the proposal based on the agent's goals and beliefs
        for issue, value in proposal.items():
            if not self.agent.reasoning.is_acceptable(issue, value):
                return False
        return True

    def generate_counter_proposal(self, proposal: Dict[str, Any]) -> Dict[str, Any]:
        # Generate a counter-proposal based on the received proposal and the agent's goals and beliefs
        counter_proposal = {}
        for issue, value in proposal.items():
            if not self.agent.reasoning.is_acceptable(issue, value):
                # Propose an alternative value for the issue
                alternative_value = self.agent.reasoning.propose_alternative(issue, value)
                counter_proposal[issue] = alternative_value
            else:
                counter_proposal[issue] = value
        return counter_proposal

    def send_proposal(self, recipient: Agent, proposal: Dict[str, Any]):
        # Send the proposal to the recipient agent
        recipient.receive_proposal(self.agent, proposal)
        self.proposals.append(proposal)

    def send_counter_proposal(self, recipient: Agent, counter_proposal: Dict[str, Any]):
        # Send the counter-proposal to the recipient agent
        recipient.receive_counter_proposal(self.agent, counter_proposal)
        self.counter_proposals.append(counter_proposal)

    def send_agreement(self, recipient: Agent, agreement: Dict[str, Any]):
        # Send the agreement to the recipient agent
        recipient.receive_agreement(self.agent, agreement)
        self.agreements.append(agreement)

    def receive_proposal(self, sender: Agent, proposal: Dict[str, Any]):
        # Process the received proposal
        if self.evaluate_proposal(proposal):
            self.send_agreement(sender, proposal)
        else:
            counter_proposal = self.generate_counter_proposal(proposal)
            self.send_counter_proposal(sender, counter_proposal)

    def receive_counter_proposal(self, sender: Agent, counter_proposal: Dict[str, Any]):
        # Process the received counter-proposal
        if self.evaluate_proposal(counter_proposal):
            self.send_agreement(sender, counter_proposal)
        else:
            # Continue the negotiation process
            pass

    def receive_agreement(self, sender: Agent, agreement: Dict[str, Any]):
        # Process the received agreement
        self.agreements.append(agreement)
        # Update the agent's beliefs and plans based on the agreement
        self.agent.update_beliefs(agreement)
        self.agent.revise_plans(agreement)

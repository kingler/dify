# File: mabos/integration/dify_ui_integration.py
from mabos.agents.agent import Agent
from mabos.agents.utils_agents.broker import Broker

class DifyUIIntegration:
    def __init__(self, broker: Broker):
        self.broker = broker

    def register_agent_ui_component(self, agent: Agent, ui_component: dict) -> None:
        """
        Register a MABOS agent's UI component to be integrated into the Dify UI.
        """
        # Implement logic to package the agent's UI component information
        # and register it with the Dify UI system using the Broker
        self.broker.register_agent_ui_component(agent, ui_component)

    def update_agent_ui_state(self, agent: Agent, state: dict) -> None:
        """
        Update the state of a MABOS agent's UI component in the Dify UI.
        """
        # Implement logic to send updates to the Dify UI system
        # about the current state of the MABOS agent's UI component, using the Broker
        self.broker.update_agent_ui_state(agent, state)

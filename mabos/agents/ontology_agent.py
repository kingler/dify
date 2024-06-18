# mabos/agents/ontology_agent.py
from .utils_agents.broker import Broker
from ..knowledge_management.knowledge_base import KnowledgeBase
from .ontology_manager import OntologyManager
from ..communication.communication import AgentCommunication
from .utils_agents.logger import Logger
from .utils_agents.message_storage import MessageStorage
from ..error_handler import ErrorHandler

class OntologyAgent:
    def __init__(self, location):
        self.location = location
        self.broker = Broker()
        self.knowledge_base = KnowledgeBase()
        self.communication = AgentCommunication(self, self.knowledge_base)
        self.error_handler = ErrorHandler()
        self.message_storage = MessageStorage()
        self.logger = Logger()
        self.ontology_manager = OntologyManager()

    def send_message(self, recipient, message):
        if recipient.location == self.location:
            # If the recipient is in the same location, send the message directly
            recipient.receive_message(self, message)
        else:
            # If the recipient is in a different location, route the message through the broker
            self.broker.route_message(self, recipient, message)

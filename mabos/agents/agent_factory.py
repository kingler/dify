from typing import Type
from mabos.agents.agent import BaseAgent, SpecializedAgent
from mabos.knowledge_management import knowledge_graph
from mabos.knowledge_management import knowledge_base
from mabos.knowledge_management.knowledge_base import KnowledgeBase
from mabos.knowledge_management.knowledge_graph import KnowledgeGraph

class AgentFactory:
    @staticmethod
    def create_agent(agent_type: Type[BaseAgent], agent_id: str, knowledge_base: KnowledgeBase, knowledge_graph: KnowledgeGraph) -> BaseAgent:
        """
        Create and configure an agent of the specified type.
        
        Args:
            agent_type: The type of agent to create (e.g., BaseAgent, SpecializedAgent).
            agent_id: The unique identifier for the agent.
            knowledge_base: The knowledge base to be used by the agent.
            knowledge_graph: The knowledge graph to be used by the agent.
        
        Returns:
            The created and configured agent instance.
        """
        return agent_type(agent_id, knowledge_base, knowledge_graph)

    @staticmethod
    def create_base_agent(agent_id: str, knowledge_base: KnowledgeBase, knowledge_graph: KnowledgeGraph) -> BaseAgent:
        """
        Create and configure a base agent.
        
        Args:
            agent_id: The unique identifier for the agent.
            knowledge_base: The knowledge base to be used by the agent.
            knowledge_graph: The knowledge graph to be used by the agent.
        
        Returns:
            The created and configured base agent instance.
        """
        return AgentFactory.create_agent(BaseAgent, agent_id, knowledge_base, knowledge_graph)

    @staticmethod
    def create_specialized_agent(agent_id: str, knowledge_base: KnowledgeBase, knowledge_graph: KnowledgeGraph) -> SpecializedAgent:
        """
        Create and configure a specialized agent.
        
        Args:
            agent_id: The unique identifier for the agent.
            knowledge_base: The knowledge base to be used by the agent.
            knowledge_graph: The knowledge graph to be used by the agent.
        
        Returns:
            The created and configured specialized agent instance.
        """
        return AgentFactory.create_agent(SpecializedAgent, agent_id, knowledge_base, knowledge_graph)

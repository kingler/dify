from typing import Any
from mabos.agents.agent import Agent, DifyAgent
from mabos.knowledge_management.core.knowledge_base import KnowledgeBase
from mabos.knowledge_management.core.knowledge_graph import KnowledgeGraph


class DifyData:
    def __init__(self, data_id: str, content: Any, mabos_data_id: str = None):
        self.data_id = data_id
        self.content = content
        self.mabos_data_id = mabos_data_id  # Optional mapping to MABOS data

    def integrate_with_mabos(self, mabos_knowledge_base: 'KnowledgeBase'):
        # Integrate Dify data with MABOS knowledge base
        for document in mabos_knowledge_base.documents:
            self.content += document  # Example integration logic
        for tool in mabos_knowledge_base.external_data_tools:
            self.content += tool  # Example integration logic
        for api_data in mabos_knowledge_base.api_maintained_knowledge:
            self.content += api_data  # Example integration logic
            
    def test_agent_synchronization():
        # Create MABOS agent
        knowledge_base = KnowledgeBase()
        knowledge_graph = KnowledgeGraph()
        mabos_agent = Agent(agent_id="mabos_1", knowledge_base=knowledge_base, knowledge_graph=knowledge_graph, dify_agent_id="dify_1")
        mabos_agent.beliefs = {"skill1": True, "skill2": True}

        # Create Dify agent
        dify_agent = DifyAgent(agent_id="dify_1", skills=["skill3"], mabos_agent_id="mabos_1")

        # Synchronize agents
        mabos_agent.synchronize_with_dify(dify_agent)
        dify_agent.synchronize_with_mabos(mabos_agent)

        # Verify synchronization
        assert "skill1" in dify_agent.skills
        assert "skill2" in dify_agent.skills
        assert "skill3" in mabos_agent.beliefs

    def test_knowledge_integration():
        # Create MABOS knowledge base
        knowledge_base = KnowledgeBase()
        knowledge_base.add_document("Document 1")
        knowledge_base.add_external_data_tool("Tool 1")
        knowledge_base.maintain_knowledge_via_api("API Data 1")

        # Create Dify data
        dify_data = DifyData(data_id="dify_1", content="Initial Content")

        # Integrate with MABOS knowledge base
        dify_data.integrate_with_mabos(knowledge_base)

        # Verify integration
        assert "Document 1" in dify_data.content
        assert "Tool 1" in dify_data.content
        assert "API Data 1" in dify_data.content

    test_agent_synchronization()
    test_knowledge_integration()            
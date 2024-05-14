from pydantic import BaseModel, Field
from typing import List
from ..reasoning.reasoning import Reasoner
from ..knowledge.knowledge import KnowledgeGraph
from ..knowledge.fact import Fact

class InferenceEngine(BaseModel):
    reasoner: Reasoner = Field(description="Reasoner used for inference")
    knowledge_graph: KnowledgeGraph = Field(description="Knowledge graph")
    
    def infer_new_facts(self) -> List[Fact]:
        # Use reasoner to infer new facts based on knowledge graph
        pass
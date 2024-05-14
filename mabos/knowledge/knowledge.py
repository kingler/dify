from pydantic import BaseModel
from typing import List, Dict, Any
from owlready2 import sync_reasoner
import networkx as nx
from ..ontology.ontology import get_ontology
from rdflib import Graph
from rdflib.query import prepareQuery
from typing import Optional
from mabos.agents import Agent
from mabos.tasks import KnowledgeManagementTask

class KnowledgeBase(BaseModel):
    def __init__(self, ontology_path: str):
        self.ontology = get_ontology(ontology_path).load()
        self.graph = self.create_knowledge_graph()

    def create_knowledge_graph(self):
        pass

    def query(self, sparql_query: str) -> List[Dict[str, str]]:
        pass

class KnowledgeManagementAgent(Agent):
    def __init__(self, ontology_path):
        self.ontology = get_ontology(ontology_path).load()
        self.knowledge_graph = nx.MultiDiGraph()
        self.knowledge_base = KnowledgeBase(ontology_path)

    def perform_reasoning(self):
        with self.ontology:
            sync_reasoner()

    def execute_sparql_query(self, query):
        g = self.ontology.world.as_rdflib_graph()
        query_obj = prepareQuery(query)
        results = g.query(query_obj)
        return results

    def process_query(self, query):
        pass

    def execute_task(self, task: Any, context: Optional[str] = None, tools: Optional[List[Any]] = None) -> str:
        if isinstance(task, KnowledgeManagementTask):
            query = task.query

            self.perform_reasoning()

            if task.sparql_query:
                results = self.execute_sparql_query(task.sparql_query)
            else:
                results = self.process_query(query)

            return results
        else:
            return super().execute_task(task, context, tools)

    def load_ontology(self, ontology_path):
        ontology = Graph()
        ontology.parse(ontology_path)
        return ontology

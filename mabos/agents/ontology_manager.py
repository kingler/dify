from ..knowledge_management.ontology.ontology import Ontology
from owlready2 import get_ontology

class OntologyManager:
    def __init__(self):
        self.ontology = Ontology()

    def load_ontology(self, ontology_path):
        self.ontology.load_ontology(ontology_path)

    def generate_domain_ontology(self, user_data):
        # Generate domain-specific ontology based on user onboarding data
        domain_ontology = get_ontology("http://example.com/onboarding-ontology") 
        
        # Define classes and properties based on user data
        with domain_ontology:
            class User(domain_ontology.Thing): pass
            class BusinessModel(domain_ontology.Thing): pass
            class ProductDescription(domain_ontology.Thing): pass
            
            class hasDescription(domain_ontology.ObjectProperty):
                domain = [BusinessModel]
                range = [str]
            class belongsTo(domain_ontology.ObjectProperty):
                domain = [ProductDescription]
                range = [BusinessModel]
        
        return domain_ontology

    def get_classes(self):
        return self.ontology.get_classes()

    def get_properties(self):
        return self.ontology.get_properties()

    def query_ontology(self, query):
        return self.ontology.query_ontology(query)

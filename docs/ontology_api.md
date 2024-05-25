# Ontology API Doc

Breaking down the task of writing the SQLAlchemy models for the MABOS-related database tables in the `ontology_api.py` file, considering the provided code snippets from `ontology.py`, `ontology.ttl`, `meta_ontology.ttl`, and `ontology_agent.py`.

Step 1: Identify the key concepts and relationships in the ontology.
Based on the provided code snippets, we can identify the following key concepts and relationships:

- Ontology: Represents the main ontology class with concepts and relationships.
- Concept: Represents a domain concept in the ontology.
- Relationship: Represents a relationship between concepts in the ontology.
- Axiom: Represents an axiom or rule in the ontology.
- MetaOntology: Represents a meta-ontology that defines the structure and properties of domain ontologies.
- DomainOntology: Represents a domain-specific ontology derived from the meta-ontology.
- Entity: Represents a business entity or concept in the domain ontology.
- Attribute: Represents a property or attribute of an entity in the domain ontology.
- DataModel: Represents a derived data model from the domain ontology.
- DerivedModel: Represents a derived model (e.g., process, object, message) from the domain ontology.
- FIBOMapping: Represents a mapping between the domain ontology and FIBO concepts.

Step 2: Define the SQLAlchemy models based on the identified concepts and relationships.
Here's an example of how you can define the SQLAlchemy models in the `ontology_api.py` file:

```python
from datetime import datetime
from enum import Enum
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class OntologyStatus(Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'

class Ontology(Base):
    __tablename__ = 'ontologies'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    status = Column(String(20), nullable=False, default=OntologyStatus.ACTIVE.value)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    concepts = relationship('Concept', back_populates='ontology')
    relationships = relationship('Relationship', back_populates='ontology')
    axioms = relationship('Axiom', back_populates='ontology')

class Concept(Base):
    __tablename__ = 'concepts'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    ontology_id = Column(Integer, ForeignKey('ontologies.id'), nullable=False)
    ontology = relationship('Ontology', back_populates='concepts')

class Relationship(Base):
    __tablename__ = 'relationships'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    domain_id = Column(Integer, ForeignKey('concepts.id'), nullable=False)
    range_id = Column(Integer, ForeignKey('concepts.id'), nullable=False)
    ontology_id = Column(Integer, ForeignKey('ontologies.id'), nullable=False)
    ontology = relationship('Ontology', back_populates='relationships')

class Axiom(Base):
    __tablename__ = 'axioms'
    id = Column(Integer, primary_key=True)
    description = Column(Text, nullable=False)
    ontology_id = Column(Integer, ForeignKey('ontologies.id'), nullable=False)
    ontology = relationship('Ontology', back_populates='axioms')

class MetaOntology(Base):
    __tablename__ = 'meta_ontologies'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    domain_ontologies = relationship('DomainOntology', back_populates='meta_ontology')

class DomainOntology(Base):
    __tablename__ = 'domain_ontologies'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    meta_ontology_id = Column(Integer, ForeignKey('meta_ontologies.id'), nullable=False)
    meta_ontology = relationship('MetaOntology', back_populates='domain_ontologies')
    entities = relationship('Entity', back_populates='domain_ontology')
    data_models = relationship('DataModel', back_populates='domain_ontology')
        derived_models = relationship('DerivedModel', back_populates='domain_ontology')
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

class Entity(Base):
    __tablename__ = 'entities'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    domain_ontology_id = Column(Integer, ForeignKey('domain_ontologies.id'), nullable=False)
    domain_ontology = relationship('DomainOntology', back_populates='entities')
    attributes = relationship('Attribute', back_populates='entity')
    fibo_mappings = relationship('FIBOMapping', back_populates='entity')

class Attribute(Base):
    __tablename__ = 'attributes'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    entity_id = Column(Integer, ForeignKey('entities.id'), nullable=False)
    entity = relationship('Entity', back_populates='attributes')

class DataModel(Base):
    __tablename__ = 'data_models'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    domain_ontology_id = Column(Integer, ForeignKey('domain_ontologies.id'), nullable=False)
    domain_ontology = relationship('DomainOntology', back_populates='data_models')

class DerivedModel(Base):
    __tablename__ = 'derived_models'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    domain_ontology_id = Column(Integer, ForeignKey('domain_ontologies.id'), nullable=False)
    domain_ontology = relationship('DomainOntology', back_populates='derived_models')

class FIBOMapping(Base):
    __tablename__ = 'fibo_mappings'
    id = Column(Integer, primary_key=True)
    fibo_concept = Column(String(100), nullable=False)
    entity_id = Column(Integer, ForeignKey('entities.id'), nullable=False)
    entity = relationship('Entity', back_populates='fibo_mappings')    

```

Step 3: Integrate the SQLAlchemy models with the existing codebase.
Update the __init__.py file in the models directory to import the ontology models.
Modify the ontology.py file to use the SQLAlchemy models for storing and retrieving ontology data.
Adapt the ontology_agent.py file to interact with the ontology models when generating and storing ontologies.

Step 4: Create database migrations for the ontology models.
Use a database migration tool (e.g., Alembic) to generate migration scripts based on the defined ontology models.
Run the migration scripts to create the corresponding tables in the database.

Step 5: Test the integration of the ontology models.
Write unit tests to verify the functionality of the ontology models and their integration with the existing codebase.
Ensure that the ontology generation, storage, and retrieval processes work as expected using the SQLAlchemy models.

By following these steps and considering the provided code snippets, you can create the necessary SQLAlchemy models in the ontology_api.py file to represent the MABOS-related database tables. The models define the structure and relationships of the ontology concepts, meta-ontology, domain ontologies, entities, attributes, data models, derived models, and FIBO mappings.

Remember to integrate the models seamlessly with the existing codebase, create database migrations, and thoroughly test the integration to ensure the correctness and reliability of the ontology-related functionality in the MABOS system.

---
1. Added an OntologyStatus enum to represent the status of an ontology (active or inactive).
2. Added description, created_at, and updated_at columns to the Ontology, MetaOntology, and DomainOntology models.
3. Added description columns to the Concept, Relationship, Entity, Attribute, DataModel, and DerivedModel models.
4. Used String(100) for the name columns to specify a maximum length of 100 characters.
5. Used Text for the description columns to allow for longer text content.
6. Used DateTime for the created_at and updated_at columns, with default values set to the current UTC timestamp.
8. Added nullable=False to the required columns to ensure data integrity.

These changes enhance the models by adding more descriptive fields, timestamps for tracking creation and updates, and ensuring data consistency through appropriate constraints.
Remember to update the __init__.py file in the models directory to import these models, and make necessary adjustments to the existing codebase to integrate these models seamlessly.
Also, consider creating database migrations using a tool like Alembic to manage the database schema changes over time.
Let me know if you have any further questions or if there's anything else I can assist you with!
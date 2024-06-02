from datetime import datetime
from enum import Enum
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .database import Base

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
    domain_ontologies = relationship('DomainOntology' back_populates='meta_ontology')

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
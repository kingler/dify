from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from .database import Base

class Ontology(Base):
    __tablename__ = 'ontologies'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    facts = relationship('Fact', back_populates='ontology')

class Fact(Base):
    __tablename__ = 'facts'
    id = Column(Integer, primary_key=True)
    subject = Column(String(100), nullable=False)
    predicate = Column(String(100), nullable=False)
    object = Column(Text, nullable=False)
    ontology_id = Column(Integer, ForeignKey('ontologies.id'), nullable=False)
    ontology = relationship('Ontology', back_populates='facts')

class Index(Base):
    __tablename__ = 'indexes'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    type = Column(String(50), nullable=False)
    ontology_id = Column(Integer, ForeignKey('ontologies.id'), nullable=False)
    ontology = relationship('Ontology')

class Cache(Base):
    __tablename__ = 'caches'
    id = Column(Integer, primary_key=True)
    query = Column(Text, nullable=False)
    result = Column(Text, nullable=False)
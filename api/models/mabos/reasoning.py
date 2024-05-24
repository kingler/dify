from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from .database import Base

class Belief(Base):
    __tablename__ = 'beliefs'
    id = Column(Integer, primary_key=True)
    belief_id = Column(String(100), unique=True, nullable=False)
    description = Column(Text)
    agent_id = Column(Integer, ForeignKey('agents.id'), nullable=False)
    agent = relationship('Agent', back_populates='beliefs')

class Desire(Base):
    __tablename__ = 'desires'
    id = Column(Integer, primary_key=True)
    desire_id = Column(String(100), unique=True, nullable=False)
    description = Column(Text)
    priority = Column(Integer)
    agent_id = Column(Integer, ForeignKey('agents.id'), nullable=False)
    agent = relationship('Agent', back_populates='desires')

class Intention(Base):
    __tablename__ = 'intentions'
    id = Column(Integer, primary_key=True)
    intention_id = Column(String(100), unique=True, nullable=False)
    description = Column(Text)
    agent_id = Column(Integer, ForeignKey('agents.id'), nullable=False)
    agent = relationship('Agent', back_populates='intentions')

class Plan(Base):
    __tablename__ = 'plans'
    id = Column(Integer, primary_key=True)
    plan_id = Column(String(100), unique=True, nullable=False)
    description = Column(Text)
    actions = relationship('Action', back_populates='plan')

class Action(Base):
    __tablename__ = 'actions'
    id = Column(Integer, primary_key=True)
    action_id = Column(String(100), unique=True, nullable=False)
    description = Column(Text)
    plan_id = Column(Integer, ForeignKey('plans.id'), nullable=False)
    plan = relationship('Plan', back_populates='actions')

class Event(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True)
    event_id = Column(String(100), unique=True, nullable=False)
    description = Column(Text)
    belief_updates = relationship('BeliefUpdate', back_populates='event')

class BeliefUpdate(Base):
    __tablename__ = 'belief_updates'
    id = Column(Integer, primary_key=True)
    belief_id = Column(String(100), nullable=False)
    description = Column(Text)
    event_id = Column(Integer, ForeignKey('events.id'), nullable=False)
    event = relationship('Event', back_populates='belief_updates')

class Agent(Base):
    __tablename__ = 'agents'
    id = Column(Integer, primary_key=True)
    agent_id = Column(String(100), unique=True, nullable=False)
    beliefs = relationship('Belief', back_populates='agent')
    desires = relationship('Desire', back_populates='agent')
    intentions = relationship('Intention', back_populates='agent')
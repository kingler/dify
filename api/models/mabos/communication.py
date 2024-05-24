from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from .database import Base

class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    sender_id = Column(Integer, ForeignKey('agents.id'), nullable=False)
    recipient_id = Column(Integer, ForeignKey('agents.id'), nullable=False)
    content = Column(Text, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    conversation_id = Column(String(100))
    reply_to_id = Column(Integer, ForeignKey('messages.id'))
    language = Column(String(50), nullable=False)
    ontology_id = Column(Integer, ForeignKey('communication_ontologies.id'))
    protocol = Column(String(50))

    sender = relationship('Agent', foreign_keys=[sender_id], back_populates='sent_messages')
    recipient = relationship('Agent', foreign_keys=[recipient_id], back_populates='received_messages')
    reply_to = relationship('Message', remote_side=[id])
    ontology = relationship('CommunicationOntology', back_populates='messages')

class CommunicationOntology(Base):
    __tablename__ = 'communication_ontologies'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)

    messages = relationship('Message', back_populates='ontology')

class Agent(Base):
    __tablename__ = 'agents'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)

    sent_messages = relationship('Message', foreign_keys='[Message.sender_id]', back_populates='sender')
    received_messages = relationship('Message', foreign_keys='[Message.recipient_id]', back_populates='recipient')

class Topic(Base):
    __tablename__ = 'topics'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)

    subscriptions = relationship('TopicSubscription', back_populates='topic')

class TopicSubscription(Base):
    __tablename__ = 'topic_subscriptions'
    id = Column(Integer, primary_key=True)
    agent_id = Column(Integer, ForeignKey('agents.id'), nullable=False)
    topic_id = Column(Integer, ForeignKey('topics.id'), nullable=False)

    agent = relationship('Agent')
    topic = relationship('Topic', back_populates='subscriptions')
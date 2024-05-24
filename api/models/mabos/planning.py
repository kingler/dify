from sqlalchemy import Column, Integer, String, ForeignKey, Float, Boolean
from sqlalchemy.orm import relationship
from .database import Base

class Plan(Base):
    __tablename__ = 'plans'
    id = Column(Integer, primary_key=True)
    plan_id = Column(String(100), unique=True, nullable=False)
    goal_id = Column(String(100), ForeignKey('goals.goal_id'), nullable=False)
    actions = relationship('Action', back_populates='plan')
    priority = Column(Integer, nullable=False)
    preconditions = Column(String(255))
    postconditions = Column(String(255))
    constraints = Column(String(255))

class Action(Base):
    __tablename__ = 'actions'
    id = Column(Integer, primary_key=True)
    action_id = Column(String(100), unique=True, nullable=False)
    description = Column(String(255), nullable=False)
    required_capabilities = Column(String(255))
    cost = Column(Float, nullable=False)
    plan_id = Column(Integer, ForeignKey('plans.id'))
    plan = relationship('Plan', back_populates='actions')

class Goal(Base):
    __tablename__ = 'goals'
    id = Column(Integer, primary_key=True)
    goal_id = Column(String(100), unique=True, nullable=False)
    description = Column(String(255), nullable=False)
    priority = Column(Integer, nullable=False)
    parent_goal_id = Column(String(100), ForeignKey('goals.goal_id'))
    parent_goal = relationship('Goal', remote_side=[goal_id])
    sub_goals = relationship('Goal', backref=backref('parent', remote_side=[goal_id]))
    goal_type = Column(String(50))
    preconditions = Column(String(255))
    postconditions = Column(String(255))
    effects = Column(String(255))
    metrics = Column(String(255))

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    task_id = Column(String(100), unique=True, nullable=False)
    description = Column(String(255), nullable=False)
    is_completed = Column(Boolean, default=False)
    agent_id = Column(String(100), ForeignKey('agents.agent_id'))
    agent = relationship('Agent', back_populates='tasks')

class Agent(Base):
    __tablename__ = 'agents'
    id = Column(Integer, primary_key=True)
    agent_id = Column(String(100), unique=True, nullable=False)
    capabilities = Column(String(255))
    experience = Column(String(255))
    current_workload = Column(Integer, default=0)
    tasks = relationship('Task', back_populates='agent')
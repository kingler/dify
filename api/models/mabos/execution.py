# Define the SQLAlchemy models for the MABOS-related database tables.
# The models are used to interact with the database using the ORM.from sqlalchemy
from sqlalchemy import Column, Integer, ForeignKey, DateTime, String, Float, relationship
from .database import Base

class Execution(Base):
    __tablename__ = 'executions'
    id = Column(Integer, primary_key=True)
    plan_id = Column(Integer, ForeignKey('plans.id'), nullable=False)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    status = Column(String(50))
    steps = relationship('ExecutionStep', back_populates='execution')
    logs = relationship('ExecutionLog', back_populates='execution')
    metrics = relationship('ExecutionMetric', back_populates='execution')

class ExecutionStep(Base):
    __tablename__ = 'execution_steps'
    id = Column(Integer, primary_key=True)
    execution_id = Column(Integer, ForeignKey('executions.id'), nullable=False)
    action_id = Column(Integer, ForeignKey('actions.id'), nullable=False)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    status = Column(String(50))
    execution = relationship('Execution', back_populates='steps')
    action = relationship('Action')
    logs = relationship('ExecutionLog', back_populates='step')
    metrics = relationship('ExecutionMetric', back_populates='step')

class ExecutionLog(Base):
    __tablename__ = 'execution_logs'
    id = Column(Integer, primary_key=True)
    execution_id = Column(Integer, ForeignKey('executions.id'))
    step_id = Column(Integer, ForeignKey('execution_steps.id'))
    timestamp = Column(DateTime, nullable=False)
    log_level = Column(String(20), nullable=False)
    message = Column(String(255), nullable=False)
    execution = relationship('Execution', back_populates='logs')
    step = relationship('ExecutionStep', back_populates='logs')

class ExecutionMetric(Base):
    __tablename__ = 'execution_metrics'
    id = Column(Integer, primary_key=True)
    execution_id = Column(Integer, ForeignKey('executions.id'))
    step_id = Column(Integer, ForeignKey('execution_steps.id'))
    name = Column(String(100), nullable=False)
    value = Column(Float, nullable=False)
    execution = relationship('Execution', back_populates='metrics')
    step = relationship('ExecutionStep', back_populates='metrics')
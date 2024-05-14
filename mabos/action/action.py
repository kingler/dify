from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum

class ActionStatusType(str, Enum):
    ACTIVE = "ActiveActionStatus"
    COMPLETED = "CompletedActionStatus"
    FAILED = "FailedActionStatus"
    POTENTIAL = "PotentialActionStatus"

class Action(BaseModel):
    """
    Represents an action that can be performed by an agent.
    Aligns with https://schema.org/Action
    """
    name: str = Field(..., description="The name of the action")
    target: Optional[str] = Field(None, description="An EntryPoint URL used to execute the action")
    actionStatus: Optional[ActionStatusType] = Field(None, description="Indicates the current disposition of the Action")
    agent: Optional[str] = Field(None, description="The direct performer or driver of the action (animate or inanimate)")
    participant: Optional[List[str]] = Field(None, description="Other co-agents that participated in the action indirectly")
    object: Optional[str] = Field(None, description="The object upon which the action is carried out")
    result: Optional[str] = Field(None, description="The result produced in the action")

    def execute(self):
        """
        Executes the action.
        """
        pass
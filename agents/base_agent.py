from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseAgent(ABC):
    """
    Base class for all agents in the swarm.
    """
    def __init__(self, agent_id: str):
        self.agent_id = agent_id

    @abstractmethod
    def observe(self, environment: Dict[str, Any]) -> Dict[str, Any]:
        """Observe the environment and return observations."""
        pass

    @abstractmethod
    def decide(self, observations: Dict[str, Any]) -> str:
        """Decide on an action based on observations."""
        pass

    @abstractmethod
    def act(self, action: str) -> Dict[str, Any]:
        """Execute the decided action and return the result."""
        pass
from typing import Dict, Any, List

class ContextManager:
    """
    Manages the shared global model (e.g., task queue, inventory).
    """
    def __init__(self):
        self.global_context = {
            "task_queue": [],
            "inventory": {},
            "agent_status": {}
        }

    def update_task_queue(self, task: Dict[str, Any]) -> None:
        """Update the global task queue."""
        self.global_context["task_queue"].append(task)

    def update_inventory(self, item: str, quantity: int) -> None:
        """Update the global inventory."""
        self.global_context["inventory"][item] = quantity

    def update_agent_status(self, agent_id: str, status: str) -> None:
        """Update an agent's status."""
        self.global_context["agent_status"][agent_id] = status

    def get_global_context(self) -> Dict[str, Any]:
        """Get the current global context."""
        return self.global_context
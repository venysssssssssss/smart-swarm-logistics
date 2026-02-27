from typing import Dict, Any, List

class WarehouseEnvironment:
    """
    Simulated warehouse environment with tasks and obstacles.
    """
    def __init__(self, width: int = 10, height: int = 10):
        self.width = width
        self.height = height
        self.tasks = []
        self.obstacles = []

    def add_task(self, task: Dict[str, Any]) -> None:
        """Add a task to the environment."""
        self.tasks.append(task)

    def add_obstacle(self, obstacle: Dict[str, Any]) -> None:
        """Add an obstacle to the environment."""
        self.obstacles.append(obstacle)

    def get_state(self) -> Dict[str, Any]:
        """Get the current state of the environment."""
        return {
            "tasks": self.tasks,
            "obstacles": self.obstacles,
            "dimensions": {"width": self.width, "height": self.height}
        }
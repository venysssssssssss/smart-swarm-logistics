import matplotlib
matplotlib.use('Agg')  # Define o backend para não-interativo
import matplotlib.pyplot as plt
from typing import Dict, Any

class WarehouseVisualizer:
    """
    Visualizes the warehouse environment and agent actions.
    Salva a visualização em warehouse_visualization.png
    """
    def __init__(self, environment: Dict[str, Any]):
        self.environment = environment

    def render(self) -> None:
        """Render the warehouse environment and save to file."""
        fig, ax = plt.subplots()
        ax.set_xlim(0, self.environment["dimensions"]["width"])
        ax.set_ylim(0, self.environment["dimensions"]["height"])

        # Draw obstacles
        for obstacle in self.environment["obstacles"]:
            ax.add_patch(plt.Rectangle(
                (obstacle["x"], obstacle["y"]),
                obstacle["width"],
                obstacle["height"],
                color="red"
            ))
        # Draw tasks
        for task in self.environment["tasks"]:
            ax.add_patch(plt.Rectangle(
                (task["x"], task["y"]),
                0.5,
                0.5,
                color="green"
            ))

        plt.title("Warehouse Environment")
        plt.savefig("warehouse_visualization.png")  
        plt.show()

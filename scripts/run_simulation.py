from agents.warehouse_agent import WarehouseAgent
from simulation.environment import WarehouseEnvironment
from simulation.visualizer import WarehouseVisualizer
from mcp.broker import MCPBroker
from mcp.context_manager import ContextManager

def run_simulation():
    """Run the warehouse simulation."""
    # Initialize environment
    env = WarehouseEnvironment(width=10, height=10)
    env.add_task({"x": 2, "y": 3, "type": "pick"})
    env.add_obstacle({"x": 5, "y": 5, "width": 1, "height": 1})

    # Initialize agents
    agent1 = WarehouseAgent("agent1")
    agent2 = WarehouseAgent("agent2")

    # Initialize MCP
    broker = MCPBroker()
    broker.connect()
    broker.start_loop()

    # Initialize context manager
    context_manager = ContextManager()

    # Visualize
    visualizer = WarehouseVisualizer(env.get_state())
    visualizer.render()

    print("Simulation started. Agents are ready to act!")

if __name__ == "__main__":
    run_simulation()
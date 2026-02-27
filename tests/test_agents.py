import unittest
from agents.warehouse_agent import WarehouseAgent

class TestWarehouseAgent(unittest.TestCase):
    def test_agent_initialization(self):
        agent = WarehouseAgent("test_agent")
        self.assertEqual(agent.agent_id, "test_agent")

if __name__ == "__main__":
    unittest.main()
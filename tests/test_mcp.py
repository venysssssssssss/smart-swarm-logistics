import unittest
from mcp.context_manager import ContextManager

class TestContextManager(unittest.TestCase):
    def test_context_update(self):
        manager = ContextManager()
        manager.update_task_queue({"task_id": 1, "type": "pick"})
        self.assertEqual(len(manager.get_global_context()["task_queue"]), 1)

if __name__ == "__main__":
    unittest.main()
from typing import Dict, Any
import numpy as np

class QLearningAgent:
    """
    Q-Learning agent for task selection.
    """
    def __init__(self, actions: list, learning_rate: float = 0.1, discount_factor: float = 0.9):
        self.actions = actions
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.q_table = {}

    def get_q_value(self, state: str, action: str) -> float:
        """Get Q-value for a state-action pair."""
        if state not in self.q_table:
            self.q_table[state] = {a: 0 for a in self.actions}
        return self.q_table[state][action]

    def update_q_value(self, state: str, action: str, reward: float, next_state: str) -> None:
        """Update Q-value using the Q-learning formula."""
        current_q = self.get_q_value(state, action)
        max_next_q = max([self.get_q_value(next_state, a) for a in self.actions])
        new_q = current_q + self.learning_rate * (reward + self.discount_factor * max_next_q - current_q)
        self.q_table[state][action] = new_q

    def choose_action(self, state: str, epsilon: float = 0.1) -> str:
        """Choose an action using epsilon-greedy policy."""
        if np.random.rand() < epsilon:
            return np.random.choice(self.actions)
        return max(self.q_table[state].items(), key=lambda x: x[1])[0]
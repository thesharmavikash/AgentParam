import numpy as np
import random
from agentscope.service import ServiceResponse

class LogicGym:
    """
    A simulated abstract environment for agents to practice ARC-style reasoning.
    Tasks involve pattern discovery, grid manipulation, and logical inference.
    """
    def __init__(self):
        self.tasks = [
            self.task_color_fill,
            self.task_symmetry,
            self.task_object_move
        ]

    def task_color_fill(self):
        grid = np.zeros((5, 5), dtype=int)
        grid[0, 0] = 1
        target = np.full((5, 5), 1)
        return "Task: Fill the entire 5x5 grid with the color 1. Current grid is all 0s except (0,0).", target

    def task_symmetry(self):
        grid = np.array([[1, 0, 0], [0, 0, 0], [0, 0, 0]])
        target = np.array([[1, 0, 1], [0, 0, 0], [1, 0, 1]])
        return "Task: Make the 3x3 grid symmetrical. Current: Top-left is 1.", target

    def task_object_move(self):
        grid = np.array([[0, 1, 0], [0, 0, 0], [0, 0, 0]])
        target = np.array([[0, 0, 0], [0, 0, 0], [0, 1, 0]])
        return "Task: Move the object (1) from the top row to the bottom row, middle column.", target

    def generate_random_puzzle(self) -> ServiceResponse:
        task_func = random.choice(self.tasks)
        desc, target = task_func()
        return ServiceResponse(
            status=ServiceResponse.SUCCESS,
            content=f"REASONING_PUZZLE:\n{desc}\nTarget State:\n{target.tolist()}"
        )

def run_logic_gym_session() -> ServiceResponse:
    gym = LogicGym()
    return gym.generate_random_puzzle()

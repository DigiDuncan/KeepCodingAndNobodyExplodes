Answer = tuple[bool, str]

class BombModule:
    def __init__(self):
        self.solved = False

    def attempt_solve(self) -> Answer:
        raise NotImplementedError

    def setup(self):
        raise NotImplementedError

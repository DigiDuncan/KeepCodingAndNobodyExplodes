from typing import Literal, Type

from kcane.lib.bombmodule import BombModule

Indicator = tuple[bool, str]
Port = Literal("dvi", "parallel", "ps2", "rj45", "serial", "rca")

class Bomb:
    def __init__(self, time: int = 300):
        self.serial: str = None
        self.indicators: list[Indicator] = []
        self.ports: list[Port] = []
        self.batteries: int = None
        self.module_count = None

        self.modules = list[BombModule]

        self.strikes = 0
        self._timer = time

    @property
    def timer(self) -> int:
        return int(self.timer)
    
    @property
    def solved(self) -> bool:
        return all([m.solved for m in self.modules]) and self.module_count is not None and self.module_count == len(self.modules)

    def update(self, delta_time: float) -> None:
        self._timer -= delta_time

    def setup(self, serial: str, batteries: int, indicators: list[Indicator], ports: list[Port]) -> None:
        self.serial = serial
        self.batteries = batteries
        self.indicators = indicators
        self.ports = ports

    def install_module(self, t: Type[BombModule]):
        mod = t()
        self.modules.append(mod)
        mod.setup()

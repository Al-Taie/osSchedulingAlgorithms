from dataclasses import dataclass, field


@dataclass
class Process:
    name: str
    arrival_time: int
    burst_time: int
    waiting_time: int = field(init=False, default=0)
    turnaround_time: int = field(init=False, default=0)

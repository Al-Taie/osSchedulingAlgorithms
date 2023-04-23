from dataclasses import dataclass, field


@dataclass(order=True)
class Process:
    name: str
    arrival_time: int
    burst_time: int
    priority: int = field(init=True, default=0)
    waiting_time: int = field(init=False, default=0)
    turnaround_time: int = field(init=False, default=0)
    remaining_time: int = field(init=False, default=0, repr=True)
    next_arrival_time: int = field(init=False, default=0, repr=False)

    def __post_init__(self):
        self.remaining_time = self.burst_time
        self.next_arrival_time = self.arrival_time


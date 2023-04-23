from dataclasses import dataclass


@dataclass(order=True)
class GanttChart:
    name: str
    arrival_time: int


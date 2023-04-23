from utils import Process
from collections import namedtuple

SJF_EXAMPLES = [
    # EXAMPLE 1 (p.10)
    [
        Process(name="P1", arrival_time=0, burst_time=7),
        Process(name="P2", arrival_time=1, burst_time=5),
        Process(name="P3", arrival_time=3, burst_time=2),
        Process(name="P4", arrival_time=4, burst_time=3),
    ],

    # EXAMPLE 2 (p.11)
    [
        Process(name="P1", arrival_time=2, burst_time=6),
        Process(name="P2", arrival_time=5, burst_time=2),
        Process(name="P3", arrival_time=1, burst_time=8),
        Process(name="P4", arrival_time=0, burst_time=3),
        Process(name="P5", arrival_time=4, burst_time=4),
    ],

    # EXAMPLE 3 (p.13)
    [
        Process(name="P1", arrival_time=0, burst_time=6),
        Process(name="P2", arrival_time=0, burst_time=8),
        Process(name="P3", arrival_time=0, burst_time=7),
        Process(name="P4", arrival_time=0, burst_time=3),
    ],

    # EXAMPLE 4 (p.13)
    [
        Process(name="P1", arrival_time=0, burst_time=7),
        Process(name="P2", arrival_time=2, burst_time=4),
        Process(name="P3", arrival_time=4, burst_time=1),
        Process(name="P4", arrival_time=5, burst_time=4),
    ],
]

FCFS_EXAMPLES = [
    # EXAMPLE 1 (p.8)
    [
        Process(name="P1", arrival_time=0, burst_time=15),
        Process(name="P2", arrival_time=2, burst_time=6),
        Process(name="P3", arrival_time=3, burst_time=7),
        Process(name="P4", arrival_time=5, burst_time=5),
    ],
    # EXAMPLE 2 (p.9)
    [
        Process(name="A", arrival_time=0, burst_time=9),
        Process(name="B", arrival_time=1, burst_time=5),
        Process(name="C", arrival_time=2, burst_time=2),
        Process(name="D", arrival_time=3, burst_time=6),
        Process(name="E", arrival_time=4, burst_time=8),
    ],
)

ROUND_ROBIN_EXAMPLES = namedtuple("Examples", ['example1', 'example2'])(
    # EXAMPLE 1 (p.14)
    example1=namedtuple('Example1', ['processes', 'time_slice'])(
        processes=[
            Process(name='P1', arrival_time=0, burst_time=10),
            Process(name='P2', arrival_time=1, burst_time=5),
            Process(name='P3', arrival_time=3, burst_time=2),
            Process(name='P4', arrival_time=4, burst_time=3),
        ],
        time_slice=3
    ),
    # EXAMPLE 2 (p.15)
    example2=namedtuple('Example2', ['processes', 'time_slice'])(
        processes=[
            Process(name='P1', arrival_time=0, burst_time=5),
            Process(name='P2', arrival_time=1, burst_time=3),
            Process(name='P3', arrival_time=2, burst_time=1),
            Process(name='P4', arrival_time=3, burst_time=2),
            Process(name='P5', arrival_time=4, burst_time=3),
        ],
        time_slice=2
    )
)

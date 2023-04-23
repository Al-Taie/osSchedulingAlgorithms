from statistics import mean
from prettytable import PrettyTable

from process import Process


def print_table(processes):
    if not processes:
        return

    table = PrettyTable()
    table.field_names = [
        "Process",
        "Arrival Time",
        "Burst Time",
        "Waiting Time",
        "Turnaround Time"]
    avg_waiting_time = mean(p.waiting_time for p in processes)
    avg_turnaround_time = mean(p.turnaround_time for p in processes)

    for p in processes:
        table.add_row([
            p.name,
            p.arrival_time,
            p.burst_time,
            p.waiting_time,
            p.turnaround_time])

    print(table)
    print(f"Average Waiting Time: {avg_waiting_time}", f"\nAverage Turnaround Time: {avg_turnaround_time}")


EXAMPLES = [
    # EXAMPLE 1
    [
        Process(name="P1", arrival_time=0, burst_time=7),
        Process(name="P2", arrival_time=1, burst_time=5),
        Process(name="P3", arrival_time=3, burst_time=2),
        Process(name="P4", arrival_time=4, burst_time=3),
    ],

    # EXAMPLE 2
    [
        Process(name="P1", arrival_time=2, burst_time=6),
        Process(name="P2", arrival_time=5, burst_time=2),
        Process(name="P3", arrival_time=1, burst_time=8),
        Process(name="P4", arrival_time=0, burst_time=3),
        Process(name="P5", arrival_time=4, burst_time=4),
    ],

    # EXAMPLE 3
    [
        Process(name="P1", arrival_time=0, burst_time=6),
        Process(name="P2", arrival_time=0, burst_time=8),
        Process(name="P3", arrival_time=0, burst_time=7),
        Process(name="P4", arrival_time=0, burst_time=3),
    ],

    # EXAMPLE 4
    [
        Process(name="P1", arrival_time=0, burst_time=7),
        Process(name="P2", arrival_time=2, burst_time=4),
        Process(name="P3", arrival_time=4, burst_time=1),
        Process(name="P4", arrival_time=5, burst_time=4),
    ],
]

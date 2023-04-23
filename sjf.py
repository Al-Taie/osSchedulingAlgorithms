from typing import List

from process import Process
from utils import print_table, EXAMPLES


def sjf(processes: List[Process]) -> None:
    """
    Non-Preemptive **Shortest Job First (SJF)** scheduling algorithm implementation

    ``An algorithm in which the process having the smallest execution time is chosen for the next execution.``
    `read more <https://www.guru99.com/shortest-job-first-sjf-scheduling.html>`_
    """
    executed = []
    current_time = 0
    while processes:
        arrived_processes = list(filter(lambda p: p.arrival_time <= current_time, processes))
        arrived_processes.sort(key=lambda p: p.burst_time)

        process = arrived_processes[0]
        processes.remove(process)

        process.waiting_time = max(0, current_time - process.arrival_time)
        process.turnaround_time = process.burst_time + process.waiting_time
        current_time += process.burst_time
        executed.append(process)

    print_table(executed)


if __name__ == '__main__':
    sjf(EXAMPLES[0])

from typing import List

from utils import print_table, Process, print_gantt_chart, GanttChart
from utils.examples import SJF_EXAMPLES


def sjf(processes: List[Process]) -> None:
    """
    Non-Preemptive **Shortest Job First (SJF)** scheduling algorithm implementation

    ``An algorithm in which the process having the smallest execution time is chosen for the next execution.``
    `read more <https://www.guru99.com/shortest-job-first-sjf-scheduling.html>`_
    """
    gantt_chart = []
    executed_queue = []
    current_time = 0
    while processes:
        arrived_processes = list(filter(lambda p: p.arrival_time <= current_time, processes))
        arrived_processes.sort(key=lambda p: p.burst_time)

        process = arrived_processes[0]
        processes.remove(process)

        process.waiting_time = max(0, current_time - process.arrival_time)
        process.turnaround_time = process.burst_time + process.waiting_time
        current_time += process.burst_time
        executed_queue.append(process)
        gantt_chart.append(GanttChart(name=process.name, arrival_time=current_time))

    print_gantt_chart(gantt_chart)
    print_table(executed_queue)


if __name__ == '__main__':
    sjf(SJF_EXAMPLES.example1)

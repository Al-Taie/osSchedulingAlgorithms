from typing import List

from utils import print_table, Process, GanttChart, print_gantt_chart
from utils.examples import FCFS_EXAMPLES


def fcfs(processes: List[Process]) -> None:
    """
    **First Come First Serve (FCFS)** scheduling algorithm implementation

    ``An algorithm that executes processes in order of their arrival, allocating CPU resources to the first process
    in the queue (FIFO).``

    `read more <https://www.guru99.com/fcfs-scheduling.html>`_
    """
    processes.sort(key=lambda p: p.arrival_time)
    current_time = 0
    gantt_chart = []

    for process in processes:
        process.waiting_time = max(0, current_time - process.arrival_time)
        process.turnaround_time = process.burst_time + process.waiting_time
        current_time += process.burst_time
        gantt_chart.append(GanttChart(name=process.name, arrival_time=current_time))

    print_gantt_chart(gantt_chart)
    print_table(processes)


if __name__ == '__main__':
    fcfs(FCFS_EXAMPLES.example1)


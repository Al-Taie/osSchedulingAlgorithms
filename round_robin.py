from typing import List

from utils.examples import ROUND_ROBIN_EXAMPLES
from utils import Process, print_table, GanttChart, print_gantt_chart


def round_robin(processes: List[Process], time_slice: int) -> None:
    """
    **Round Robin** scheduling algorithm implementation

    ``An algorithm that executes each ready process turn by turn only in a cyclic processes for a limited time slice.``

    `read more <https://www.guru99.com/round-robin-scheduling-example.html>`_
    """
    current_time = 0
    gantt_chart = []
    executed_queue = []

    while processes:
        processes.sort(key=lambda p: p.next_arrival_time)
        process = processes.pop(0)

        if process.remaining_time > time_slice:
            current_time += time_slice
            process.remaining_time -= time_slice
            process.next_arrival_time = current_time
            processes.append(process)
        else:
            current_time += process.remaining_time
            process.remaining_time = 0
            process.waiting_time = current_time - process.arrival_time - process.burst_time
            process.turnaround_time = current_time - process.arrival_time
            executed_queue.append(process)
        gantt_chart.append(GanttChart(name=process.name, arrival_time=current_time))

    print_gantt_chart(gantt_chart)
    print_table(executed_queue)


if __name__ == '__main__':
    example = ROUND_ROBIN_EXAMPLES.example2
    round_robin(processes=example.processes, time_slice=example.time_slice)

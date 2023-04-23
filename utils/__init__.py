from utils.process import Process
from statistics import mean
from typing import List
from prettytable import PrettyTable
from utils.ganta_chart import GanttChart
import re


def print_table(processes: List[Process]) -> None:
    if not processes:
        return

    processes.sort()
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


def print_gantt_chart(data: List[GanttChart]) -> None:
    if not data:
        return

    processes = '|'.join(f'  {p.name}  ' for p in data)
    processes = f'|{processes}|'
    matches = re.finditer(r'\|', processes)

    times = ['0'] + [str(p.arrival_time) for p in data]
    time_template = ' ' * (len(processes))

    for index, match in enumerate(matches):
        time_template = time_template[:match.start()] + times[index] + time_template[match.start():]

    print('Gantt Chart')
    print(processes)
    print(''.join(time_template), end='\n\n')


__all__ = [print_table, print_gantt_chart, Process, GanttChart]

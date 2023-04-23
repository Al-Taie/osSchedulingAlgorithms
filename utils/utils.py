from statistics import mean
from prettytable import PrettyTable


def print_table(processes) -> None:
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

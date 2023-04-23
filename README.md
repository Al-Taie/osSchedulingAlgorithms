
# CPU Scheduling Algorithms in Operating Systems

> **CPU Scheduling** is a process of determining which process will own CPU for execution while another process is on hold. 
<br> The main task of CPU scheduling is to make sure that whenever the CPU remains idle, the OS at least select one of the processes available in the ready queue for execution. 
<br> The selection process will be carried out by the CPU scheduler. 
It selects one of the processes in memory that are ready for execution.

### Types of CPU scheduling Algorithm
There are mainly six types of process scheduling algorithms

| Algorithm                     | Theory                                                                    | Implementation             |
|-------------------------------|---------------------------------------------------------------------------|----------------------------|
| First Come First Serve (FCFS) | [click me](https://www.guru99.com/fcfs-scheduling.html)                   | [click me](fcfs.py)        |
| Shortest-Job-First (SJF)      | [click me](https://www.guru99.com/shortest-job-first-sjf-scheduling.html) | [click me](sjf.py)         |
| Round Robin                   | [click me](https://www.guru99.com/round-robin-scheduling-example.html)    | [click me](round_robin.py) |
| Priority                      | [click me](https://www.guru99.com/priority-scheduling-program.html)       | [click me](#)              |
| Multilevel Queue              | [click me](#)                                                             | [click me](#)              |
| Shortest Remaining Time       | [click me](#)                                                             | [click me](#)              |


<br>

![Scheduling Algorithms.webp](images%2FScheduling%20Algorithms.png)

### First Come First Serve

> First Come First Serve is the full form of FCFS. It is the easiest and most simple CPU scheduling algorithm. In this type of algorithm, the process which requests the CPU gets the CPU allocation first. This scheduling method can be managed with a FIFO queue.

As the process enters the ready queue, its PCB (Process Control Block) is linked with the tail of the queue. So, when CPU becomes free, it should be assigned to the process at the beginning of the queue.

#### Characteristics of FCFS method:

> It offers non-preemptive and pre-emptive scheduling algorithm.

Jobs are always executed on a first-come, first-serve basis
It is easy to implement and use.
However, this method is poor in performance, and the general wait time is quite high.

### Shortest Remaining Time

> The full form of SRT is Shortest remaining time. It is also known as SJF preemptive scheduling. In this method, the process will be allocated to the task, which is closest to its completion. This method prevents a newer ready state process from holding the completion of an older process.

#### Characteristics of SRT scheduling method:
> This method is mostly applied in batch environments where short jobs are required to be given preference.

This is not an ideal method to implement it in a shared system where the required CPU time is unknown.
Associate with each process as the length of its next CPU burst. So that operating system uses these lengths, which helps to schedule the process with the shortest possible time.


### Priority Based Scheduling
> Priority scheduling is a method of scheduling processes based on priority. In this method, the scheduler selects the tasks to work as per the priority.

Priority scheduling also helps OS to involve priority assignments. 

The processes with higher priority should be carried out first, whereas jobs with equal priorities are carried out on a round-robin or FCFS basis. Priority can be decided based on memory requirements, time requirements, etc.

### Round-Robin Scheduling
Round robin is the oldest, simplest scheduling algorithm. The name of this algorithm comes from the round-robin principle, where each person gets an equal share of something in turn. It is mostly used for scheduling algorithms in multitasking. This algorithm method helps for starvation free execution of processes.

#### Characteristics of Round-Robin Scheduling
Round robin is a hybrid model which is clock-driven
Time slice should be minimum, which is assigned for a specific task to be processed. However, it may vary for different processes.
It is a real time system which responds to the event within a specific time limit.


### Shortest Job First
SJF is a full form of (Shortest job first) is a scheduling algorithm in which the process with the shortest execution time should be selected for execution next. This scheduling method can be preemptive or non-preemptive. It significantly reduces the average waiting time for other processes awaiting execution.

#### Characteristics of SJF Scheduling
It is associated with each job as a unit of time to complete.
In this method, when the CPU is available, the next process or job with the shortest completion time will be executed first.
It is Implemented with non-preemptive policy.
This algorithm method is useful for batch-type processing, where waiting for jobs to complete is not critical.
It improves job output by offering shorter jobs, which should be executed first, which mostly have a shorter turnaround time.


### Multiple-Level Queues Scheduling
This algorithm separates the ready queue into various separate queues. In this method, processes are assigned to a queue based on a specific property of the process, like the process priority, size of the memory, etc.

However, this is not an independent scheduling OS algorithm as it needs to use other types of algorithms in order to schedule the jobs.

#### Characteristic of Multiple-Level Queues Scheduling:
Multiple queues should be maintained for processes with some characteristics.
Every queue may have its separate scheduling algorithms.
Priorities are given for each queue.


### The Purpose of a Scheduling algorithm
Here are the reasons for using a scheduling algorithm:
* The CPU uses scheduling to improve its efficiency.
* It helps you to allocate resources among competing processes.
* The maximum utilization of CPU can be obtained with multi-programming.
* The processes which are to be executed are in ready queue.[[1]](https://www.guru99.com/cpu-scheduling-algorithms.html)

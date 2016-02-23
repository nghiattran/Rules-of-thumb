# Modern Operating Systems

---
## Chapter 2


### 2.3 INTERPROCESS COMMUNICATION

Three issues with **InterProcess Communication** (**IPC**):

1. How one process can pass information to another.
2. Making sure two or more processes do not get in each other’s way.
3. Proper sequencing

#### 2.3.3 Mutual Exclusion with Busy Waiting

##### The Test and Set Lock (TSL) Instruction

```
TSL RX,LOCK
```

1. Read the content at the memory address of lock into register `RX`.
2. Store a non-zero value at the memory address of `LOCK`.

Locking the memory bus is very different from disabling interrupts.

**Disabling interrupts** on processor 1 has no effect at all on processor 2.
**Locking memory bus** does not allow on processors to access the memory.

Use TSL to solve race condition:

1. When lock = 0, any process may set lock = 1 by using TSL instruction and go to its critical section.
2. When the process finish its critical section, set lock = 0 using the original move instruction.

```
enter region:
	TSL REGISTER,LOCK 			// copy lock to register and set lock to 1
	CMP REGISTER,#0				// was lock zero?
	JNE enter region			// if it was not zero, lock was set, so loop
	RET 						// return to caller; critical region entered
leave region:
	MOVE LOCK,#0 				// store a 0 in lock
	RET 						// return to caller
```

#### Busy waiting problems

Both Peterson’s solution and the TSL solution can solve race condition but they use a tight loop waiting to get into critical section which is wasting CPU time and cause **Priority Inversion problem**. 

Priority Inversion problem with busy waiting method:

* A computer with two processes P0 with high priorities, and P1 with low priorities.
* The scheduling rules are such that P0 get CPU time whenever it is in ready state.
* At a time moment, P1 is in critical section.
* P0 become to ready state. P0 posse CPU time and start to run.
* Since P1 is in critical section, P0 run busy waiting forever since P1 does not have a chance to get CPU time to finish its critical section.

#### 2.3.4 Sleep and Wakeup

Sleep and wakeup:

* Instead of busy waiting, it goes to sleeping state.
* Once a process finish its Critical section, it calls wakeup function which allows one of sleeping process get into its critical section.

##### The Producer-Consumer Problem

The **producer-consumer problem** (**bounded-buffer problem**):

* Two processes share a common, fixed-sized buffer.
* Producer puts information into the buffer, and consumer takes it out.
* When the producer wants to put a new item in the buffer, but it is already full.

	* Go to sleep, awakened by customer when customer has removed one or more items

* When the consumer tries to take a item from the buffer, but buffer is already empty.

	* Go to sleep, awakened by producer when producer has puts one or more items into buffer.

```cpp
void producer(void)
{
	int item;
	while (TRUE) { 								/* repeat forever */
		item = produce item( ); 				/* generate next item */
		if (count == N) sleep( ); 				/* if buffer is full, go to sleep */
		inser t item(item); 					/* put item in buffer */
		count = count + 1; 						/* increment count of items in buffer */
		if (count == 1) wakeup(consumer); 		/* was buffer empty? */
	}
}
void consumer(void)
{
	int item;
	while (TRUE) { 								/* repeat forever */
		if (count == 0) sleep( ); 				/* if buffer is empty, got to sleep */
		item = remove item( ); 					/* take item out of buffer */
		count = count − 1; 						/* decrement count of items in buffer */
		if (count == N − 1) wakeup(producer); 	/* was buffer full? */
		consume item(item); 					/* print item */
	}
}
```

Problems:

1. Initially buffer is empty, `count = 0`.
2. The consumer just reads `count = 0`, since the consumer’s CPU time is over, scheduler assigns a CPU time to producer.
3. Producer produces item and checks count, `count = 0`. Insert item to buffer.Increase `count = count +1`. Now, since `count = 1`, it calls wakeup(consumer). Since the consumer is not sleeping yet, consumer misses the wakeup signal.
4. Consumer gets CPU time. Consumer already read `count = 0`, consumer goes to sleep.
5. Producer keep produce items and finally buffer become full. The producer go to sleep. Both sleep forever.

Quick fix by adding wakeup waiting bit:

* When a wakeup is sent to a consumer that is still awake, this bit is set.
* When the consumer tries to go to sleep:
	* If the wakeup waiting bit is on, it will be turned off, but the process will stay awake.

### 2.3.5 Semaphores

> **Semaphore** is integer variable type that counts the number of wakeups saved for future use. 

Two operations on semaphores (generalizations of **sleep** and **wakeup**):

1. Down

	* Checks to see if the value is greater than 0:

		* If so, it decrements the value (i.e., uses up one stored wakeup) and just continues.
		* If the value is 0, the process is put to `sleep` without completing the `down` for the moment.
2. Up 

	* Increments the value of the semaphore addressed.
	* If one or more processes were sleeping on that semaphore (unable to complete an earlier down operation) one of them is chosen by the system and is allowed to complete its down.

Checking the value, changing it, and possibly going to sleep, are all done as a single, indivisible **atomic action**.

```cpp
#define N 100 							/* number of slots in the buffer */
typedef int semaphore;					/* semaphores are a special kind of int */
semaphore mutex = 1; 					/* controls access to critical region */
semaphore empty = N; 					/* counts empty buffer slots */
semaphore full = 0; 					/* counts full buffer slots */

void producer(void)
{
	int item;
	while (TRUE) { 						/* TRUE is the constant 1 */
		item = produce item( ); 		/* generate something to put in buffer */
		down(&empty); 					/* decrement empty count */
		down(&mutex); 					/* enter critical region */
		inser t item(item); 			/* put new item in buffer */
		up(&mutex); 					/* leave critical region */
		up(&full); 						/* increment count of full slots */
	}	
}
void consumer(void)
{
	int item;
	while (TRUE) {						/* infinite loop */
		down(&full); 					/* decrement full count */
		down(&mutex);					/* enter critical region */
		item = remove item( ); 			/* take item from buffer */
		up(&mutex); 					/* leave critical region */
		up(&empty); 					/* increment count of empty slots */
		consume item(item); 			/* do something with the item */
	}
}
```

> Semaphores that are initialized to 1 and used by two or more processes to ensure that only one of them can enter its critical region at the same time are called **binary semaphores** (semaphore that only has 2 values).

### 2.3.6 Mutexes

> A **mutex** is a shared variable that can be in one of two states: unlocked or locked.

When a thread (or process) needs access to a critical region, it calls **mutex lock**:

* If the mutex is currently unlocked (meaning that the critical region is available), the call succeeds and the calling thread is free to enter the critical region.

* If the mutex is already locked, the calling thread is blocked until the thread in the critical region is finished and calls mutex unlock.

* If multiple threads are blocked on the mutex, one of them is chosen at random and allowed to acquire the lock.

### 2.3.7 Monitors

> A **monitor** is a collection of procedures, variables, and data structures that are all grouped together in a special kind of module or package.

In monitor, only one process can be active in a monitor at any instant. Monitor uses **conditional variables** along with two operations on them, wait and signal.

When a monitor procedure discovers that it cannot continue (e.g., the producer finds the buffer full), it does a *wait* on some condition variable. This action causes the calling process to block.

On the other hand, the consumer can wake up its sleeping partner by doing a *signal* on the condition variable that its partner is waiting on.

This can cause two active processes at the same time so Hoare and Brinch Hansen proposed two solutions:

* Hoare: Letting the newly awakened process run, suspending the other one.
* Hansen: Requiring that a process doing a signal must exit the monitor immediately. If a signal is done on a condition variable on which several processes are waiting, only one of them, determined by the system scheduler, is revived.

## 2.4 SCHEDULING

When a computer is multiprogrammed, it frequently has multiple processes or threads competing for a CPU at the same time. If only one CPU is available, *scheduler* has to be made which process to run next by using **scheduling algorithm**. 

### 2.4.1 Introduction to Scheduling

In addition to picking the right process to run, the scheduler also has to worry about making efficient use of the CPU because process switching is expensive.

* First a switch from user mode to kernel mode must occur
* The state of the current process must be saved, including storing its registers in the process table so they can be reloaded later.
* A new process must be selected by running the scheduling algorithm.
* Then the memory management unit must be reloaded with the memory map of the new process.
* Finally, the new process must be started.
* In addition, the process switch may invalidate the memory cache and related tables, forcing it to be dynamically reloaded from the main memory twice.

##### Process Behavior

Process that spend most of their time computing are called **compute-bound** or **CPU-bound**, and processes that spend most of their time waiting for I/O are called **I/O bound**. 

##### When to Schedule

Situations in which scheduling is needed:

1. When a new process is created, a decision needs to be made whether to run the parent process or the child process.
2. When a process exits, some other process must be chosen from the set of ready processes
3. When a process blocks on I/O, on a semaphore, or for some other reasons.
4. When an I/O interrupt occurs.

Two categories of scheduling algorithms with respect to how they deal with clock interrupts:

1. A nonpreemptive scheduling algorithm picks a process to run and then just lets it run until it blocks or voluntarily releases the CPU.
2. A preemptive scheduling algorithm picks a process and lets it run for a maximum of some fixed time.

##### Categories of Scheduling Algorithms

Different scheduling algorithms are needed in different environments. Three environments worth distinguishing are:

1. Batch:

	* Nonpreemptive algorithms, or preemptive algorithms with long time periods for each process, are often acceptable
	* Reduces process switches and thus improves performance

2. Interactive:

	* With interactive users, preemption is essential to keep one process from hogging the CPU and denying service to the others

3. Real time:

	* Preemption is, oddly enough, sometimes not needed because the processes know that they may not run for long periods of time and usually do their work and block quickly

##### Scheduling Algorithm Goals

Some goals for a scheduling algorithm:

* All systems

	* Fair ness - giving each process a fair share of the CPU
	* Policy enforcement - seeing that stated policy is carried out
	* Balance - keeping all parts of the system busy

* Batch systems

	* Throughput - maximize jobs per hour
	* Turnaround time - minimize time between submission and termination
	* CPU utilization - keep the CPU busy all the time

* Interactive systems

	* Response time - respond to requests quickly
	* Propor tionality - meet users’ expectations

* Real-time systems

	* Meeting deadlines - avoid losing data
	* Predictability - avoid quality degradation in multimedia systems

#### 2.4.2 Scheduling in Batch Systems

##### First-Come, First-Served

Basically, there is a single queue of ready processes. All incomming processes will be push into the queue and executed in order.

Strengths:

* Easy to understand and equally easy to program
* Fair in the same sense that allocating scarce resources

Weaknesses:

* If some biggest requests come first the average delay will be very high

##### Shortest Job First

The scheduler picks the **shortest job first** (the process that can be done in the shortest time)

It is worth pointing out that shortest job first is optimal only when all the jobs are available simultaneously. Jobs arrive at different time, the scheduler only picks the shortest job available at a time which might not be optimal.

##### Shortest Remaining Time Next

A preemptive version of shortest job first is **shortest remaining time next**. With this algorithm, the scheduler always chooses the process whose remaining run time is the shortest. This scheme allows scheduler to pick the optimal solution.

#### 2.4.3 Scheduling in Interactive Systems

##### Round-Robin Scheduling

Round-Robin: each process is assigned a time interval, called its **quantum**, during which it is allowed to run. If the process is still running at the end of the quantum, the CPU is preempted and given to another process. If the process has blocked or finished before the quantum has elapsed, the CPU switching is done when the process
blocks, of course. 

One issue with Round-Robin is the length of quantum. 

* If the length of quantum is too short, scheduler has to switch from process to process in a very short period of time and switching operation is both unuseful and resource-consumming.

* If the length of quantum is too long, the whole system will experience delays since other processes have to wait for the running process to finish.

Setting the quantum too short causes too many process switches and lowers the CPU efficiency, but setting it too long may cause poor response to short interactive requests. 

##### Priority Scheduling

The basic idea is straightforward: each process is assigned a priority, and the runnable process with the highest priority is allowed to run. Even on a PC with a single owner, there may be multiple processes, some of them more important than others

To prevent high-priority processes from running indefinitely, the scheduler may decrease the priority of the currently running process at each clock tick which causes its priority to drop below that of the next highest process, so a process switch occurs.

Ways to define process priority:

* Internal way: based on the measurable quantity or quantities to compute the priority of a process.
* External way: based on the importance of the process

One problems with priority scheduling is the **Starvation** of lower priority process. Processes with lowest priority might never be executed if higher priority processes keep comming.

But it can be solved using **aging**. A aging is a technique of gradually increasing the priorities of processes that wait in the system for a long time.

## Chapter 3: MEMORY MANAGEMENT

**Memory hierarchy**:

* Small, fast, very expensive registers,
* Volatile, expensive cache memory,
* Megabyte medium-speed, medium-speed RAM
* Huge size of slow cheap, non-volatile disk storage (Hard Disks)

**Memory management** is a part of operating system which manage the memory hierarchy. Its job is to efficiently manage memory: keep track of which parts of memory are in use, allocate memory to processes when they need it, and deallocate it when they are done.

### 3.1 NO MEMORY ABSTRACTION

Three options to organize memory:

* Operating system at the bottom of memory in RAM.
* OS in ROM (Read-Only Memory) at the top of memory.
* The device drivers may be at the top of memory in a ROM and the rest of the system in RAM down below

![alt text](memory-organizarion.png "Three options to organize memory")

Models (a) and (c) have the disadvantage that a bug in the user program can wipe out the operating system, possibly with disastrous results.

##### Running Multiple Programs Without a Memory Abstraction

However, even with no memory abstraction, it is possible to do multiprogramming if the operating system saves the entire contents of memory to a disk file, then bring in and run the next program. This concept is called **swapping**.

With the addition of some special hardware, it is possible to run multiple programs concurrently, even without swapping. The early models of the IBM 360 solved the problem as follows. Memory was divided into 2-KB blocks and each was assigned a 4-bit protection key held in special registers inside the CPU. A machine with a 1-MB memory needed only 512 of these 4-bit registers for a total of 256 bytes of key storage. The PSW (Program Status Word) also contained a 4-bit key. The 360 hardware trapped any attempt by a running process to access memory with a protection code different from the PSW key. Since only the operating system could change the protection keys, user processes were prevented from interfering with one another and with the operating system itself.

The core problem here is that the two programs reference absolute physical
memory but what they actually mean is relative memory of the program as the following.

![alt text](memory-multiprocess-problem.png "Problem with Running Multiple Programs Without a Memory Abstraction")

In this case, the program 2 (figure b), JMP to 28 which does CMP. But when loaded to memory, JMP to 28 means doing MOV instruction of program 1 (figure 1).

To solve this problem, the OS will automatically was loaded at address 16,384, 28 will be added to every program address during the load process so the instruction JMP 28 would be JMP 16,412 instead.

### 3.2 A MEMORY ABSTRACTION: ADDRESS SPACES

Exposing physical memory to processes has several major drawbacks:

* If user programs can address every byte of memory, they can easily trash the operating system, intentionally or by accident, bringing the system to a grinding halt
* It is difficult to have multiple programs running at once

#### 3.2.1 The Notion of an Address Space

> An **address space** is the set of addresses that a process can use to address memory. Each process has its own address space, independent of those belonging to other processes

##### Base and Limit Registers

The classical solution is to equip each CPU with two special hardware registers, usually called the **base** and **limit** registers.

When these registers are used, programs are loaded into consecutive memory locations wherever there is room and without relocation during loading.

When a process is running, the base register is loaded with the physical address where its program begins in memory and the limit register is loaded with the length of the program.

So in the last example, program 1 will have base and limit as 0 and 16,384, respectively, program 2 will have base and limit as 16,384 and 32,768, respectively. So that when the process run `JMP 28` it will be treated as `JMP 16412`.

#### 3.2.2 Swapping



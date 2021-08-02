# Queue

Queues have two ends - **front-end** and **back-end** or **rear-end**. Items are added at the rear-end and removed from the front-end. The operation to add an item to the queue via the rear-end is known as **enqueue** and to remove from the front-end is known as **dequeue**.

We can say Queues follow the **FIFO** (first in first out) rule.

### Other Queue Terms

1. **Peek**: To see the first item in the queue (from the front-end). Also known as **inspection**.
2. **Overflow: **When one tries to enqueue an item in a full queue
3. **Underflow:** When one tries to dequeue an item from an empty queue

## Python Implementation

```python
# Enqueue
def enqueue(queue, item):
    queue.append(item)

# Dequeue
def isempty(queue):
    if len(queue) == 0:
        return True
    return False

def dequeue(queue):
    if not isempty(queue):
        queue.pop(0)
    else:
        print("Underflow Error")

# Peek
def peek(queue):
    return queue[0]

# Display
def display(queue):
    if isempty(queue):
        print("Queue is empty")
    else:
        for i in queue:
            print(i, end = " ")
     
         
```

## Deque

These are double-ended queues and here, elements can be added and deleted at either end

### Input Restricted Deque

Allows insertions at one end only, but deletion at both ends

### Output Restricted Deque

Allows deletions at only one end, by insertion at both ends

## Applications of Queue

1. Order in which passengers enter and leave a bus
2. To maintain an order for all printing requests in a common printer
3. The orders of calls in a call center
4. To decide the order for take-off and landing of flights
5. To plan the order to execute programs in the CPU
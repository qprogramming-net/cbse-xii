# Program Efficiency

The efficiency of an algorithm needs to be measured to determine whether they are **suitable** for **large scale tasks**. The quality or **performance** of an algorithm depends on internal and external factors:

1. Internal Factors:
   1. Time required to run
   2. Space (memory) required to run
2. **External Factors:**
   1. Size of input
   2. Speed of computer processor
   3. Quality of compiler

We can control external factors to some effect and hence determine the efficiency of the algorithm, also known as **complexity** based on the internal factors.

## Computational Complexity

The study of factors which determine how much resource is required to perform a computation. These resources are the internal factors **time and space**.

Complexity is not an absolute measure. It is a bounding function also known as a **growth function** which describes the resource requirements as the size of the input increases. It allows us to compare different algorithms for the same purpose based on a measure of its resource requirement.

### Efficiency and Effectiveness

Efficiency is a measure of the performance of the algorithm while effectiveness is a measure of how correctly the algorithm solves a problem.

## Calculating Complexity

The complexity of an algorithm is calculated based on the time required to run and the memory used by the program. The time is generally considered **more important** since we can adjust the memory in a computer. 

The actual run time of a computer (the experimental value of time complexity) is not a good measure of algorithm efficiency given that several external factors such as the speed of the processor, RAM, compiler come into play and vary by machine. Therefore, we need to create a mathematical expression of the time complexity of a program and we can do so using the **Big-O Notation**.

## Big-O Notation

The Big-O Notation is used to mathematically represent the growth rate of an algorithm. It gives us an estimate of how the algorithm's **performance** will be affected when the input grows. The Big-O notation represents the **upper bound** of the algorithm's performance i.e. the maximum.

For example, if we have an algorithm having a time complexity of $O(n^3)$ which runs on an input with size $n$, the algorithm will take at maximum, $n^3$ steps to execute.

This mathematical representation allows us to compare the growth rates of two algorithms in order to determine which one will be more efficient for a task. Let's look at an example to understand this better:

**To solve a problem, two algorithms are used, one with time complexity $O(n)$ and the other with $O(\sqrt{n})$. Which will be the better option?**

Let's see this carefully. Let's assume $n$ is a large number. We know that the square root of a number is always less than the number itself, so the second algorithm will need fewer steps to execute.

We can also use real values to show this result:

|            | 1    | 100  | 10000 |
| ---------- | ---- | ---- | ----- |
| $n$        | 1    | 100  | 10000 |
| $\sqrt{n}$ | 1    | 10   | 100   |

You can see that as the input gets larger, the ratio of the complexities $\frac{\sqrt{n}}{n}$ becomes smaller and smaller.

We can visually see this in a graph:

<img src="C:\Users\kumar\AppData\Roaming\Typora\typora-user-images\image-20210801140115892.png" alt="image-20210801140115892" style="zoom:33%;" />

Here, the red is $O(n)$ and green is $O(\sqrt{n})$.

### Dominant Term

When we write an expression for the time complexity, we use a single term to describe it known as the **dominant term**. While the true expression may be different, in order to compare two complexities, a single term is better.

The dominant term is the term in the mathematical expression (a polynomial expression) having the highest power.

For example, in the expression $n^3 + 4n  + 5$ the term with the highest power is $n^3$, so we get the time complexity as $O(n^3)$.

Let's look at some common growth rates now:

| **Complexity** [Common Name] | **Real-Life Example**                 |
| ---------------------------- | ------------------------------------- |
| $O(1)$ [constant]            | Adding an element to a list           |
| $O(log \ n)$ [log]           | Binary Search                         |
| $O(n)$ [linear]              | Linear Search                         |
| $O(n \ log \ n)$ [n log n]   | Divide and conquer sort               |
| $O(n^2)$ [quadratic]         | Bubble sort and Insertion sort        |
| $O(n^3)$ [cubic]             | Solving simultaneous linear equations |
| $O(2^n)$ [exponential]       | Towers of Hanoi                       |

## Computation of Big-O

The first step to calculating the efficiency is to create a mathematical expression of the total time taken by a program.

To do so we have two components of each term in the expression:

1. **Constants:** These are represented by $c_n$ for some positive integer $n$ and represent a section of the program having constant execution time.

   For example, the statement `print(2)` has a constant execution time.

2. **Variables:** These are an exponent of $n$, for example $n^2$ and $n^5$. They represent values which depend on the size of the input, $n$

   For example, the total time taken for a  `for` loop to run depends on the input. If the input size is 100, it will take 100 iterations to run. Here, we assume the loop takes $n$ iterations to execute.

To get the full value of a term, we combine the constants and variables. For example, in the following program:

```python
for i in range(n): # variable
    print(i) # constant
```

the time taken to execute `print(i)` is constant, whereas the loop runs $n$ times. Thus, each time the loop runs, it takes a constant time, let's call it $c_0$ to run the `print` statement. So, the program would take a total time of $c_0 \times n$ to run. Thus, the expression of the time taken would be:
$$
Time = c_0n
$$
And the Big-O notation would be $O(n)$ ( we remove the constants attached to a variable).

Now, we must look at certain parts of a program and how we would represent their complexities. We **assume that each step in the execution takes the same time.**

1. **Loops**

   We already saw that a loop takes $c_0n$ time to execute. But what if we have nested loops?

   ```python
   for i in range(n):
       for j in range(n):
           print(i,j) # constant
   ```

   Here, we know that the `print` statement will take a constant time, let's say $c_0$ to execute.

   For the loops, each loop will iterate $n$ times so in total, they will iterate $n^2$ times.

   Thus, we get the final expression as:
   $$
   Time = c_0\times n \times n = c_0n^2
   $$
   So, the Big-O notation will be $O(n^2)$.

   Let's now consider a case where the loops have separate number of iterations:

   ```python
   for i in range(n):
       for j in range(m):
           print(i,j) # constant	
   ```

   Here, the `print` will again have constant time $c_0$ while the loops will execute $n \times m$ times in total, giving the final expression as:
   $$
   Time = c_0mn
   $$
   And the Big-O notation will be $O(mn)$

2. **Consecutive Statements**

   We add the time complexity of each statement to get the final complexity. For example:

   ```python
   	# Statement 1
   print("Let's run a program") # 1st constant
   
   # Statement 2
   for i in range(n):
       print(i) # 2nd constant
       
   # Statement 3
   for j in range(n):
       for k in range(n):
           print(k) # 3rd constant
   ```

   Here, the first `print` will take constant time $c_0$ , the second will take tie $c_1$ and the third $c2$.

   In the first loop, the total time taken will be $c_1n$ while in the second it will be $c_2n^2$. So, we add the time complexities of all three statements to get:
   $$
   Time = c_0 + c_1n + c_2n^2
   $$
   And here, the dominant term is $c_2n^2$, so the Big-O notation will be $O(n^2)$.

3. **Conditionals**

   We need to consider the worst-case running time, so we take the time taken by checking the condition and add the time taken by the indented block having maximum complexity.

   Example:

   ```python
   For numbe
   ```

4. **Logarithms**

## Best, Average and Worst Case

### Best Case

The minimum number of steps taken by an algorithm for an input of size $n$.

### Average Case

The average number of steps taken by an algorithm for an input of size $n$.

### Worst Case

The minimum number of steps taken by an algorithm for an input of size $n$. The Big-O Notation is the worst case complexity of an algorithm.

We use the worst-case for measuring algorithm efficiency since it provides an upper bound on the run time and also guarantees that the algorithm will not exceed a certain number of steps.

### Linear Search

| Case    | Time                 | Big-O  |
| ------- | -------------------- | ------ |
| Best    | $Time = 1$           | $O(1)$ |
| Average | $Time = \frac{n}{2}$ | $O(n)$ |
| Worst   | $Time = n$           | $O(n)$ |




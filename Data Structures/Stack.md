# Stack

## Operations

### Push

Adding an element to the **top** of the stack. Also known as insertion of an element

### Pop

Removing the top element from a stack.

## Other Terms

1. **Peek:** See the top element without removing it
2. **Underflow:** Trying to remove the top from an empty stack produces an underflow error
3. **Overflow:** When a stack has filled its maximum capacity and you try to add a new element, it will produce an overflow error.

## Stack in Python

```python
# Push
def push(stack, item):
    stack.append(item)

# Pop
def isempty(stack):
    if len(stack) == 0:
        return True
    return False

def pop(stack):
    if not isempty(stack):
        print("Popping", stack.pop())
    else:
        print("Underflow error")
  
def peek(stack):
    return stack[-1]

def display(stack):
   	if isempty(stack):
        print("Stack Empty")
    else:
        for i in stack[::-1]:
            print(i)
```

## Applications

1. **Reversing a String**

   Append all characters from left to right to stack, and then pop all elements.

2. **Polish Strings**

   To evaluate arithmetic expressions

   


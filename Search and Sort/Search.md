# Searching

## Linear Search

```python
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
```

## Binary Search

### Iterative Method

```python
def binary_search(arr, x, l, u):
    
    while l <= u:
        mid = (l+u)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 
        else:
            u = mid - 1
            
	return -1
```


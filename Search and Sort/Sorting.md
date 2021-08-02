# Sorting

## Selection Sort

```python
def selection_sort(arr):
    for i in range(len(arr)):
        minimum = i
        for j in range(i+1, len(arr):
            if arr[minimum] > arr[j]:
                minimum = j
     
    	arr[i], arr[minimum] = arr[minimum], arr[i]
	return arr	
```

## Insertion Sort

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr
```

## Bubble Sort

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
	
```


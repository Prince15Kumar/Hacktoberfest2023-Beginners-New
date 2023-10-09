# Python Program for Insertion Sort

def insertionSort(arr):
    n = len(arr)   
      
    if n <= 1:
        return  
 
    for i in range(1, n):   
        key = arr[i]   
        j = i-1
        while j >= 0 and key < arr[j]:   
            arr[j+1] = arr[j]   
            j -= 1
        arr[j+1] = key   
  
# Sorting the array [12, 11, 13, 5, 6] using insertionSort
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print(arr)





Output:

Sorted array is:
[5, 6, 11, 12, 13]

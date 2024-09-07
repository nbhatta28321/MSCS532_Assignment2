import random
import time
import tracemalloc

def merge_sort(A): #function to divide the array

    if len(A) <= 1: #return when the array has only one element which is sorted
        return A
    
    middle = len(A) // 2  #divide into two halves
    left_half = A[:middle]
    right_half = A[middle:]

    left = merge_sort(left_half) # recursively called the array until it od size 1
    right = merge_sort(right_half)
    output = merge(left, right) #merge the array after the operation

    return output


def merge(left, right): #sorts the element and merges the array

    answer =[]

    i = j = 0
    while i < len(left) and j < len(right): #loop until there is no element on left half and right half
        if left[i] <= right[j]: # append the array to the left side until to sort the array in increasing order
            answer.append(left[i])
            i += 1
        else:
            answer.append(right[j])
            j += 1


    answer += left[i:] #merge the left and right halves of the sorted array
    answer += right[j:]
    
    return answer
    
# function to do the merge sort and print the value
tracemalloc.start()
start = time.time()
merge_sort(list(range(100)))
end = time.time()
current, peak_memory = tracemalloc.get_traced_memory()
tracemalloc.clear_traces()
print("Execution time for sorted numbers is {} with memory usage of {}".format(end-start, peak_memory / (1024 * 1024)))


tracemalloc.start()
start = time.time()
merge_sort(list(range(100, 0, -1)))
end = time.time()
current, peak_memory = tracemalloc.get_traced_memory()
tracemalloc.clear_traces()
print("Execution time for reverse sorted numbers is {} with memory usage of {}".format(end-start, peak_memory / (1024 * 1024)))


tracemalloc.start()
start = time.time()
randomNum = merge_sort([random.randint(1, 500) for _ in range(100)])
end = time.time()
current, peak_memory = tracemalloc.get_traced_memory()
tracemalloc.clear_traces()
print("Execution time for random numbers is {} with memory usage of {}".format(end-start, peak_memory / (1024 * 1024)))




"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
# def quicksort(array):
    
#     if len(array) <= 1:
#         return array
#     else:
#         return quicksort([x for x in array[1:] if x<array[0]]) + [array[0]] + quicksort([x for x in array[1:] if x>=array[0]])

def quicksort(arr):
    """ Quicksort a list

    :type arr: list
    :param arr: List to sort
    :returns: list -- Sorted list
    """
    if not arr:
        return []

    return quicksort([x for x in arr if x < arr[0]]) \
        + [x for x in arr if x == arr[0]] \
        + quicksort([x for x in arr if x > arr[0]])
        
test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)

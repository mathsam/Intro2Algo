def quick_sort(array, start=0, end=None):
    """Sort in ascending order: my partion method"""
    if end is None:
        end = len(array) - 1
    if end-start <= 0:
        return
    mid_val = array[end]
    left = start
    right = end
    while right > left:
        if array[left] <= mid_val:
            left += 1
        else:
            tmp_val = array[right]
            array[right] = array[left]
            right -= 1
            array[left] = tmp_val
    if array[left] < mid_val:
        left += 1
    quick_sort(array, start, left-1)
    quick_sort(array, left, end)


def quick_sort_classic(array, start=0, end=None):
    """Sort in ascending order: Cormen's partition method"""
    if end is None:
        end = len(array) - 1
    if end-start <= 0:
        return
    pivot_val = array[end]
    j = start
    for i in range(start, end):
        if array[i] <= pivot_val:
            array[i], array[j] = array[j], array[i]
            j += 1
    array[end], array[j] = array[j], array[end]
    quick_sort_classic(array, start, j-1)
    quick_sort_classic(array, j+1, end)

def quick_sort_original(array, start=0, end=None):
    """Sort in ascending order: Hoare's method"""
    if end is None:
        end = len(array) - 1
    if end-start <= 0:
        return
    pivot_val = array[start]
    left = start + 1
    right = end
    while right > left:
        while left < end and array[left] <= pivot_val:
            left += 1
        while right > left and array[right] > pivot_val:
            right -= 1
        array[left], array[right] = array[right], array[left]
    if array[left] < pivot_val:
        array[left], array[start] = array[start], array[left]
    quick_sort_original(array, start, left-1)
    quick_sort_original(array, left, end)

a = [4,3,2,1,2,3,5,1,2]
quick_sort_original(a)
print a
def quick_sort(array, start=0, end=None):
    """Sort in ascending order"""
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
    return array
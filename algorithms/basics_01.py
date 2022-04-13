# binary search - !! sorted list only !!

def binary_search(lst, item):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = int((low + high) / 2)
        guess = lst[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

# SORTED LIST
sample_list = [18, 23, 32, 43, 48, 65, 87, 902]
print(binary_search(sample_list, 902))

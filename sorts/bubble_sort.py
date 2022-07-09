def bubble_sort(unorder_list: list) -> list:
    """
    Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted. The algorithm, which is a comparison sort, is named for the way smaller or larger elements "bubble" to the top of the list.
    """
    array_length = len(unorder_list)
    maxSwap = array_length - 1
    noSwap = 0
    while noSwap <= maxSwap:
        for i in range(array_length - 1):
            noSwap += 1
            if i < array_length-1 and unorder_list[i] > unorder_list[i+1]:
                unorder_list[i], unorder_list[i+1] = unorder_list[i+1], unorder_list[i]
                noSwap -= 1
        array_length -= 1
        maxSwap -= 1
    return unorder_list

if __name__ == "__main__":
    print(bubble_sort([3,6,10,7,9]))
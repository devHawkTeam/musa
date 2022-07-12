from typing import List

def selection_sort(arr: List[int]) -> List[int]:
    """
    Selection sort algorithm is a simple sorting algorithm that works by
    selecting the smallest element from the array and moving it to the beginning.
    It is a comparison sort, meaning that it can be implemented using the
    minimum number of comparisons.
    
    Big-O notation:
    Time complexity: O(n^2)
    Space complexity: O(1)
    Best case: O(n^2)
    Worst case: O(n^2)
    Average case: O(n^2)
    """
    for i in range(len(arr)-1): 
        min_index = i 
        for j in range(i+1, len(arr)): 
            if arr[j] < arr[min_index]: 
                min_index = j 
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i] 
    return arr

if __name__ == "__main__":
    print(selection_sort([1, 2,3]))
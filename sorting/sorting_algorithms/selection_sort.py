
def visualize_sorting(arr, step_name, current_arr):
    """Visualize the current state of the array during sorting."""
    print(f"{step_name}: {current_arr}")


def selection_sort(arr, visualize=False):
    """
    Sorts an array using selection sort algorithm.
    
    Args:
        arr: List to be sorted
        visualize: If True, show the sorting process step by step
        
    Returns:
        List: Sorted array
    """
    myArr = arr.copy()
    n = len(myArr)
    
    for i in range(n):
        minIndex = i 
        for j in range(i + 1, n):
            if myArr[j] < myArr[minIndex]:
                minIndex = j
        
        # Swap elements if minIndex is different from i
        if minIndex != i:
            myArr[i], myArr[minIndex] = myArr[minIndex], myArr[i]
        
        if visualize:
            visualize_sorting(myArr, f"Pass {i}: Element {myArr[i]} placed at position {i}", myArr)

    return myArr
def visualize_sorting(arr, step_name, current_arr):
    """Visualize the current state of the array during sorting."""
    print(f"{step_name}: {current_arr}")


def bubble_sort(arr, visualize=False):
    """
    Sorts an array using bubble sort algorithm.
    
    Args:
        arr: List to be sorted
        visualize: If True, show the sorting process step by step
        
    Returns:
        List: Sorted array
    """
    myArr = arr.copy()
 
    for i in range(len(myArr)):
        for j in range(len(myArr)-i-1):
            if myArr[j] > myArr[j+1]:
                myArr[j], myArr[j+1] = myArr[j+1], myArr[j]
    
    return myArr
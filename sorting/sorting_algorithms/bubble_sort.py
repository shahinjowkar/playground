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
    itteration = len(myArr) - 1
    
    if visualize:
        print(f"Original array: {myArr}")
        print("Starting bubble sort...")
        print("-" * 40)
    
    while itteration > 0:
        if visualize:
            print(f"\nPass {len(myArr) - itteration}:")
        
        swapped = False
        for i in range(itteration):
            if myArr[i] > myArr[i+1]:
                # Swap elements
                myArr[i], myArr[i+1] = myArr[i+1], myArr[i]
                swapped = True
                
                if visualize:
                    print(f"  Swap {myArr[i+1]} and {myArr[i]}: {myArr}")
            elif visualize:
                print(f"  No swap needed: {myArr}")
        
        if visualize:
            print(f"  After pass {len(myArr) - itteration}: {myArr}")
        
        itteration -= 1
        
        # Early termination if no swaps occurred
        if not swapped and visualize:
            print("  No swaps occurred - array is sorted!")
            break
    
    if visualize:
        print("-" * 40)
        print(f"Final sorted array: {myArr}")
    
    return myArr
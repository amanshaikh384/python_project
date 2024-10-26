# Binary Search Algorithm
def binary_search(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1
    
    while low <= high:
        mid = (low + high) // 2
        mid_element = sorted_list[mid]
        
        if mid_element == target:
            return mid
        elif mid_element < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1

if __name__ == "__main__":
    sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = int(input("Enter Number To Search: "))
    
    index = binary_search(sorted_list, target)
    if index != -1:
        print(f"Element {target} found at index {index}.")
    else:
        print(f"Element {target} not found in the list.")

def binary_search(sorted_lst, target_value):
    """function that takes as input a sorted list and a target value and return True if the target value is in the sorted list"""

    n = len(sorted_lst)
    left = 0 
    right = n - 1
    middle = (left + right) // 2 
    #case if list is empty:
    if len(sorted_lst) == 0:
        return False
    #if the target value is the middle
    if target_value == sorted_lst[middle]:
        return True 
    #if the target value is smaller than the middle
    if target_value < sorted_lst[middle]:
        return binary_search(sorted_lst[:middle], target_value)
    #if the target value is bigger than the middle
    if target_value > sorted_lst[middle]:
        return binary_search(sorted_lst[middle+1:], target_value)
    
if __name__ == "__main__":
    print(binary_search([1, 2, 3, 4, 5, 7, 8, 9], 6))

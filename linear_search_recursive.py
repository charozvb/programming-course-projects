def linear_search(lst_numbers, target_value, index=0):
    """function that takes a list of numbers, a target value and a index, returns True if the target value is in the list"""
    if index != len(lst_numbers):
        #if the target value is found at lst[index]
        if lst_numbers[index] == target_value:
            return True
        else:
            return linear_search(lst_numbers, target_value, index +1)
    return False
        
if __name__ == "__main__":
    print(linear_search([2,3,6,5,9,1,7,8], 5))

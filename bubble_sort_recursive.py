def bubble_sort(lst):
    """function that takes a list and sorts it using bubblesort"""
    #counter to keep tracks of whether there were swaps or not
    swap_number = 0
    #for loop with swapping
    for number in range(len(lst)-1):
        if lst[number] > lst[number+1]:
            lst[number], lst[number+1] = lst[number+1], lst[number]
            swap_number += 1
    #if there were no swaps that means the list is already sorted    
    if swap_number == 0:
        return lst
    #otherwise, keep going over the function to swap
    else:
        return bubble_sort(lst)

if __name__ == "__main__":
    print(bubble_sort([1,3,6,5,4,7,8,2,9]))



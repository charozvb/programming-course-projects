import binary_search_recursive 
import linear_search_recursive
import bubble_sort_recursive
import get_random_list
import time


def main():
    for n in range(100, 200, 1):
        lst = get_random_list.get_random(1000, n)
        bubble_start = time.time()
        bubble_sort_recur = bubble_sort_recursive.bubble_sort(lst)
        bubble_end = time.time()
        bubble_runtime = bubble_end - bubble_start
        print(bubble_runtime, n)

if __name__ == "__main__":
    main()

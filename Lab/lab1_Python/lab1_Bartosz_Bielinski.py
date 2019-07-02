# Lab ASEiEd - exercise 1 - variuos sort algorithms
from random import randint
import time

list_size = 2500
min_range = 0
max_range = 10000


def main():
    unsorted_list = create_list(list_size, min_range, max_range)
    print(unsorted_list)

    start = time.time()

    bubble_sort_list = bubble_sort(unsorted_list)

    bubble_sort_end_time = time.time()
    print("Booble sort took %s" % (bubble_sort_end_time - start))
    print(bubble_sort_list)

    start = time.time()

    selection_sort_list = selection_sort(unsorted_list)

    selection_sort_end_time = time.time()
    print("Selection sort took %s" % (selection_sort_end_time - start))

    print(selection_sort_list)

    start = time.time()

    quick_sort_list = quick_sort(unsorted_list)

    quick_sort_end_time = time.time()
    print("Quick sort took %s" % (quick_sort_end_time - start))

    print(quick_sort_list)


def create_list(size, min_value, max_value):
    """
    Creating python list with size of param 'size' and with random elements from 'min_value' to 'max_value'.

    :param size: Amount of elements in created list
    :param min_value: minimum value that can be generated with randint
    :param max_value: maximum value that can be generated with randint
    :return: Python list with amount of elements equal to param 'size'
    """
    unsorted_list = []
    for i in range(size):
        unsorted_list.append(randint(min_value, max_value))

    return unsorted_list


def bubble_sort(unsorted_list):
    """
    Function sorting input list with bubble sort algorithm

    :param unsorted_list: input list with unsorted elements
    :return: copy of input list with sorted elements
    """
    sorted_list = unsorted_list.copy()

    posortowana = False

    while not posortowana:
        posortowana = True
        for i in range(len(sorted_list) - 1, 0, -1):
            if sorted_list[i] < sorted_list[i - 1]:
                sorted_list[i], sorted_list[i - 1] = sorted_list[i - 1], sorted_list[i]
                posortowana = False

    return sorted_list


def selection_sort(unsorted_list):
    """
    Function sorting input list with selection sort algorithm

    :param unsorted_list: input list with unsorted elements
    :return: copy of input list with sorted elements
    """

    sorted_list = unsorted_list.copy()

    for i in range(len(sorted_list)):
        min_elem = sorted_list[i]
        min_index = i
        for j in range(i, len(sorted_list), 1):
            if sorted_list[j] < min_elem:
                min_elem = sorted_list[j]
                min_index = j
        sorted_list[i], sorted_list[min_index] = sorted_list[min_index], sorted_list[i]

    return sorted_list


def quick_sort(unsorted_list):
    """
    Function sorting input list with selection quick sort algorithm.

    :param unsorted_list: input list with unsorted elements
    :return: copy of input list with sorted elements
    """
    sorted_list = unsorted_list.copy()

    quick_sort_step(sorted_list, 0, len(sorted_list) - 1)

    return sorted_list


def quick_sort_step(list_to_sort, beginning, end):
    """
    Function used by quick sort algorithm. This function is called recursively with smaller and smaller lists, it is 
    base mechanic of quick sort.
    
    :param list_to_sort: input list from current step of quick sort algorithm
    :param beginning: index of the element that is considered to be the first element of sublist
    :param end: index of the element that is considered to be the last element of sublist
    :return:
    """

    if beginning >= end:
        return

    else:
        pivot_value = list_to_sort[beginning]

        left_cursor = beginning + 1
        right_cursor = end

        end_iteration = False
        while not end_iteration:

            while left_cursor <= right_cursor and list_to_sort[left_cursor] <= pivot_value:
                left_cursor += 1

            while list_to_sort[right_cursor] >= pivot_value and right_cursor >= left_cursor:
                right_cursor -= 1

            if right_cursor < left_cursor:
                end_iteration = True

            else:
                list_to_sort[left_cursor], list_to_sort[right_cursor] = list_to_sort[right_cursor], list_to_sort[
                    left_cursor]

        list_to_sort[beginning], list_to_sort[right_cursor] = list_to_sort[right_cursor], list_to_sort[beginning]

        quick_sort_step(list_to_sort, beginning, right_cursor - 1)
        quick_sort_step(list_to_sort, right_cursor + 1, end)


if __name__ == '__main__':
    main()

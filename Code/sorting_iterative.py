#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check that all adjacent items are in order, return early if so
    for index, item in enumerate(items):
        if index < len(items)-1:
            if item > items[index + 1]:
                return False
    return True

def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order
    for index, item in enumerate(items):
        if index < len(items)-1:
            if item > items[index + 1]:
                print("index: {} index+1: {}".format(items[index], items[index + 1]))
                items[index], items[index + 1]  = items[index + 1], items[index]
                break
                
    if is_sorted(items) == False:
        bubble_sort(items)
                
    return items


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item

    curr_min = items[0]
    first_unsorted_num = 0

    for item in enumerate(items):
        for index, item in enumerate(items):
            if item < curr_min:
                curr_min = item
                i = index

        if curr_min < items[first_unsorted_num]:
           items[first_unsorted_num], items[i] = items[i], items[first_unsorted_num]
    
    return items



    





def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items

if __name__ == '__main__':
    array1 = [10, 7, 4, 9]
    array2 = [9, 19, 5, 4, 10, 1, 6]
    print(bubble_sort(array2))
    print(selection_sort(array2))
  
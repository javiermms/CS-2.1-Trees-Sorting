#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # start and end
    # TODO: Check that all adjacent items are in order, return early if so
    for index, item in enumerate(items):
        if index < len(items)-1:
            if item > items[index + 1]:
                return False
    return True
# already in order o(N) worst O(n2)
def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order
    # Do Swap 
    # in order -> if there is no swap its sorted
    if is_sorted(items) == True:
        return items

    for index in range(len(items)-1):
        if items[index] > items[index + 1]:
            print("index: {} index+1: {}".format(items[index], items[index + 1]))
            items[index], items[index + 1]  = items[index + 1], items[index]

    if is_sorted(items) == False:
        bubble_sort(items)
              
    return items

# already in order o(N2) worst O(n2)
def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum num in list
    # TODO: switch with first unsorted element 
    # TODO: what do you do when the min starts at the unsorted variable
    
    for unsorted_index in range(len(items)):
        curr_min = unsorted_index
        for index in range(unsorted_index+1, len(items)):
            if items[curr_min] > items[index]:
                curr_min = index

        items[curr_min], items[unsorted_index] = items[unsorted_index], items[curr_min]

    return items

'''
Look at individual swaps: 
print(items)
print('Swaps: {}, {}  index:{} min:{}'.format(items[unsorted_index], items[curr_min],  unsorted_index, items[curr_min]))
print('\n')
'''


# already in order o(n) worst O(n2)
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
    array2 = [9, 19, 5, 4, 10, 1, 6, 0, 2, 3]
    # probelm array2 = [1, 4, 5, 19, 10, 9, 6]
    # array2 = [1, 4, 5, 6, 10, 9, 19]
    # array2 = [1, 4, 5, 6, 9, 10, 19]
    # print(bubble_sort(array2))
    print(selection_sort(array1))
  
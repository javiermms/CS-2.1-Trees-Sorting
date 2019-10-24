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
                items[index], items[index + 1]  = items[index + 1], items[index]
                for index in range(index + 1):
                    if items[index] > items[index + 1]:
                        items[index], items[index + 1]  = items[index + 1], items[index]
                
    return items


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items

if __name__ == '__main__':
    array1 = [6, 7, 4, 5, 3, 1, 10, 2]
    array1 = [6, 4, 5, 3, 1, 7, 2, 10]
    array2 = [1, 2, 3, 4, 5, 6, 7, 8]
    array3 = [1, 2, 3, 0, 5, 6, 7, 8]
    print(bubble_sort(array1))
    print(is_sorted(array2))
    print(is_sorted(array3))
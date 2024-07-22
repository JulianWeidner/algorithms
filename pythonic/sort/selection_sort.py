"""
Selection Sort

Selection Sort is a simple comparison-based sorting algorithm. 
The idea behind selection sort is to divide the array into a sorted and an unsorted region
and repeatedly select the smallest (or largest, depending on the sorting order) element from the unsorted region 
and move it to the end of the sorted region. 
This process continues until all elements have been sorted.

Use Cases
- Small Datasets: Selection sort is useful for small datasets where the overhead of more complex algorithms is not justified.
- Memory Constraints: It is an in-place sorting algorithm, meaning it requires only a constant amount of additional memory space.
- Teaching and Learning: It is easy to understand and implement, making it a good choice for educational purposes to introduce basic sorting concepts.

Selection sort is not suitable for large datasets due to its O(n2) time complexity, which makes it inefficient compared to more advanced sorting algorithms like quicksort or mergesort.
"""

#given_list[0:len(given_list)]

given_list = [64, 25, 12, 22, 11, 90, 34, 78, 56, 43]


def selection_sort(given_list) -> list:

    i = len(given_list)

    for _ in range(len(given_list)):
        lowest_index_val = given_list[:i].index(min(given_list[:i]))
        removed = given_list.pop(lowest_index_val)
        print(given_list[:i])
        given_list.append(removed)
        print(given_list)
        i-=1

selection_sort(given_list=given_list)

    
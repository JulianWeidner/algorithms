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


def des_selection_sort(given) -> list:
    n = len(given)
    k = 0 #swapped list
    for _ in range(n):
        max_num_index = given[k:].index(max(given[k:])) #the maximum value index within the k-(len) array
        given[k], given[max_num_index+k] = given[max_num_index+k], given[k] # with k being the boundary, it 
        k +=1
    return given

def asc_selection_sort(given) -> list:
    #take an array, move the minimum value to the sorted section
    i = 0
    for _ in range(len(given)):
        min_val = min(given[i:])
        min_index = given[i:].index(min_val)
        given[i], given[min_index+i] = given[min_index+i], given[i]
        i+=1
    return given

print(given_list)
print(des_selection_sort(given=given_list[:]))
print(asc_selection_sort(given=given_list[:]))



    
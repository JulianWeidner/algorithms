#Given an array (or list) of elements, sort the elements in ascending (or descending) order.
given_list =  [64, 34, 25, 12, 22, 11, 90]


#function done with list.sort (in place)
#modifes the actual list
def bbl_sort(asc_or_dsc, given) -> list:
    given.sort(reverse=asc_or_dsc)
    return given

#function fone with sorted
#creates in new list
def bbl_sorted(asc_or_dsc, given) -> list:
    return sorted(given, reverse=asc_or_dsc)

print(bbl_sort(False, given_list))
print(bbl_sorted(True, given_list))


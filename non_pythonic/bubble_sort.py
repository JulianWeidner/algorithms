given_list =  [64, 34, 25, 12, 22, 11, 90]
# ascending [11, 12, 22, 25, 34, 64, 90]


def bbl_sort(given, reverse=False) -> list:
    max_index = len(given) - 1
    for _ in range(max_index): #when not using the value  just use ' _'
        i = 0
        k = 1
        while k <= max_index:
            #ascending
            if reverse == False: 
                if given[i] > given[k]:
                    tmp = given[i]
                    given[i] = given[k]
                    given[k] = tmp
            elif reverse == True:
                    #descending
                    if given[i] < given[k]:
                        tmp = given[i]
                        given[i] = given[k]
                        given[k] = tmp
            i+=1 
            k+=1
    return given
print(bbl_sort(given_list[:], False)) #since this is modifiing the original list, I could use given_list[:] to create a shallow list (a copy). Shouldn't matter in this instance, but would be good practice.
print(bbl_sort(given_list[:], True))


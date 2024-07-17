given_list =  [64, 34, 25, 12, 22, 11, 90]
# ascending [11, 12, 22, 25, 34, 64, 90]


def bbl_sort(given, reverse=False) -> list:
    for index in range(len(given)):
        i = 0
        k = 1
        while k <= len(given) - 1:
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
print(bbl_sort(given_list, True))
print(bbl_sort(given_list, False))


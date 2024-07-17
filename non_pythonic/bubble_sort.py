given_list =  [64, 34, 25, 12, 22, 11, 90]
# ascending [11, 12, 22, 25, 34, 64, 90]


def bbl_sort(given, reverse=False) -> list:
    i = 0
    k = 1
    for index in range(len(given)):
        i = 0
        k = 1
        if reverse == False:
            while k <= len(given) - 1:
                if given[i] > given[k]:
                    tmp = given[i]
                    given[i] = given[k]
                    given[k] = tmp
                i+=1 
                k+=1
        if reverse== True:
            while k <= len(given) - 1:
                if given[i] < given[k]:
                    tmp = given[i]
                    given[i] = given[k]
                    given[k] = tmp
                i+=1 
                k+=1
                    


    return given
    """
         elif reverse == True:
            while k <= len(given) - 1:
                if given[i] < given[k]:
                    tmp = given[k]
                    given[k] = given[i]
                    given[i] = tmp
                i+=1 
                k+=1
        return given
        """
       
    
print(bbl_sort(given_list, True))


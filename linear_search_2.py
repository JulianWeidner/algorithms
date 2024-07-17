given_list = [34, 7, 23, 32, 5, 62]

def linear_search(locate, given) -> int:
    ndx = 0 
    for num in given:
        if num == locate:
            print(f'located Val: {num} @ Index: {ndx}')
            return ndx
        ndx += 1
    print("Element not found")
    return -1
    

linear_search(25, given_list)



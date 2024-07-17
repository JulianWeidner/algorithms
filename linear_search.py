given_list = [34, 7, 23, 32, 5, 62]

def linear_search(locate, given) -> int:
    try:
        return given.index(locate)
    except Exception as e:
        print(f"Not Located: {e}")
        return None
    

linear_search(24, given_list)



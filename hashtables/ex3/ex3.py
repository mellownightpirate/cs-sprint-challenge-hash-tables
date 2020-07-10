def intersection(arrays):
    """
    YOUR CODE HERE
    """
    array_hash = {}
    repeating_elements = {}
    # go thorugh every element in all arrays
    for array in arrays:
        for element in array:
    # if it's not in hash already, add it
            if element not in array_hash:
                array_hash[element] = None
    # if it's in hash, add it to 'repeating elements' hash
            else:
                repeating_elements[element] = None
    # return a list of repeating elements
    return list(repeating_elements)


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

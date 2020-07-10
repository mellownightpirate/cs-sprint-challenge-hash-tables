# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # dictinoary with an entry for each file
    queries_dict = {query: [] for query in queries}
    # if last part of query is the same as filename add it to relevent entry in dict
    for file in files:
        query = file.split('/')[-1]
        if query in queries_dict:
            queries_dict[query].append(file)
    return [file for query in queries_dict for file in queries_dict[query]]


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))

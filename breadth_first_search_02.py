# find the shortest path from 1 to 14. 
# graph in list adjacent representation  

graph = {
    "1": ["2", "3"],
    "2": ["4", "5"],
    "4": ["8", "9"],
    "9": ["12"],
    "3": ["6", "7"],
    "6": ["10", "11"],
    "10": ["13", "14"]
    }

def breadth_first_search(graph, start, end):
    next_start = [(node, path + "," + node) for i, path in start if i in graph for node in graph[i]]
    for node, path in next_start:
        if node == end:
            return path
    else:
        return breadth_first_search(graph, next_start, end)

print(breadth_first_search(graph, [("1", "1")], "14"))

    





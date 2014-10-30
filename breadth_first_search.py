
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
    queue = []
    queue.append([start])
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == end:
            return path
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)
print(breadth_first_search(graph, "1", "14"))




# def earliest_ancestor(ancestors, starting_node, found=False):
#     '''
#     loop over the ancestors , then choose the lowest
#     parent until we got the last parent
#     returns their earliest known ancestor –
#     the one at the farthest distance ?
#     so recursive ?
#     '''
#     for child_1, child_2 in ancestors:
#         if child_2 == starting_node: #or child_1 == starting_node:maximum recursion depth exceeded in comparison
#             return earliest_ancestor(ancestors, child_1, True)

#     if found:
#         return starting_node
#     else:
#         return -1






# second way

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


class Graph:

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else: 
            raise IndexError("Nonexistent vertex")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for child_1 , child_2 in ancestors:
        graph.add_vertex(child_1)
        graph.add_vertex(child_2)

    for node in ancestors:
        graph.add_edge(node[1], node[0])


    '''
    Breadth-first search gives us the shortest path
    we need queue
    '''
    queue = Queue()
    queue.enqueue([starting_node])
    visited = set()
    results = []


    while queue.size() > 0:
        path = queue.dequeue()
        last_vert = path[-1]


        if last_vert not in visited:
            visited.add(last_vert)


        for neighbor in graph.get_neighbors(last_vert):
            # copy of each call/loop
            path = list(path)
            path.append(neighbor)
            # save in the storage of the queue
            queue.enqueue(path)
            results.append(path[-1])


        if not results:
            return -1
    return path[-1]

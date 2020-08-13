"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Nonexited vertice")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        q.enqueue(starting_vertex)
        visited = set()

        while q.size():
            ver = q.dequeue()
            if ver not in visited:
                visited.add(ver)
                print(ver)
                for neighbor in self.get_neighbors(ver):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        visited = set()
        s.push(starting_vertex)
        while s.size():
            ver = s.pop()
            if ver not in visited:
                print(ver)
                visited.add(ver)
                for neighbor in self.get_neighbors(ver):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        print(starting_vertex)
        if visited is None:
            visited = set()

        visited.add(starting_vertex)
        # this is a base case , here where we destroy the recursive
        # because if the list of neighbors is empty is not gonna work
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

    '''
    # this is another way
    def dft_recursive(self, start, visited=set()):
        print(start)
        visited.add(start)

        for n in self.get_neighbors(start):
            if n not in visited:
                self.dft_recursive(n , visited)
    '''
    '''
    def dft_r(self, start):
        visited = set()
        print(start)
        visited.add(start)
        for n in self.get_neighbors(start):
            if n not in visited:
                self.dft_r(n)
    '''

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # since it is breadth first search , so we are gonna use queue
        q = Queue()

        # track node that we have visited
        visited = set()
        path = [starting_vertex]
        q.enqueue(path)
        print("before path", path)

        while q.size():
            # the current path is a list
            path = q.dequeue()
            print("while path", path)
            traveling_node = path[-1]
            # print("Node" , traveling_node)
            if traveling_node == destination_vertex:
                return path

            if traveling_node not in visited:
                visited.add(traveling_node)

                for neighbor in self.get_neighbors(traveling_node):
                    # each call has its copy
                    copy_path = path[:]
                    copy_path.append(neighbor)

                    q.enqueue(copy_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        visited = set()
        s = Stack()
        s.push([starting_vertex])
        while s.size():
            path = s.pop()
            traveling_node = path[-1]
            print("while", traveling_node)
            if traveling_node == destination_vertex:
                return path

            if traveling_node not in visited:
                visited.add(traveling_node)

            for neighbor in self.get_neighbors(traveling_node):
                copy_path = path[:]
                copy_path.append(neighbor)

                s.push(copy_path)

    # def dfs_recursive(self, vertex, destination_vertex, path=[], visited=None):
    #     """
    #     Return a list containing a path from
    #     starting_vertex to destination_vertex in
    #     depth-first order.
    #     This should be done using recursion.
    #     """
    #     if visited is None:
    #         visited = set()

    #     visited.add(vertex)

    #     if len(path) == 0:
    #         path.append(vertex)

    #     if vertex == destination_vertex:
    #         return path

    #     for neighbor in self.get_neighbors(vertex):
    #         if neighbor not in visited:
    #             res = self.dfs_recursive(
    #                 neighbor, destination_vertex, path + [neighbor], visited)
    #             if res is not None:
    #                 return res

    def dfs_recursive(self, start, end, visited=None, path=None):
        if visited is None:
            visited = set()

        if path is None:
            path = []

        visited.add(start)

        # each call should have its own copy
        path = path + [start]
              # ^
        # works | same as 
        # path = list(path)
        # path.append(start)

        print("path" , path)
        if start == end:
            return path


            # self.vertice[start]
        for neighbor in self.get_neighbors(start):
            # base case
            if neighbor not in visited:
                res = self.dfs_recursive(neighbor, end, visited, path)
                if res is not None:
                    return res
        return None


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(3)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("bfs", graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print("dfs", graph.dfs_recursive(1, 6))

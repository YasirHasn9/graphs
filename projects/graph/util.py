
# Note: This Queue class is sub-optimal. Why?
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


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


# find the words in words

def word_ladder(start, end):
    # since it is search then we are gonna use bfs
    # also since it bfs then we are gonna use queue

    q = Queue()
    q.enqueue([start])
    visited = set()

    while q.size():
        # dequeue the path
        path = q.dequeue()
        # get the last word in the path
        last_word = path[-1]
        if last_word == end:
            return path

        if last_word not in visited:
            visited.add(last_word)

            for word in get_neighbors(last_word):
                q.enqueue(path + [word])

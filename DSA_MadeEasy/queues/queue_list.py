class Queue(object):
    def __init__(self):
        self.queue = []
    
    def enqueue(self,data):
        self.queue.insert(0,data)

    def dequeue(self):
        return self.queue.pop()
    def isEmpty(self):
        return not bool(self.queue)

    def size(self):
        return len(self.queue)
    
    def peek(self):
        return self.queue[-1]
    
    def __repr__(self):
        return '{}'.format(self.queue)

if __name__ == '__main__':
    queue = Queue()
    print("Is the queue empty? ", queue.isEmpty())
    print("Adding 0 to 10 in the queue...")
    for i in range(10):
        queue.enqueue(i)
    print("Queue size: ", queue.size())
    print("Queue peek : ", queue.peek())
    print("Dequeue...", queue.dequeue())
    print("Queue peek: ", queue.peek())
    print("Is the queue empty? ", queue.isEmpty())
    print(queue)        

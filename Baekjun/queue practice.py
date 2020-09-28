import queue
    
wait_line=queue.Queue()

wait_line.put(1)
wait_line.put(2)
wait_line.get(2)

wait_line.qsize()

stack1=queue.LifoQueue()

priority_q=queue.PriorityQueue()




import threading
import queue
import os

buffer_size = 5

lock = threading.Lock()
queue = queue.Queue(buffer_size)
file_count = 0

def producer(top_dir, queue_buffer):
    queue_buffer.put(top_dir,timeout=3)
    doc = os.listdir(top_dir)
    for i in doc:
        if(os.path.isdir(os.path.join(top_dir, i))):
            queue_buffer.put(os.path.join(top_dir, i))
            producer(os.path.join(top_dir, i), queue_buffer) 
    
def consumer(queue_buffer):
    global file_count
    try:
        data = queue_buffer.get(True,1) 
        files = os.listdir(data) 
        lock.acquire()
        if(os.path.isfile(os.path.join(dir, i))):
                lock.acquire()
                file_count += 1
                lock.release()

    except Exception as e:
        return


def main():
    producer_thread = threading.Thread(target = producer, args = ('./testdata', queue))
    consumer_count = 20
    consumers = []
    for i in range(consumer_count):
        consumers.append(threading.Thread(target = consumer, args = (queue,)))

    producer_thread.start()
    for c in consumers:
        c.start()

    producer_thread.join()
    for c in consumers:
        c.join()

    print(file_count, 'files found.')

if __name__ == "__main__":
    main()
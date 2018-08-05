#http://nbviewer.jupyter.org/github/x-village/OS_Lab/blob/master/Lab1.ipynb
import numpy as np

def main():
    # Generate random matrix and result matrix
    matA = np.random.randint(10, size = (1000, 1000))
    matB = np.random.randint(10, size = (1000, 1000))
    result = np.zeros((matA.shape[0], matB.shape[1]))
    result_multi = np.zeros((matA.shape[0], matB.shape[1]))
    result_multi02 = np.zeros((matA.shape[0], matB.shape[1]))

    matA_temp = []
    threads = []
    thread_num = 10

    # Compare with numpy's multiplication result
    #print('Answer is correct:', np.all(np.matmul(matA, matB) == result))
    

import multiprocessing
import random

#def thread_func(matA, matB, result, row):
#    result[row] = np.matmul(matA, matB)

def thread_func(matA, matB, result, row):
    result[row] = np.matmul(matA, matB)

def thread_func_02(matA, matB, result, rows, i):
    for j in range(rows):
        result[i * rows + j] = np.matmul(matA[j], matB)

def multithread_func(matA, matB, result_queue, i):
    result_queue.put((np.matmul(matA, matB), i))

for i in range(thread_num):
        matA_temp = matA[matA.shape[0] // thread_num * i : matA.shape[0] // thread_num * (i + 1), 0:matA.shape[1]]
        thread = threading.Thread(target = thread_func_02, args = (matA_temp, matB, result, matA.shape[0] // thread_num, i))
        threads.append(thread)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    end_time = time.time()

###

def main():
    # Generate queue for communication
    result_queue = multiprocessing.Manager().Queue()

    processes = 10
    jobs = []

    for i in range(processes):
        matA_temp = matA[matA.shape[0] // thread_num * i : matA.shape[0] // thread_num * (i + 1), 0:matA.shape[1]]
        process = multiprocessing.Process(target = thread_func, args = (i, result_queue))
        jobs.append(process)

    for process in jobs:
        process.start()

    for process in jobs:
        process.join()

    while not result_queue.empty():
        result = result_queue.get()
        print(result)

#time
import time

def main():
    start_time = time.time()
    for row in range(0, matA.shape[0]):
        result_normal[row] = np.matmul(matA[row], matB)

    end_time = time.time()

# Compare with numpy's multiplication result
    print('Answer is correct:', np.all(np.matmul(matA, matB) == result))
    print('Time elapsed:\t', end_time - start_time)

if __name__ == "__main__":
    main()


#Q1 - Lab1-矩陣平行運算
#Q2 - 分別利用multi-thread和multi-process進行矩陣平行運算
#Q3 - 需要和numpy計算的結果做比對，確保答案正確
#Q4 - 需要計時，並和原本未使用thread或process加速的狀況做效能比較
#Q5 - 隨機產生 10x10 / 100x100 / 1000x1000 的矩陣進行測試，比對不同計算量下的效能提昇

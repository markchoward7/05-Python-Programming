import threading, time

# start = time.perf_counter()

# def do_something(num):
#     print("sleeping %d second(s)" % num)
#     time.sleep(num)
#     print("done sleeping")

# threads =[threading.Thread(target=do_something, args=[5]) for _ in range(10000)]

# for thread in threads:
#     thread.start()

# for thread in threads:
#     thread.join()

# finish = time.perf_counter()

# print('finished in:', finish - start)

import concurrent.futures

# start = time.perf_counter()

# def do_something(num):
#     print("sleeping %d second(s)" % num)
#     time.sleep(num)
#     return "done sleeping"

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     results = [executor.submit(do_something, 5) for _ in range(50)]
    
#     for f in concurrent.futures.as_completed(results):
#         print(f.result())

# finish = time.perf_counter()

# print('finished in:', finish - start)

# start = time.perf_counter()

# def do_something(num):
#     print("sleeping %d second(s)" % num)
#     time.sleep(num)
#     return "done sleeping %d" % num

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     seconds = [5,4,3,2,1]
    
#     results = executor.map(do_something, seconds)
    
#     for result in results:
#         print(result)

# finish = time.perf_counter()

# print('finished in:', finish - start)

import multiprocessing

# def do_something(num):
#     print("sleeping %d second(s)" % num)
#     time.sleep(num)
#     print("done sleeping")

# if __name__ == '__main__':
#     start = time.perf_counter()
#     processes =[multiprocessing.Process(target=do_something, args=[5]) for _ in range(1000)]

#     for process in processes:
#         process.start()

#     for process in processes:
#         process.join()

#     finish = time.perf_counter()

#     print('finished in:', finish - start)

def do_something(num):
    print("sleeping %d second(s)" % num)
    time.sleep(num)
    print("done sleeping")

if __name__ == "__main__":

    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        for _ in range(100):
            executor.submit(do_something, 5)

    finish = time.perf_counter()

    print('finished in:', finish - start)
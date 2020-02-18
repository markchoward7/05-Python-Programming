import math, random, time

my_list = [i for i in range(10000000)]
#my_list2 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
my_list2 = [190, 191, 192, 193, 194, 195, 196, 197, 199, 200]
rand_list = [random.randint(1,1000) for _ in range (100)]

def binary_search(target, sorted_list):
    left = 0
    right = len(sorted_list) - 1
    count = 0
    while left <= right:
        count += 1
        mid = (right + left) // 2
        if target == sorted_list[mid]:
            print("Loops:", count)
            return mid
        elif target < sorted_list[mid]:
            right = mid - 1
        else:
            left = mid + 1
    print("Loops:", count)
    return -1

start_time = time.time()
print("Old checking for 200")
binary_search(200, my_list)
print("Old checking for 800")
binary_search(800, my_list)
print("Old checking for 1200")
binary_search(1200, my_list)
print("Elapsed time:", time.time() - start_time)

def new_binary_search(target, sorted_list):
    left = 0
    right = len(sorted_list) - 1
    count = 0
    while left <= right:
        count += 1
        if target >= sorted_list[left] + (sorted_list[right] - sorted_list[left]) * 0.666:
            mid = math.ceil(right - ((right - left) * 0.166))
        elif target <= sorted_list[left] + (sorted_list[right] - sorted_list[left]) * 0.333:
            mid = math.floor(left + ((right - left) * 0.166))
        else:
            mid = (right + left) // 2
        if target == sorted_list[mid]:
            print("Loops:", count)
            return mid
        elif target < sorted_list[mid]:
            right = mid - 1
        else:
            left = mid + 1
    print("Loops:", count)
    return -1

start_time = time.time()
print("New checking for 200")
new_binary_search(200, my_list)
print("New checking for 800")
new_binary_search(800, my_list)
print("New checking for 1200")
new_binary_search(1200, my_list)
print("Elapsed time:", time.time() - start_time)

start_time = time.time()
print("Old check list2 for 198")
binary_search(198, my_list2)
print("Old check list2 for 191")
binary_search(191, my_list2)
print("Old check list2 for 199")
binary_search(199, my_list2)
print("Old check list2 for 195")
binary_search(195, my_list2)
print("Elapsed time:", time.time() - start_time)

start_time = time.time()
print("New check list2 for 198")
new_binary_search(198, my_list2)
print("New check list2 for 191")
new_binary_search(191, my_list2)
print("New check list2 for 199")
new_binary_search(199, my_list2)
print("New check list2 for 195")
new_binary_search(195, my_list2)
print("Elapsed time:", time.time() - start_time)

start_time = time.time()
print("Old check rand_list for 250")
binary_search(250, rand_list)
print("Old check rand_list for 500")
binary_search(500, rand_list)
print("Old check rand_list for 750")
binary_search(750, rand_list)
print("Elapsed time:", time.time() - start_time)

start_time = time.time()
print("New check rand_list for 250")
new_binary_search(250, rand_list)
print("New check rand_list for 500")
new_binary_search(500, rand_list)
print("New check rand_list for 750")
new_binary_search(750, rand_list)
print("Elapsed time:", time.time() - start_time)
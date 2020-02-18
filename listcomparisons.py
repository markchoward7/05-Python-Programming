from linklist import DoublyLinkedList
import random, time

my_list = []
my_linked_list = DoublyLinkedList()
rand_num = []

for _ in range(10000000):
    rand_num.append(random.randint(1,100000000))

start_time = time.time()
for item in rand_num:
    my_list.append(item)
print("List append creation:", time.time() - start_time)

start_time = time.time()
for item in rand_num:
    my_linked_list.append(item)
print("Linked list append creation:", time.time() - start_time)

start_time = time.time()
my_list.reverse()
print("List reverse:", time.time() - start_time)

start_time = time.time()
my_linked_list.reverse()
print("Linked List reverse:", time.time() - start_time)

start_time = time.time()
my_list.copy()
print("List copy:", time.time() - start_time)

start_time = time.time()
my_linked_list.copy()
print("Linked list copy:", time.time() - start_time)

start_time = time.time()
my_list.append("find me")
print("List append 1 item:", time.time() - start_time)

start_time = time.time()
my_linked_list.append("find me")
print("Linked list append 1 item:", time.time() - start_time)

start_time = time.time()
my_list.index("find me")
print("List find last item:", time.time() - start_time)

start_time = time.time()
my_linked_list.find("find me")
print("Linked list find last item:", time.time() - start_time)

start_time = time.time()
my_list.insert(0, "find this")
print("List insert at beginning:", time.time() - start_time)

start_time = time.time()
my_linked_list.insert(0, "find this")
print("Linked list insert at beginning:", time.time() - start_time)

start_time = time.time()
my_list.index("find this")
print("List find first item:", time.time() - start_time)

start_time = time.time()
my_linked_list.find("find this")
print("Linked list find first item:", time.time() - start_time)

start_time = time.time()
my_list.pop()
print("List pop item:", time.time() - start_time)

start_time = time.time()
my_linked_list.pop()
print("Linked list pop item:", time.time() - start_time)
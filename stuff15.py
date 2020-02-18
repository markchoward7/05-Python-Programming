def reverse(my_list):
    new_list = []
    for i in range(len(my_list) - 1, -1, -1):
        new_list.append(my_list[i])
    return new_list
# O(n)
print(reverse([1,2,3,4,5]))

def power(x, n):
    if n == 0:
        return 1
    total = x
    for _ in range(1,n):
        total *= x
    return total
print(power(3,0))
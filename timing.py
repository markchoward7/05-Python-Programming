
problem_size = 1

def loop(num, count):
    while num > 0:
        num -= 1
        count += 1
    return count

for _ in range(5):
    count = 0
    problemSize = problem_size
    while problemSize > 0:
        count = loop(problemSize, count)
        problemSize -= 1
    print("%d\t%d" % (problem_size, count))
    problem_size += 1
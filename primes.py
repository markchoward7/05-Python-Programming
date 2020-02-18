import math, time

def prime_generator():
# generator to find primes, will keep finding primes as many times as __next__ is called
    # initalize and set primes list and first num to check
    primes = [2]
    num = 3
    while True:
        # check each number in the list of primes
        for prime in primes:
            # if the prime is greater than the sqrt of the number to check
            # the number must be prime, add it to the list and break
            if prime >= math.floor(math.sqrt(num)) + 1:
                primes.append(num)
                break
            # if the number can be divided by the prime, it isn't prime, break
            if num % prime == 0:
                break
        # increment the number to check by 2
        num += 2
        # yield the results
        yield primes

def prime_sieve(num):
# function to find primes, uses the sieve to set all factors of a number to not be prime
    # set up a list of Bools as True to start
    is_prime = [True for _ in range(num+1)]
    # set 0 and 1 to not prime
    is_prime[0] = False
    is_prime[1] = False
    # take all even numbers within the list and set them to not prime
    for i in range(4, num + 1, 2):
        is_prime[i] = False
    # initalize and set current number to 3
    current_num = 3
    # while loop to make sure the current_num squared is less than the maximum number to check
    while(current_num * current_num <= num):
        # if the current_num is prime
        if (is_prime[current_num] == True):
            # take all factors within the list and set them to not prime
            for i in range(current_num * 2, num + 1, current_num):
                is_prime[i] = False
        # increment the number to check by 2
        current_num += 2
    # return the results
    return([index for index, check in enumerate(is_prime) if check])  
        

def main():
# main function, calls the prime checks and times them
    start_time = time.time()
    gen = prime_generator()
    for _ in range(500000):
        primes = gen.__next__()
    end_time = time.time()
    generator_time = end_time - start_time
    start_time = time.time()
    primes2 = prime_sieve(1000000)
    end_time = time.time()
    # if the return results are the same, everything is good, print one of them out
    if primes == primes2:
        print(primes)
    else:
    # if not, print the differences so we can troubleshoot
        print(set(primes2) - set(primes))
        print(set(primes) - set(primes2))
    # print the time they take
    print("Generator time: ", generator_time)
    print("Sieve time: ", end_time - start_time)
# call main
main()
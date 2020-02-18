def program_1():

    def main():
        print("Enter a number")
        num = int(input())
        recurse(1, num)
    
    def recurse(start, num):
        if start <= num:
            print(start)
            recurse(start+1, num)
    main()

def program_2():

    def main():
        print("Enter the first number")
        num1 = int(input())
        print("Enter the second number")
        num2 = int(input())
        print(multiply(num1, num2))

    def multiply(num1, num2):
        if num2 > 1:
            return num1 + multiply(num1, num2 - 1)
        else:
            return num1
    main()

def program_3():

    def main():
        print("Enter a number")
        num = int(input())
        asterisks(1,num)
    
    def asterisks(start, num):
        print("*" * start)
        if start < num:
            asterisks(start+1, num)
    main()

def program_4():

    def main():
        my_list = [0,1,2,3,4,5,6,7,8,5]
        print(largest(my_list, 0, my_list[0]))

    def largest(my_list, index, current_largest):
        if index >= len(my_list):
            return current_largest
        else:
            if current_largest > my_list[index]:
                current_largest = largest(my_list, index+1, current_largest)
            else:
                current_largest = largest(my_list, index+1, my_list[index])
        return current_largest
    main()

def program_5():

    def main():
        my_list = [0,1,2,3,4,5,6,7,8]
        print(list_sum(my_list, 0))

    def list_sum(my_list, index):
        if index < len(my_list):
            return my_list[index] + list_sum(my_list, index+1)
        else:
            return 0
    main()

def program_6():

    def main():
        print("Enter a number")
        num = int(input())
        print(recurse(num))

    def recurse(num):
        if num > 0:
            return num + recurse(num-1)
        else:
            return 0
    main()

def program_7():

    def main():
        print("Enter the number to be raised")
        num = int(input())
        print("Enter the power to raise by")
        exp = int(input())
        print(exponent(num, exp))

    def exponent(num, exp):
        if exp > 1:
            return num * exponent(num, exp - 1)
        else:
            return num
    main()

def program_8():

    def main():
        print("Enter a value for m")
        m = int(input())
        print("Enter a value for n")
        n = int(input())
        print(ackermann(m, n))

    def ackermann(m, n):
        if m == 0:
            return n + 1
        if n == 0:
            return ackermann(m - 1, 1)
        return ackermann(m - 1, ackermann(m, n - 1))
    main()
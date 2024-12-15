import math

def reverse(num_in):
    range_of_num = len(str(num_in))
    copy_num = num_in
    reversed_num = 0
    for _ in range(range_of_num):
        digit = copy_num %10
        copy_num = int(copy_num/10)
        reversed_num = reversed_num*10+digit
    return reversed_num

def num_to_ls_prime(num):
    ls_prime = [False]*num
    for tmp in range(num):
        if (isPrime(tmp)):
            ls_prime[tmp] = True
    return ls_prime

def isPrime(num):
    if (num <= 1):
        return False
    for tmp in range(2,int(num**0.5)+1):
        if (num%tmp==0):
            return False
    return True

num_of_test = int(input())
for _ in range(num_of_test):
    number = int(input())

    ls_eimrp = []
    ls_prime = num_to_ls_prime(number)

    for tmp in range(10,number):
        reversed_num = reverse(tmp)

        if (tmp != reversed_num and ls_prime[tmp] and reversed_num < number and ls_prime[reversed_num]):
            ls_eimrp.append(tmp)
            ls_eimrp.append(reversed_num)
            ls_prime[tmp] = False
            ls_prime[reversed_num] = False

    result = " ".join(map(str,ls_eimrp))
    print(result)


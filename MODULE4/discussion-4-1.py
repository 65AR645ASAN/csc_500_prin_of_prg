def isPrime(number):
    # rule 1: number should be positive, and greater than 1.
    if number > 1:
        # iterate over a range from 2 to half the number.
        for i in range(2, number // 2):
            # rule 2: shouldn't have any positive divisor
            # other than 1 and itself.
            if (number % i) == 0:
                return False
        return True
    else:
        return False

if __name__ == '__main__':
    number = int(input("Enter number to check if it's prime: "))
    if isPrime(number):
        print("{} is a prime number".format(number))
    else:
        print("{} is not a prime number".format(number))


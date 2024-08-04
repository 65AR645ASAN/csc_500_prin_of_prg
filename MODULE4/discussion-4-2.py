def isPrime(number):
    # rule 1: number should be positive, and greater than 1.
    if number > 1:
        # iterate over a range from 2 to half the number.
        for i in range(2, number // 2 + 1):
            print(f"Iterator numeral inside the stated range: {i}")
            # rule 2: shouldn't have any positive divisor
            # other than 1 and itself.
            if (number % i) == 0:
                print(f"Inside if modulus check, and not prime "
                      f"- modulus ouput: {number % i} - remainder is '0'")
                return False
        return True
    else:
        return False


if __name__ == '__main__':
    while True:
        number = int(input("Enter number to check if it's prime: "))
        if isPrime(number):
            print("{} is a prime number".format(number))
            break
        else:
            print("{} is not a prime number. Please try again.".format(number))

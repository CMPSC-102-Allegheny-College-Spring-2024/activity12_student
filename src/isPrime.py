# Iterative program to check if a number is prime in Python

def is_prime(number: int) -> bool:
    """ Determine primality: return 0 and 1"""

    # TODO: Complete the first case; if the `number` is less than 2, then return `FALSE`

    # Iterate from 2 to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        # If the number is divisible 
        # by any value in the range, it's not prime

        # TODO: Complete the second case; if the number divided by the index has a remainder of zero, then return `FALSE`

    # If no divisors are found, the number is prime
    return True
# end of is_prime()

# Driver function of the program

def main()-> None:
    """ driver function"""
    # Example usage
    # user_input = int(input("\t Enter a number: "))
    # result = is_prime(user_input)

    myNumber = 101
    # TODO: create the variable `result` and set it equal to the function `is_prime()` with the variable `myNumber` as an argument.

    if result:
        print(f"\t {myNumber}: Prime number")
    else:
        print(f"\t {myNumber}: Not a prime number")
# end of main()
        
# TODO: call the function main() here to execute the program.

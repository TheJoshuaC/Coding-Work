# collatz conjecture method

print('\nThis program will apply Collatz Conjecture to any positive interger \n\n')
number = int(input('Please enter a positive integer: '))

def collatz(number):
    while number != 1:
        if number % 2 ==0:
            number //= 2
        else:
            number = 3 * number + 1
        print(number)

collatz(number)
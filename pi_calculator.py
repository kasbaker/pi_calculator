"""Calculate pi to N digits using Gauss-Legendre algorithm"""
from decimal import *

N = 10000     # max decimal points displayed
getcontext().prec = N

# starting values for algorithm
a_ = Decimal(1)
b_ = Decimal(2 ** (-.5))
t_ = Decimal(.25)
p_ = Decimal(1)


def gen_abtp(a, b, t, p):
    """Generates the next a, b, t, and p values in the algorithm"""
    a_next = (a + b)/2
    b_next = (a*b).sqrt()
    t_next = t - p*(a-a_next)**2
    p_next = 2*p
    yield a_next, b_next, t_next, p_next


def gen_pi(a, b, t, p, n):
    """Generates the next estimate of pi from the algorithm"""
    for x in range(n):
        yield ((a+b)**2)/(4*t)
        (a, b, t, p) = next(gen_abtp(a, b, t, p))


def calc_n_digits_pi(n):
    """Calculates pi to an accuracy of at least n digits and then returns the result"""
    max_error = Decimal(10) ** (-n)
    estimate = Decimal(1)
    for pi_gen in gen_pi(a_, b_, t_, p_, 100):
        if abs(estimate - pi_gen) < max_error:
            return pi_gen.quantize(max_error)
        else:
            estimate = pi_gen
            continue


def main():
    # calculate pi to this many digits
    print("\n"*100)
    print("Welcome to the pi calculator!")

    run = True
    while run:
        print("\nHow many digits of pi would you like to calculate?")
        # check if input is an integer
        try:
            digits = int(input("Input any integer between 1 and 10000: "))
        except ValueError:
            print("You must input an integer. Try again.")
            continue

        # check if number is within range
        if 0 < digits < 10001:
            input(f"\nOK calculating {digits} digits of pi!\n\n *** Press Enter to continue ***\n")
        else:
            print("That number is out of range. Try again.")
            continue

        # calculate pi
        pi = calc_n_digits_pi(digits-1)
        print(f"Pi is approximately: {pi}\n")

        user_input = None
        while user_input != 'y' and user_input != 'n':
            user_input = input("Would you like to calculate again? y/n ").lower()
            if user_input == 'y':
                print("\nYay pi!")
            elif user_input == 'n':
                print("\nGoodbye!")
                run = False
            else:
                print("Please input 'y' or 'n'. Try again.\n")


if __name__ == "__main__":
    main()
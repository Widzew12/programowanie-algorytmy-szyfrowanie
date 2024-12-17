# Python3 program to find multiplicative modulo
# inverse using Extended Euclid algorithm.

class MultiplicativeInverse:
    def __init__(self):
        self.x, self.y = 0, 1

# Global Variables
x, y = 0, 1

# Function for extended Euclidean Algorithm


def gcdExtended(self, a, b):
    # Base Case
    if (a == 0):
        self.x = 0
        self.y = 1
        return b

    # To store results of recursive call
    gcd = self.gcdExtended(b % a, a)
    x1 = self.x
    y1 = self.y

    # Update x and y using results of recursive call
    self.x = y1 - (b // a) * x1
    self.y = x1

    return gcd


def modInverse(A, M):
    multiplicative_inverse = MultiplicativeInverse()
    g = multplicative_inverse.gcdExtended(A, M)
    if (g != 1):
        print("Inverse doesn't exist")
        return None
    else:

        # m is added to handle negative x
        res = (x % M + M) % M
        print("Modular multiplicative inverse is ", res)
        return res


# Driver Code
if __name__ == "__main__":
    A = 3
    M = 11

    # Function call
    modInverse(A, M)
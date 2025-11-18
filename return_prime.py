import math
def return_prime(n):return n if n>1 and all(n%i for i in range(2,math.isqrt(n)+1)) else None
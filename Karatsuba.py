import math

def number_of_digits(n):
    return math.floor(math.log10(n) + 1)

def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y
    else:
        m = max(number_of_digits(x), number_of_digits(y))
        m2 = m // 2
        xl = x // 10 ** (m2)
        xr = x % 10 ** (m2)
        yl = y // 10 ** (m2)
        yr = y % 10 ** (m2)
        z0 = karatsuba(xr, yr)
        z1 = karatsuba((xl + xr), (yl + yr))
        z2 = karatsuba(xl, yl)
        return (z2 * 10 ** (2 * m2)) + ((z1 - z2 - z0) * 10 ** (m2)) + (z0)

print(karatsuba(1234, 5678))

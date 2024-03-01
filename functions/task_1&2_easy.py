import cmath


def solve_quadratic_equation(a, b, c):
    d = b**2 - 4 * a * c
    x1 = (-b + cmath.sqrt(d)) / (2 * a)
    x2 = (-b - cmath.sqrt(d)) / (2 * a)

    # Check if the imaginary part is 0 and if so, only print the real part
    if x1.imag == 0:
        x1 = x1.real
    if x2.imag == 0:
        x2 = x2.real

    print(f"x1 = {x1}")
    print(f"x2 = {x2}")


a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

solve_quadratic_equation(a, b, c)

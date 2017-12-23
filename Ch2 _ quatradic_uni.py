import sys, math, cmath

SQUARED = "\N{SUPERSCRIPT TWO}"
ARROW = "\N{RIGHTWARDS ARROW}"

if not sys.platform.startswith("linux"):
    SQUARED = "^2"
    ARROW = "->"


def get_float(msg, allow_zero):
    x = None
    while x is None:
        try:
            x = float(input(msg))
            if not allow_zero and abs(x) < sys.float_info.epsilon:
                print("cannot assign number 0")
                x = None
        except ValueError as err:
            print(err)
    return x

print("a\N{SUPERSCRIPT TWO} + bx + c = 0")
a = get_float("pick a: ", False)
b = get_float("pick b: ", True)
c = get_float("pick c: ", True)

x1 = None
x2 = None
discriminant = (b ** 2) - (4 * a * c)
if discriminant == 0:
    x1 = -(b / (2 * a))
else:
    if discriminant > 0:
        root = math.sqrt(discriminant)
    else:
        root = cmath.sqrt(discriminant)
    x1 = -(b + root) / (2 * a)
    x2 = -(b - root) / (2 * a)

equation = ("{0}x\N{SUPERSCRIPT TWO} + {1}x + {2} = 0"
            " \N{RIGHTWARDS ARROW}  x = {3}".format(a, b, c, x1))
if x2 is not None:
    equation += " or x = {0}".format(x2)
print(equation)

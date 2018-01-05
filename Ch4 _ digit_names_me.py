import sys


Language = "en"

ENGLISH = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
           5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
SLOVAK = {0: "nula", 1: "jedna", 2: "dva", 3: "tri", 4: "styri",
          5: "pat", 6: "sest", 7: "sedem", 8: "osem", 9: "devat"}


def main():
    if len(sys.argv) == 1 or sys.argv[1] in {"-h", "--help"}:
        print("usage: {0} [en|svk] number".format(sys.argv[0]))
        sys.exit()
    
    args = sys.argv[1:]
    if args[0] in {"en", "svk"}:
        global Language
        Language = args.pop(0)
    print_digits(args.pop(0))


def print_digits(digits):
    dictionary = ENGLISH if Language == "en" else SLOVAK
    for digit in digits:
        print(dictionary[int(digit)], end=" ")
    print()


main()

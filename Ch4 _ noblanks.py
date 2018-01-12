import sys, os


def main():
    if len(sys.argv) == 1 or sys.argv[1] in {"-h", "--help"}:
        print("usage: {0} file [file2 [..fileN]]".format(sys.argv[0]))
        sys.exit()

    for filename in sys.argv[1:]:
        lines = read_data(filename)
        if lines:
            write_data(lines, os.path.splitext(filename)[0] + ".nb")


def read_data(filename):
    lines = []
    fh = None
    try:
        fh =open(filename, encoding="utf8")
        for line in fh:
            if line.strip():
                lines.append(line)
    except EnvironmentError as err:
        print("ERROR: {0} could not be opened!: {1}".format(
                                             filename, err))
        return []
    else:
        print("Succesfully extracted data from {0}".format(filename))
    finally:
        if fh is not None:
            fh.close()
    return lines


def write_data(lines, filename):
    fh = None
    try:
        fh = open(filename, "w", encoding="utf8")
        for line in lines:
            fh.write(line)
    except EnvironmentError as err:
        print("ERROR: {0} could not be saved!: {1}".format(
                                             filename, err))
    else:
        print("Succesfully saved data to {0}".format(filename))
    finally:
        if fh is not None:
            fh.close()

main()

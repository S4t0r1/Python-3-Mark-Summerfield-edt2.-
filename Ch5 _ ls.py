import locale, os, argparse, datetime

locale.setlocale(locale.LC_ALL,"")


def main():
    counts = [0, 0]
    opts, paths = process_args()
    if not opts.recursive:
        filenames = []
        dirnames = []
        for path in paths:
            if os.path.isfile(path):
                filenames.append(path)
            for filename in os.listdir(path):
                if not opts.hidden and filename.startswith("."):
                    continue
                fullname = os.path.join(path, filename)
                if fullname.startswith("./"):
                    fullname = fullname[2:]
                if os.path.isfile(fullname):
                    filenames.append(fullname)
                else:
                    dirnames.append(fullname)
        counts[0] += len(filenames)
        counts[1] += len(dirnames)
        process_lists(opts, filenames, dirnames)
    else:
        for path in paths:
            for root, dirs, files in os.walk(path):
                if not opts.hidden:
                    dirs[:] = [dir for dir in dirs if not dir.startswith(".")]
                filenames = []
                for name in files:
                    if not opts.hidden and name.startswith("."):
                        continue
                    fullname = os.path.join(root, name)
                    if fullname.startswith("./"):
                        fullname = fullname[2:]
                    filenames.append(fullname)
                counts[0] += len(filenames)
                counts[1] += len(dirs)
                process_lists(opts, filenames, [])
    print_counts(counts)


def process_args():
    usage = """%prog [options] [path1 [path2 [..pathN]]]

Paths are optional. If none are given . is used."""
    
    parser = argparse.ArgumentParser(usage=usage)
    parser.add_argument("-H", "--hidden", dest="hidden",
                        action="store_true",
                        help=("show hidden items [default: off]"))
    parser.add_argument("-m", "--modified", dest="modified",
                        action="store_true",
                        help=("show modification date/time [default: off]"))
    orderlist = ["name", "n", "modified", "m", "size", "s"]
    parser.add_argument("-o", "--order", dest="order",
                        choices=orderlist,
                        help=("order by ({0}) [default: %default]".format(
                              ",".join(["'" + x + "'" for x in orderlist]))))
    parser.add_argument("-r", "--recursive", dest="recursive",
                        action="store_true",
                        help=("recursing to subdirectories [default: off]"))
    parser.add_argument("-s", "--sizes", dest="sizes",
                        action="store_true",
                        help=("show sizes [default: off]"))
    parser.set_defaults(order=orderlist[0])
    opts, args = parser.parse_args()
    if not args:
        args = ["."]
    return opts, args


def process_lists(opts, filenames, dirnames):
    keys_lines = []
    for name in filenames:
        modified = ""
        if opts.modified:
            try:
                modified = (datetime.datetime.fromtimestamp(os.path.getmtime(name))
                           .isoformat(" ")[:19] + " ")
            except EnvironmentError:
                print("{0:>19} ".format("unknown"))
        size = ""
        if opts.sizes:
            try:
                size = "{0:>15n} ".format(os.path.getsize(name))
            except EnvironmentError:
                print("{0:>15} ".format("unknown"))
        if os.path.islink(name):
            name += " -> " + os.path.realpath(name)
        if opts.order in {"modified", "m"}:
            orderkey = modified
        elif opts.order in {"size", "s"}:
            orderkey = modified
        else:
            orderkey = name
        keys_lines.append((orderkey, "{modified}{size}{name}".format(
                                                        **locals())))
    size = "" if not opts.sizes else " " * 15
    modified = "" if not opts.modified else " " * 20
    for name in sorted(dirnames):
        keys_lines.append((name, modified + size + name + "/"))
    for key, line in sorted(keys_lines):
        print(line)


def print_counts(counts):
    print("{0} file{1}, {2} director{3}".format(
          "{0:n}".format(counts[0]) if counts[0] else "no",
          "s" if counts[0] != 1 else "",
          "{0:n}".format(counts[1]) if counts[1] else "no",
          "ies" if counts[1] != 1 else "y"))


main()

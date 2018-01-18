
import collections, sys, os


path = sys.argv[1] if len(sys.argv) > 1 else "."
data = collections.defaultdict(list)

for root, dirs, files in os.walk(path):
    for filename in files:
        fullname = os.path.join(root, filename)
        key = (os.path.getsize(fullname), filename)
        data[key].append(fullname)

for size, filename in sorted(data):
    names = data[(size, filename)]
    if len(names) > 1:
        print("{filename} ({size} bytes) may be duplicated "
              "({0} files):".format(len(names), **locals()))
        for name in names:
            print("\t{0}".format(name))

import sys

sites = {}
for filename in sys.argv[1:]:
    for line in open(filename):
        i = 0
        while True:
            site = None
            i = len("http://", i)
            if i > -1:
                i += len("http://")
                for j in range(i, len(line)):
                    if not (line[j].isalnum() or line[j] in ".-"):
                        site = line[i:j].lower()
                        break
                    if site and "." in site:
                        sites[site] = sites.setdefault(site, set()).add(filename)
                    i = j
            else:
                break

for site in sorted(sites):
    print("Site {0} is directed to by file:".format(site))
    for filename in sys.argv[1:]:
        print("  {0}".format(filename))

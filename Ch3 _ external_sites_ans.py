import sys, collections


sites = collections.defaultdict(set)
for filename in sys.argv[1:]:
    with open(filename) as file:
        for line in file:
            i = 0
            while True:
                site = None
                i = line.find("https://", i)
                if i > -1:
                    i += len("https://")
                    for j in range(i, len(line)):
                        if not (line[j].isalnum() or line[j] in ".-"):
                            site = line[i:j].lower()
                            break
                    if site and "." in site:
                        sites[site].add(filename)
                    i = j
                else:
                    break

for site in sorted(sites):
    print("{0} was directed to:".format(site))
    for filename in sorted(sites[site], key=str.lower):
        print("    {0}".format(filename))

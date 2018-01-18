import sys, gzip, io, xml.etree.ElementTree


def main():
    if len(sys.argv) != 2 or sys.argv[1] in {"-h", "--help"}:
        print("usage: {0} filename".format(sys.argv[0]))
        sys.exit(2)
    
    filename = sys.argv[1]
    binary = gzip.open(filename).read()
    fh = io.StringIO(binary.decode("utf8"))
    
    tree = xml.etree.ElementTree.ElementTree()
    root = tree.parse(fh)
    stations = []
    for element in tree.getiterator("station_name"):
        stations.append(element.text)


main()

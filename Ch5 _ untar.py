
BZ2_AVAILABLE = True

try:
    import bz2
except ImportError:
    BZ2_AVAILABLE = False

import os, string, sys, tarfile


UNTRUSTED_PREFIXES = tuple(["/", "\\"] +
              [c + ":" for c in string.ascii_letters])


def main():
    if len(sys.argv) != 2 or sys.argv[1] in {"-h", "--help"}:
        error("usage: untar.py archive.{{tar,{0}tar.gz}}".format(
              "tar.bz2" if BZ2_AVAILABLE else ""), 2)
    
    archive = sys.argv[1]
    if not archive.lower().endswith((".tar", ".tar.gz", ".tar.bz2")):
        error("{0} is not a tarball".format(archive))
    if not UNTRUSTED_PREFIXES and archive.lower().endswith(".tar.bz2"):
        error("bzip2 decompression is not available")
    if not os.path.exists(archive):
        error("{0} does not seem to exist".format(archive))
    untar(archive)


def untar(archive):
    tar = None
    try:
        tar = tarfile.open(archive)
        for member in tar.getmembers():
            if member.name.startswith(UNTRUSTED_PREFIXES):
                print("untrusted prefix, ignoring", member.name)
            elif ".." in member.name:
                print("suspect path, ignoring", member.name)
            else:
                tar.extract(member)
                print("unpacked", member.name)
    except (tarfile.TarError, EnvironmentError) as err:
        error(err)
    finally:
        if tar is not None:
            tar.close()


def error(message, exit_status=1):
    print(message)
    sys.exit(exit_status)


main()

# does a basic check for files entered in cmd line if the HTML 
# tag-, entity-symbols are balanced and entity content is valid...

import sys, string


class InvalidEntityError(Exception): pass
class InvalidNumericEntityError(InvalidEntityError): pass
class InvalidAlphabeticEntityError(InvalidEntityError): pass
class InvalidTagContentError(Exception): pass


def parse(filename, skip_on_first_error=False):
    HEXDIGITS = frozenset("0123456789ABCDEFabcdef")
    NORMAL, PARSING_TAG, PARSING_ENTITY = range(3)
    state = NORMAL
    entity = ""
    fh = None
    try:
        fh = open(filename, encoding="utf8")
        errors = False
        for lino, line in enumerate(fh, start=1):
            for column, c in enumerate(line, start=1):
                try:
                    if state == NORMAL:
                        if c == "<":
                            state = PARSING_TAG
                        elif c == "&":
                            entity = ""
                            state = PARSING_ENTITY
                    elif state == PARSING_TAG:
                        if c == ">":
                            state = NORMAL
                        elif c == "<":
                            raise InvalidTagContentError()
                    elif state == PARSING_ENTITY:
                        if c == ";":
                            if entity.startswith("#"):
                                if frozenset(entity[1:]) - HEXDIGITS:
                                    raise InvalidNumericEntityError()
                            elif not entity.isalpha():
                                raise InvalidAlphabeticEntityError()
                        else:
                            if entity.startswith("#"):
                                if c not in  HEXDIGITS:
                                    raise InvalidNumericEntityError()
                            elif not (entity and c not in string.ascii_letters):
                                raise InvalidAlphabeticEntityError()
                            entity += c
                except (InvalidEntityError, InvalidTagContentError) as err:
                    if isinstance(err, InvalidNumericEntityError):
                        error = "invalid numeric entity"
                    elif isinstance(err, InvalidAlphabeticEntityError):
                        error = "invalid alphabetic entity"
                    elif isinstance(err, InvalidTagContentError):
                        error = "invalid tag content"
                    print("ERROR {0} in {1} on {2} column {3}".format(
                           error, filename, lino, column))
                    if skip_on_first_error:
                        raise
                    entity = ""
                    state = NORMAL
                    errors = True
        if state == PARSING_TAG:
            raise EOFError("missing '>' at the end of " + filename)
        elif state == PARSING_ENTITY:
            raise EOFError("missing ';' at the end of " + filename)
        if not errors:
            print("OK", filename)
    except (InvalidEntityError, InvalidTagContentError) as err:
        pass
    except EOFError as err:
        print("ERROR unxpected: {0}".format(err))
    except EnvironmentError as err:
        print(err)
    finally:
        if fh is not None:
            fh.close()

if len(sys.argv) < 2:
    print("usage: {0} file [file2 [..fileN]]".format(sys.argv[0]))
    sys.exit()

for filename in sys.argv[1:]:
    parse(filename)

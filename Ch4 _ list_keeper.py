import os


YES = frozenset({"y", "Y", "yes", "Yes", "YES"})


def main():
    dirty = False
    items = []
    
    filename, items = choose_file()
    if not filename:
        print("Cancelled")
        return
    
    while True:
        print("\nList Keeper\n")
        print_list(items)
        option = get_option(items, dirty)
        if option in "Aa":
            dirty = add_item(items, dirty)
        elif option in "Dd":
            dirty = delete_item(items, dirty)
        elif option in "Ss":
            dirty = save_list(filename, items)
        elif option in "Qq":
            if (dirty and (get_string("Save unsaved changes (y/n)?", 
                                      "yes/no", "y") in YES)):
                save_list(filename, items, True)
            break


def choose_file():
    enter_filename = False
    print("\nList Keeper\n")
    files = [x for x in os.listdir(".") if x.endswith(".lst")]
    if not files:
        enter_filename = True
    if not enter_filename:
        print_list(files)
        index = get_integer("Choose a file with number (or 0 to create new)",
                            "number", minimum=1, maximum=len(files), 
                             allow_zero=True)
        if index == 0:
            enter_filename = True
        else:
            filename = files[index - 1]
            items = load_list(filename)
    if enter_filename:
        filename = get_string("Choose a filename", "filename")
        if not filename.endswith(".lst"):
            filename += ".lst"
    return filename, items


def print_list(items):
    if not items:
        print("--the list is empty--")
    else:
        width = 1 if len(items) < 10 else 2 if len(items) < 100 else 3
        for i, items in enumerate(items):
            print("{0:{width}}: {item}".format(i + 1, **locals()))
    print()


def get_option(items, dirty):
    while True:
        if items:
            if dirty:
                menu = "[A]dd [D]elete [S]ave [Q]uit"
                valid_options = "AaDdSsQq"
            else:
                menu = "[A]dd [D]elete [Q]uit"
                valid_options = "AaDdQq"
        else:
            menu = "[A]dd [Q]uit"
            valid_options = "AaQq"
        option = get_string(menu, "choice", "a")
        if option not in valid_options:
            print("ERROR: invalid option--enter on of {0}".format(
                                                    valid_options))
            input("Press Enter to continue...")
        else:
            return option


def add_item(items, dirty):
    item = get_string("Add item", "item")
    if item:
        items.append(item)
        items.sort(key=str.lower)
        return True
    else:
        return dirty


def delete_item(items, dirty):
    index = get_integer("Delete item number (or 0 to abort)",
                        "number", maximum=len(items), allow_zero=True)
    if index != 0:
        del items[index - 1]
        return True
    else:
        return dirty


def load_list(filename):
    items = []
    fh = None
    try:
        for line in open(filename, encoding="utf8"):
            items.append(line.rstrip())
    except EnvironmentError as err:
        print("ERROR: {0} could not be loaded: {1}".format(filename, err))
        return []
    finally:
        if fh is not None:
            fh.close()
    return items


def save_list(filename, items, terminate=False):
    fh = None
    try:
        fh = open(filename, "w", encoding="utf8")
        fh.write("\n".join(items))
        fh.write("\n")
    except EnvironmentError as err:
        print("ERROR: {0} could not be saved: {1}".format(filename, err))
        return True
    else:
        print("{0} item{1} saved into {2}".format(len(items),
                 ("s" if len(items) != 1 else ""), filename))
        if not terminate:
            input("Press ENTER to continue")
        return False
    finally:
        if fh is not None:
            fh.close()


def get_string(message, name="string", default=None, 
               minimum_length=0, maximum_length=80):
    message += ": " if default is None else "[{0}]".format(default)
    while True:
        try:
            line = input(message)
            if not line:
                if default is not None:
                    return default
                if minimum_length == 0:
                    return ""
                else:
                    raise ValueError("{0} may not be empty".format(name))
            if not (minimum_length <= len(line) <= maximum_length):
                raise ValueError("{name} must be between {minimum_length} "
                                 "and {maximum_length} characters".format(**locals()))
            return line
        except ValueError as err:
            print("ERROR", err)


def get_integer(message, name="number", default=None, 
               minimum=0, maximum=100, allow_zero=True):
    message += ": " if default is None else "[{0}]".format(default)
    
    class RangeError(Exception): pass
    
    while True:
        try:
            line = input(message)
            if not line and default is not None:
                return default
            i = int(line)    
            if i == 0:
                if allow_zero:
                    return i
                else:
                    raise RangeError("{0} may not be empty".format(name))
            if not (minimum <= i <= maximum):
                raise RangeError("{name} must be between {minimum} "
                                 "and {maximum} inclusive {0}".format(
                                 "(or 0)" if allow_zero else "", **locals()))
            return i
        except RangeError as err:
            print("ERROR", err)
        except ValueError as err:
            print("ERROR: {name} has to be an integer".format(**locals()))


main()

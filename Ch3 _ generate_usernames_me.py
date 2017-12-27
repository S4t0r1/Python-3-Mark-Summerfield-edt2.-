import sys, collections

ID, FORENAME, MIDDLENAME, SURNAME, DEPARTMENT = range(5)
User = collections.namedtuple("User",
            "username forename middlename surname id")


def main():
    usernames = set()
    users = {}
    with open("users.txt", encoding="utf8") as file:
        for line in file:
            line = line.rstrip()
            if line:
                user = process_line(line, usernames)
                users[(user.surname.lower(), user.forename.lower(),
                       user.id)] = user
    print_users(users)


def process_line(line, usernames):
    fields = line.split(":")
    username = generate_username(fields, usernames)
    user = User(username, fields[FORENAME], fields[MIDDLENAME],
                fields[SURNAME], fields[ID])
    return user


def generate_username(fields, usernames):
    username = ((fields[FORENAME][0] + fields[MIDDLENAME][:1] +
                 fields[SURNAME]).replace("-", "").replace("'", ""))
    username = original_name = username[:8].lower()
    count = 1
    while username in usernames:
        username = "{0}{1}".format(original_name, count)
        count += 1
    usernames.add(username)
    return username


def print_users(users):
    with open("userslist.txt", 'w', encoding="utf8") as output:
        namewidth = 32
        usernamewidth = 9
        
        output.write("{0:<{nw}} {1:^6} {2:{uw}}\n".format(
                     "Name", "ID", "Username", nw=namewidth, uw=usernamewidth))
        output.write("{0:-<{nw}} {0:-<6} {0:-<{uw}}\n".format("", 
                      nw=namewidth, uw=usernamewidth))
    
        for key in sorted(users):
            user = users[key]
            initial = ""
            if user.middlename:
                initial = " " + user.middlename[0]
            name = "{0.surname}, {0.forename}{1}".format(user, initial)
            output.write("{0:.<{nw}} ({1.id:4}) {1.username:{uw}}\n".format(
                          name, user, nw=namewidth, uw=usernamewidth))


main()

import random


def get_forenames_and_surnames():
    forenames = []
    surnames = []
    for names, filename in ((forenames, "forenames.txt"),
                             (surnames, "surnames.txt")):
        for name in open(filename):
            names.append(name.rstrip())
    return forenames, surnames

forenames, surnames = get_forenames_and_surnames()
fh = open("testnames1.txt", "w", encoding="utf8")

for i in range(100):
    line = "{0} {1}\n".format(random.choice(forenames),
                             random.choice(surnames))
    fh.write(line)


#===============================================================================


import random


def get_forenames_and_surnames():
    forenames = []
    surnames = []
    for names, filename in ((forenames, "forenames.txt"),
                             (surnames, "surnames.txt")):
        for name in open(filename):
            names.append(name.rstrip())
    return forenames, surnames

forenames, surnames = get_forenames_and_surnames()
fh = open("testnames2.txt", "w", encoding="utf8")

limit = 100
years = list(range(1970, 2012)) * 3
for year, forename, surname in zip(random.sample(years, limit),
                               random.sample(forenames, limit), 
                               random.sample(surnames, limit)):
    new_name = "{0} {1}".format(forename, surname)
    fh.write("{0:.<25}.{1}\n".format(new_name, year))

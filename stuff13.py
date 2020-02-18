import keyword, re

def program_1():
    strings = """ bat bit but hat hit hut """

    pattern = re.compile(r"(b|h)+(a|i|u)+t")

    for match in pattern.finditer(strings):
        print(match)

def program_2():
    names = """
    first last
    firstagain lastagain
    """

    pattern = re.compile(r"[a-zA-Z]+ [a-zA-Z]+")

    for match in pattern.finditer(names):
        print(match)

def program_3():
    names = """
    first, m
    firstagain, n
    """

    pattern = re.compile(r"[a-zA-Z]+, [a-zA-Z]")

    for match in pattern.finditer(names):
        print(match)

def program_4():
    identifiers = """
valid_example
valid_example2
validexample3
valid4example
validExample5
ValidExample6
_valid_example7
validexample8_
v
@invalidexample
2invalidexample
False
class
    """

    pattern = re.compile(r"(^[a-zA-Z_]\w*)", re.MULTILINE)

    for match in pattern.finditer(identifiers):
        if match.groups()[0] not in keyword.kwlist:
            print(match)

def program_5():
    addresses = """
    1180 Bordeaux Drive
    3120 De la Cruz Boulevard
    """

    pattern = re.compile(r"[0-9]+[a-zA-Z ]+[a-zA-Z]+")

    for match in pattern.finditer(addresses):
        print(match)

def program_6():
    urls = """
    www.google.com
    www.whitehouse.gov
    www.reddit.com
    """

    pattern = re.compile(r"www\.[a-z0-9.]+\.+[a-z]+")
    
    for match in pattern.finditer(urls):
        print(match)

def program_7():
    emails = """
    first.last@domain.com
    first.last@domain.edu
    first.last@us.af.mil
    first-last@do-main.com
    first.last69420@domain.com
    dontcatchthis
    dont@catchthis
    """

    pattern = re.compile(r"[a-zA-Z0-9-.]+@[a-zA-Z.-]+(\.[a-z]+)$", re.MULTILINE)

    for match in pattern.finditer(emails):
        print(match)

def program_8():
    urls = """
    www.google.com
    www.whitehouse.gov
    www.reddit.com/r/birdsarentreal
    old.reddit.com
    https://my.af.mil
    dontcatchthis
    """

    pattern = re.compile(r"(http(s)?://)?(www\.)?[a-z0-9.-]+\.[a-z/]+")
    
    for match in pattern.finditer(urls):
        print(match)

def program_9():

    def extract_type(variable):
        type_string = str(type(variable))
        pattern = re.compile(r"'([a-z_]+)'")

        return re.search(pattern, type_string).group(1)

    def main():
        variable1 = 5
        variable2 = 5.
        variable3 = 's'
        variable4 = (5,'s')
        variable5 = set([5, 's'])
        variable6 = {5 : 's'}
        variable7 = [5, 's']

        print(extract_type(variable1))
        print(extract_type(variable2))
        print(extract_type(variable3))
        print(extract_type(variable4))
        print(extract_type(variable5))
        print(extract_type(variable6))
        print(extract_type(variable7))
        print(extract_type(main))
        print(extract_type(object))
    main()

def program_10():

    months = """
    01
    02
    03
    04
    05
    06
    07
    08
    09
    10
    11
    12
    13
    21
    """

    pattern = re.compile(r"(0[1-9]|1[0-2])")

    for match in pattern.finditer(months):
        print(match)
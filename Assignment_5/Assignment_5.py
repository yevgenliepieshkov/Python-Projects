# ----------------Method implementations--------------------
MAX_LEN = 1500
MIN_LEN = 4


def get_key_character():

    char = None

    while char is None:

        char = input("Please enter a SINGLE character to act as key: ")

        if len(char) != 1:
            char = None
            continue
        else:
            break

    return char


def get_string():

    sentence = None

    while sentence is None:

        sentence = input("Please enter a phrase or sentence >= {0}"
                         " and <= {1} characters: ".format(MIN_LEN, MAX_LEN))

        if (len(sentence) >= MIN_LEN) and (len(sentence) <= MAX_LEN):
            continue
        else:
            sentence = None

    return sentence


def mask_character(a, b):

    new_string = "'"

    for char in range(len(b)):

        if b[char] == a:
            new_string += "*"
        else:
            new_string += b[char]

    new_string += "'"

    return new_string


def remove_character(a, b):

    new_string = "'"

    for char in range(len(b)):

        if b[char] != a:
            new_string += b[char]

    new_string += "'"

    return new_string


def count_key(a, b):

    counter = 0

    for char in range(len(b)):

        if b[char] == a:
            counter += 1

    return counter


# ----------------------Main ---------------------------

my_key = get_key_character()
my_string = get_string()

print("\nString with key character, '{}', masked:\n   ".format(my_key),
      mask_character(my_key, my_string),

      "\n\nString with '{}' removed:\n   ".format(my_key),
      remove_character(my_key, my_string),

      "\n\n# of occurrences of key character,"
      "'{0}': {1}".format(my_key,count_key(my_key,my_string)))

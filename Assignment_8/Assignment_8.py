# intended constants
MAX_SIZE = 20
ILLEGAL_INPUT_MESSAGE = \
    "** this is neither a QUIT request nor a legal student # ***"

# define and initialize the array in one comprehension
student = ["undefined" for k in range(MAX_SIZE)]

print("\nThe students before editing ----------------\n\n" + str(student))

while True:
    # get string from user
    user_choice = input("\nChoose a student to edit\n"
                        "from 0 to " + str(MAX_SIZE - 1) + "\n"
                                                           " ('q', 'Quit', etc to end program): ")

    # allow any word that starts with a q/Q to end the program
    if (user_choice[0].upper() == "Q"):
        break

    # extract the index as a number and see if it's in range
    if not user_choice.isdigit():
        print("\n" + ILLEGAL_INPUT_MESSAGE)
        continue
    else:
        index = int(user_choice)
    print("user choice:  " + str(index))
    if (not (0 <= index < MAX_SIZE)):
        print("\n" + ILLEGAL_INPUT_MESSAGE)
        continue

    # we have a legal index.  show old name for student and get new one
    new_name = \
        input("\nEditing student #{}: '{}.'  New name: ".
              format(index, student[index]))
    student[index] = new_name

# print the edited array
print("\nThe students after editing ----------------\n")
for k in range(MAX_SIZE):
    print("stud #" + str(k) + " = " + student[k])



    MAX_SIZE = 20
    EMPTY_ENTRY_MESSAGE = \
        "** Nothing entered ***"
    ILLEGAL_ENTRY_MESSAGE = \
        "** Non-ineger or non-quit entered ***"
    OUT_OF_RANGE_MESSAGE = \
        "** Integer not within acceptable bounds ***"

    # define and initialize the array in one comprehension
    student = ["undefined" for k in range(MAX_SIZE)]

    print("\nThe students before editing ----------------\n\n" + str(student))

    while True:
        # get string from user
        user_choice = input("\nChoose a student to edit\n"
                            "from 0 to " + str(MAX_SIZE - 1) + "\n"
                                                               " ('q', 'Quit', etc to end program): ")

        # allow any word that starts with a q/Q to end the program
        try:
            if (user_choice[0].upper() == "Q"):
                break
        except IndexError:
            print("\n" + EMPTY_ENTRY_MESSAGE)
            continue

            # extract the index as a number and see if it's in range
        try:
            index = int(user_choice)
        except ValueError:
            print("\n" + ILLEGAL_ENTRY_MESSAGE)
            continue

        if (not (0 <= index < MAX_SIZE)):
            print("\n" + OUT_OF_RANGE_MESSAGE)
            continue

        # we have a legal index.  show old name for student and get new one
        print("user choice:  " + str(index))
        new_name = \
            input("\nEditing student #{}: '{}.'  New name: ".
                  format(index, student[index]))
        student[index] = new_name

    # print the edited array
    print("\nThe students after editing ----------------\n")
    for k in range(MAX_SIZE):
        print("stud #" + str(k) + " = " + student[k])

    """ ----------------------- RUN --------------------
    The students before editing ----------------

    ['undefined', 'undefined', 'undefined', 'undefined', 'undefined', 'undefined', 'undefined', 'undefined', 'undefined', 'undefined', 'undefined', 'undefined', 'undefined', 'undefined', 'undefined', 'undefined', 'undefined', 'undefined', 'undefined', 'undefined']

    Choose a student to edit
    from 0 to 19
     ('q', 'Quit', etc to end program): 

    ** Non-ineger or non-quit entered ***

    Choose a student to edit
    from 0 to 19
     ('q', 'Quit', etc to end program): hflkjgh

    ** Non-ineger or non-quit entered ***

    Choose a student to edit
    from 0 to 19
     ('q', 'Quit', etc to end program): 2222

    ** Integer not within acceptable bounds ***

    Choose a student to edit
    from 0 to 19
     ('q', 'Quit', etc to end program): -3

    ** Integer not within acceptable bounds ***

    Choose a student to edit
    from 0 to 19
     ('q', 'Quit', etc to end program): 3
    user choice:  3

    Editing student #3: 'undefined.'  New name: three three three

    Choose a student to edit
    from 0 to 19
     ('q', 'Quit', etc to end program): 5
    user choice:  5

    Editing student #5: 'undefined.'  New name: five five five

    Choose a student to edit
    from 0 to 19
     ('q', 'Quit', etc to end program): 5
    user choice:  5

    Editing student #5: 'five five five.'  New name: FIVE five

    Choose a student to edit
    from 0 to 19
     ('q', 'Quit', etc to end program): quit already

    The students after editing ----------------

    stud #0 = undefined
    stud #1 = undefined
    stud #2 = undefined
    stud #3 = three three three
    stud #4 = undefined
    stud #5 = FIVE five
    stud #6 = undefined
    stud #7 = undefined
    stud #8 = undefined
    stud #9 = undefined
    stud #10 = undefined
    stud #11 = undefined
    stud #12 = undefined
    stud #13 = undefined
    stud #14 = undefined
    stud #15 = undefined
    stud #16 = undefined
    stud #17 = undefined
    stud #18 = undefined
    stud #19 = undefined

    ------------------------------------------------------- """

while True:
    try:
        # get string from user
        user_choice = input("\nChoose a student to edit\n"
                            "from 0 to " + str(MAX_SIZE - 1) + "\n"
                                                               " ('q', 'Quit', etc to end program): ")

        # allow any word that starts with a q/Q to end the program
        if (user_choice[0].upper() == "Q"):
            break

        # extract the index as a number and see if it's in range
        index = int(user_choice)

        if (not (0 <= index < MAX_SIZE)):
            print("\n" + OUT_OF_RANGE_MESSAGE)
            continue

        # we have a legal index.  show old name for student and get new one
        print("user choice:  " + str(index))
        new_name = \
            input("\nEditing student #{}: '{}.'  New name: ".
                  format(index, student[index]))
        student[index] = new_name

    # catch all possible exceptions
    except IndexError:
        print("\n" + EMPTY_ENTRY_MESSAGE)
        continue
    except ValueError:
        print("\n" + ILLEGAL_ENTRY_MESSAGE)
        continue

    # intended constants
MAX_SIZE = 20
EMPTY_ENTRY_MESSAGE = \
    "** Nothing entered ***"
ILLEGAL_ENTRY_MESSAGE = \
    "** Non-ineger or non-quit entered ***"
OUT_OF_RANGE_MESSAGE = \
    "** Integer not within acceptable bounds ***"

# define and initialize the array in one comprehension
student = ["undefined" for k in range(MAX_SIZE)]

print("\nThe students before editing ----------------\n\n" + str(student))

while True:
    try:
        # get string from user
        user_choice = input("\nChoose a student to edit\n"
                            "from 0 to " + str(MAX_SIZE - 1) + "\n"
                                                               " ('q', 'Quit', etc to end program): ")

        # allow any word that starts with a q/Q to end the program
        if (user_choice[0].upper() == "Q"):
            break

        # extract the index as a number and see if it's in range
        index = int(user_choice)

        if (not (0 <= index < MAX_SIZE)):
            print("\n" + OUT_OF_RANGE_MESSAGE)
            continue

        # we have a legal index.  show old name for student and get new one
        print("user choice:  " + str(index))
        new_name = \
            input("\nEditing student #{}: '{}.'  New name: ".
                  format(index, student[index]))
        student[index] = new_name

    # catch all possible exceptions
    except IndexError:
        print("\n" + EMPTY_ENTRY_MESSAGE)
        continue
    except ValueError:
        print("\n" + ILLEGAL_ENTRY_MESSAGE)
        continue

# print the edited array
print("\nThe students after editing ----------------\n")
for k in range(MAX_SIZE):
    print("stud #" + str(k) + " = " + student[k])

""" ----------------------- RUN --------------------
The students before editing ----------------

['undefined', 'undefined', 'undefined', 'undefined', 'undefined', 'undefined', 'undefined', 'undefined', 'undefined', 'undefined', 'undefined', 'undefined', 'undefined', 'undefined', 'undefined', 'undefined', 'undefined', 'undefined', 'undefined', 'undefined']

Choose a student to edit
from 0 to 19
 ('q', 'Quit', etc to end program): 

** Nothing entered ***

Choose a student to edit
from 0 to 19
 ('q', 'Quit', etc to end program): rtrtg

** Non-ineger or non-quit entered ***

Choose a student to edit
from 0 to 19
 ('q', 'Quit', etc to end program): 4444

** Integer not within acceptable bounds ***

Choose a student to edit
from 0 to 19
 ('q', 'Quit', etc to end program): 3
user choice:  3

Editing student #3: 'undefined.'  New name: three three three three

Choose a student to edit
from 0 to 19
 ('q', 'Quit', etc to end program): 5
user choice:  5

Editing student #5: 'undefined.'  New name: five

Choose a student to edit
from 0 to 19
 ('q', 'Quit', etc to end program): 5
user choice:  5

Editing student #5: 'five.'  New name: fiive FIVE FIVE five five

Choose a student to edit
from 0 to 19
 ('q', 'Quit', etc to end program): quit now

The students after editing ----------------

stud #0 = undefined
stud #1 = undefined
stud #2 = undefined
stud #3 = three three three three
stud #4 = undefined
stud #5 = fiive FIVE FIVE five five
stud #6 = undefined
stud #7 = undefined
stud #8 = undefined
stud #9 = undefined
stud #10 = undefined
stud #11 = undefined
stud #12 = undefined
stud #13 = undefined
stud #14 = undefined
stud #15 = undefined
stud #16 = undefined
stud #17 = undefined
stud #18 = undefined
stud #19 = undefined

------------------------------------------------------- """


def float_largest_to_top(data, array_size):
    changed = False

    # notice we stop at array_size-2 because of expr. k+1 in loop
    for k in range(array_size - 1):
        if (data[k] > data[k + 1]):
            data[k], data[k + 1] = data[k + 1], data[k]
            changed = True;
    return changed


def print_array(data, array_size,
                optional_title="--- The Array -----------:\n"):
    ITEMS_PER_LINE = 5
    print(optional_title)

    # new line every ITEMS_PER_LINE items, commas between
    for k in range(array_size):
        if (k % ITEMS_PER_LINE == 0):
            print()
        else:
            print(", ", end='')
        print(data[k], end='')


# client --------------------------------------------
my_array = [10.2, 56.9, -33, 12, 0, 2, 4.8, 199.9, 73, -91.2]
array_size = len(my_array)

float_largest_to_top(my_array, array_size)
print_array(my_array, array_size, "Testing Flt Lgst to Top")

""" --------------------------- RUN ---------------------------
Testing Flt Lgst to Top

10.2, -33, 12, 0, 2
4.8, 56.9, 73, -91.2, 199.9
------------------------------------------------------------ """
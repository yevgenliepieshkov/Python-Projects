# ---------------- SOURCE ----------------------------------------
class TripleString:
    """ encapsulates a 3-string object """

    # intended class constants ------------------------------------
    MIN_LEN = 1

    MAX_LEN = 50

    DEFAULT_STRING = "(undefined)"

    # constructor method ------------------------------------
    def __init__(self,
                 string1=DEFAULT_STRING, string2=DEFAULT_STRING,
                 string3=DEFAULT_STRING):
            if not self.set_string1(string1):
                self.string1 = TripleString.DEFAULT_STRING
            if not self.set_string2(string2):
                self.string2 = TripleString.DEFAULT_STRING
            if not self.set_string3(string3):
                self.string3 = TripleString.DEFAULT_STRING

    # mutator ("set") methods -------------------------------
    def set_string1(self, string):
        if not self.valid_string(string):
            return False
        self.string1 = string
        return True

    def set_string2(self, string):
        if not self.valid_string(string):
            return False
        self.string2 = string
        return True

    def set_string3(self, string):
        if not self.valid_string(string):
            return False
        self.string3 = string
        return True

    # accessor ("get") methods -------------------------------
    def get_string1(self):
        return self.string1

    def get_string2(self):
        return self.string2

    def get_string3(self):
        return self.string3

    # helper methods for entire class -----------------
    def valid_string(self, string):
        if len(string) < TripleString.MIN_LEN \
                or len(string) > TripleString.MAX_LEN:
            return False
        return True

    def to_string(self):
        string = "String 1: {}, String 2: {}, String 3: {}\n"\
            .format(self.get_string1(), self.get_string2(), self.get_string3())
        return string

# ------------- CLIENT --------------------------------------------------

# Create 6 TripleString objects


triple_string_num_1 = TripleString("hello", "h", "")
triple_string_num_2 = TripleString("-1", "omg", "let's do it")
triple_string_num_3 = TripleString("", "Nooo", "Hi")
triple_string_num_4 = TripleString("", "", "")
triple_string_num_5 = TripleString("Good morning", " it's me", "the third triple string")
triple_string_num_6 = TripleString("NO way", "", "where is the second string")

print(triple_string_num_1.to_string() + triple_string_num_2.to_string()
      + triple_string_num_3.to_string() + triple_string_num_4.to_string()
      + triple_string_num_5.to_string() + triple_string_num_6.to_string())

triple_string_num_1.set_string3("bye")
triple_string_num_2.set_string1("+2")
triple_string_num_3.set_string2("Yees")
triple_string_num_4.set_string1("1")
triple_string_num_4.set_string2("2")
triple_string_num_4.set_string3("3")
triple_string_num_5.set_string2("It's not me")
triple_string_num_6.set_string2("here I am")

print("{}{}{}{}{}{}".format(triple_string_num_1.to_string(), triple_string_num_2.to_string(),
                            triple_string_num_3.to_string(), triple_string_num_4.to_string(),
                            triple_string_num_5.to_string(), triple_string_num_6.to_string()))

string = ""

if triple_string_num_3.set_string1(string):
    print("Successfully set string1  to: " + "\"" + string + "\"")
else:
    print("Setting: " + "\"" + string + "\" as a string1 was not successful")

string = "Now I am a good string that will pass all filters"

if triple_string_num_4.set_string2(string):
    print("Successfully set string2 to: " + "\"" + string + "\"")
else:
    print("Setting: " + "\"" + string + "\" as a string2 was not successful")

string = "Now I am a bad string that will not pass all filters"

if triple_string_num_5.set_string3(string):
    print("Successfully set string2 to: " + "\"" + string + "\"")
else:
    print("Setting: " + "\"" + string + "\" as a string2 was not successful")


print("\nHere is string1 from object triple_string_num_3: "
      + triple_string_num_3.get_string1() + "\n"
      "Here is string2 from object triple_string_num_4: "
      + triple_string_num_4.get_string2() + "\n"
      "Here is string3 from object triple_string_num_5: "
      + triple_string_num_5.get_string3() + "\n")




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
        if len(string) < TripleString.MIN_LEN or len(string) > TripleString.MAX_LEN:
            return False
        return True

    def to_string(self):
        string = "String 1: {}, String 2: {}, String 3: {}"\
            .format(self.get_string1(), self.get_string2(), self.get_string3())
        return string

# ------------- CLIENT --------------------------------------------------

# Create 4 TripleString objects


triple_string_num_1 = TripleString("hello", "h", "")

print(triple_string_num_1.get_string1(), triple_string_num_1.get_string2(), triple_string_num_1.get_string3())
print(triple_string_num_1.to_string())

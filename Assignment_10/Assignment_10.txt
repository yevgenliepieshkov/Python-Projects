class Student:
    # class ("static") members and intended constants
    DEFAULT_NAME = "zz-error"
    DEFAULT_POINTS = 0
    MAX_POINTS = 30
    SORT_BY_FIRST = 88
    SORT_BY_LAST = 98
    SORT_BY_POINTS = 108
    sort_key = SORT_BY_LAST

    # initializer ("constructor") method -------------------
    def __init__(self,
                 last=DEFAULT_NAME,
                 first=DEFAULT_NAME,
                 points=DEFAULT_POINTS):
        # instance attributes
        if (not self.set_last_name(last)):
            self.last_name = Student.DEFAULT_NAME
        if (not self.set_first_name(first)):
            self.first_name = Student.DEFAULT_NAME
        if (not self.set_points(points)):
            self.total_points = Student.DEFAULT_POINTS

    # mutator ("set") methods -------------------------------
    def set_last_name(self, last):
        if not self.valid_string(last):
            return False
        # else
        self.last_name = last
        return True

    def set_first_name(self, first):
        if not self.valid_string(first):
            return False
        # else
        self.first_name = first
        return True

    def set_points(self, points):
        if not self.valid_points(points):
            return False
        # else
        self.total_points = points
        return True

    # accessor ("get") methods -------------------------------
    def get_last_name(self):
        return self.last_name

    def get_first_name(self):
        return self.first_name

    def get_total_points(self):
        return self.total_points

    # output method  ----------------------------------------
    def display(self, client_intro_str="--- STUDENT DATA ---"):
        print(client_intro_str + str(self))

    # standard python stringizer ------------------------
    def __str__(self):
        return self.to_string()

    # instance helpers -------------------------------
    def to_string(self, optional_title=" ---------- "):
        ret_str = ((optional_title
                    + "\n    name: {}, {}"
                    + "\n    total points: {}.").
                   format(self.last_name, self.first_name,
                          self.total_points))
        return ret_str

    # static/class methods -----------------------------------
    @classmethod
    def compare_two_students(cls, first_stud, second_stud):
        if cls.get_sort_key() == cls.SORT_BY_FIRST:
            return cls.compare_strings_ignore_case(
                first_stud.get_first_name(), second_stud.get_first_name())
        if cls.get_sort_key() == cls.SORT_BY_LAST:
            return cls.compare_strings_ignore_case(
                first_stud.get_last_name(), second_stud.get_last_name())
        if cls.get_sort_key() == cls. SORT_BY_POINTS:
            return first_stud.get_total_points() - second_stud.get_total_points()

    @staticmethod
    def valid_string(test_str):
        if (len(test_str) > 0) and test_str[0].isalpha():
            return True
        return False

    @classmethod
    def valid_points(cls, test_points):
        if 0 <= test_points <= cls.MAX_POINTS:
            return False
        else:
            return True

    @staticmethod
    def compare_strings_ignore_case(first_string, second_string):
        """ returns -1 if first < second, lexicographically,
           +1 if first > second, and 0 if same
           this particular version based on last name only
           (case insensitive) """

        fst_upper = first_string.upper()
        scnd_upper = second_string.upper()
        if fst_upper < scnd_upper:
            return -1
        # else if
        if fst_upper > scnd_upper:
            return 1
        # else
        return 0

    @classmethod
    def set_sort_key(cls, key):
        if key is cls.SORT_BY_LAST or cls.SORT_BY_FIRST or cls.SORT_BY_POINTS:
            cls.sort_key = key
            return True
        else:
            print("Invalid sort key")
            return False

    @classmethod
    def get_sort_key(cls):
        return cls.sort_key


class StudentArrayUtilities:

    MAX_STUDENTS = 20
    DEFAULT_SIZE = 0
    NOT_FOUND = -1

    def __init__(self):
        self.the_array = []
        self.num_students = StudentArrayUtilities.DEFAULT_SIZE

    def add_student(self, stud):

        if self.num_students < self.MAX_STUDENTS:
            self.the_array.append(stud)
            self.num_students += 1
            return True
        else:
            return False

    def remove_student(self):

        if self.num_students > self.DEFAULT_SIZE:
            self.num_students -= 1
            return self.the_array.pop()
        else:
            return None

    def array_sort(self):

        for k in range(self.num_students):

            if not self.float_largest_to_top(self.num_students-k):
                return

    def float_largest_to_top(self, top):

        changed = False

        for k in range(top-1):

            if Student.compare_two_students(self.the_array[k],
                                            self.the_array[k+1]) > self.DEFAULT_SIZE:
                self.the_array[k], self.the_array[k + 1] \
                    = self.the_array[k + 1], self.the_array[k]
                changed = True

        return changed

    def __str__(self):
        return self.to_string()

    def to_string(self, optional_title="--- The Students ---:\n"):

        ret_val = optional_title + "\n"

        for student in self.the_array:
            ret_val = ret_val + str(student) + "\n"

        return ret_val

    def get_median_destructive(self):
        temp = Student.get_sort_key()
        Student.set_sort_key(Student.SORT_BY_POINTS)
        self.array_sort()

        if self.num_students <= self.DEFAULT_SIZE:
            Student.set_sort_key(temp)
            return 0

        if self.num_students % 2 == self.DEFAULT_SIZE:
            Student.set_sort_key(temp)
            half = int(self.num_students/2)
            result = (self.the_array[half-1].get_total_points()
                      + self.the_array[half].get_total_points())/2
            return result

        if self.num_students % 2 > self.DEFAULT_SIZE:
            i = int((self.num_students / 2) - 0.5)
            Student.set_sort_key(temp)
            return self.the_array[i].get_total_points()

# client --------------------------------------------

# instantiate some students, one with an illegal name ...


my_class = \
   [
    Student("smith","fred", 95),
    Student("bauer","jack",123),
    Student("jacobs","carrie", 195),  Student("renquist","abe",148),
    Student("3ackson","trevor", 108),  Student("perry","fred",225),
    Student("loceff","fred", 44),  Student("stollings","pamela",452),
    Student("charters","rodney", 295),  Student("cassar","john",321)
   ]

array_size = len(my_class)

# instantiate an SAU object
my_studs = StudentArrayUtilities()

# we can add students manually and individually
my_studs.add_student( Student( "bartman", "petra", 102 ) )
my_studs.add_student( Student( "charters", "rodney", 295 ) )

# if we happen to have an array available, we can add students in loop
for k in range(array_size):
   my_studs.add_student(my_class[k])

print( "Before sorting using str:" + str(my_studs) )
print( "Before sorting using to_string():" + my_studs.to_string() )
my_studs.array_sort()
print( "After default sort (LAST):" + str(my_studs) )

Student.set_sort_key(Student.SORT_BY_FIRST)
my_studs.array_sort()
print( "After dsort by FIRST:" + str(my_studs) )

# test median
med = my_studs.get_median_destructive()
print( "Median of even class =", med)
if Student.get_sort_key() == Student.SORT_BY_FIRST:
   print( "Successfully preserved sort key." )
else:
   print( " ** problem **" )

# various tests of removing and adding too many students
for k in range(100):
   student = my_studs.remove_student()
   if student != None:
      print( "Removed " + str(student) )
   else:
      print( "Empty after", k, "removes." )
      break

for k in range(100):
   if not my_studs.add_student(Student("first", "last", 22)):
      print( "Full after", k, "adds."  )
      break
   else:
      print( "Added(first, last, 22)" )

p = ""
for k in my_studs.the_array:
    k.set_last_name("last")
    p = p + " " + k.get_last_name() + " " + str(k.get_total_points()) + "\n"

print(p)
print(my_studs.num_students)

for k in range(my_studs.num_students):
    if len(my_class) > 0:
        my_studs.remove_student()
        my_studs.add_student(my_class.pop())
        print(my_studs.the_array[my_studs.num_students-1])

if not my_studs.remove_student():
    print("no more studs in array")

print(my_studs.num_students)
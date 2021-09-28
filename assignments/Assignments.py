from Student import Student


def gol_hash(s):
    total = 0
    for char in s:
        if char != '':
            total += ord(char)
    return total


def hash_object(s, method_one=False):
    """
    * Approach One using the id
    * This returns the address of the instance S(which is an int).
    * Therefore, the hashes will only match if it is the same instance when comparing
    That is
    a = Object()
    b = a
    id(a) == id(b) # This will return true
    Any other instance will be false, even if the variables of the class match-up
    """
    if method_one:
        return id(s)
    """
    * Approach Two using the variables 
    * This uses the variables to return the hash value
    * Therefore, the hashes will only match if they have the same variables / the combination sum is the same
    """
    return gol_hash(s.get_name()) + s.get_age() + s.get_marks()


def histogram(s):
    counter = dict()
    arr_words = s.split()
    max_word_length = 0
    for word in arr_words:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1
            max_word_length = max(max_word_length, len(word))

    for word in counter:
        temp_word = word + ':'
        temp_value = '*' * counter[word]
        print('{0:<{width}} {1}'.format(temp_word, temp_value, width=max_word_length + 1))


# Histograms example
histogram("Life is so so good")

# Object Hashing example
student_a = Student("Joshua Maina", 23, 123)
student_b = Student("Edith Nekesa", 23, 223)
student_c = student_a
student_d = Student("Joshua Maina", 23, 123)
students = [student_a, student_b, student_c, student_d]
for index, student in enumerate(students, 1):
    print("Students {}".format(index))
    print(student)
    print("Student hash - method 1: {}\n"
          "Student hash - method 2: {}".format(hash_object(student, method_one=True), hash_object(student)))

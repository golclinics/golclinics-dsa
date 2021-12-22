class Person:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

    def __repr__(self):
        return "Person([{0}, {1}, {2}])".format(self.name, self.age, self.location)


people = [
    Person("Dennis", 44, "Nairobi"),
    Person("Mary", 14, "Kisumu"),
    Person("John", 13, "kwale"),
    Person("Ruth", 24, "Mandera"),
    Person("Karen", 32, "Kakuma"),
    Person("Peter", 29, "Isiolo"),
    Person("Peter", 29, "Nakuru"),
    Person("Peter1", 29, "Nakuru"),
    Person("Irene", 7, "nyeri"),
    Person("Mohamud", 21, "voi"),
]

def sort_people(people):

    for i in range(len(people)):
        for j in range(len(people)):
            if people[i].age > people[j].age:
                people[i], people[j] = people[j], people[i]
            if people[i].age == people[j].age and people[i].location > people[j].location:
                people[i], people[j] = people[j], people[i]
            if people[i].age == people[j].age and people[i].location == people[j].location and people[i].name > people[j].name:
                people[i], people[j] = people[j], people[i]
                
    return people

print(sort_people(people))

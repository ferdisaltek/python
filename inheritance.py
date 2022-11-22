
class Person:  #base class ,parent class

    def __init__(self,name ,lastname,age) -> None:
        self.name=name
        self.lastname=lastname
        self.age=age
        print("person nernesi türetildi")

    def intro(self):
        print(self.name, self.lastname, self.age)


class student(Person):
    pass

class teacher(Person):
    pass


p1=Person("ferdi","saltek",33)
p1.intro()

s1=student("ali","veli",49)
s1.intro()
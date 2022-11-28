
class Person:  #base class ,parent class

    def __init__(self,name ,lastname,age) -> None:
        self.name=name
        self.lastname=lastname
        self.age=age
        print("person nernesi türetildi")

    def intro(self):
        print(self.name, self.lastname, self.age)


class student(Person):
    def __init__(self, name, lastname, age,number) -> None:
        super().__init__(name, lastname, age)
        #Person.__init__(self,name ,lastname,age)
        self.number=number
        print("student nesnesi oluşturuldu.")

    def intro(self):
        print(self.name, self.lastname, self.age, self.number)

    def study(self):
        print(f"{self.number} numaralı öğrenci ders çalıyor.")

class teacher(Person):
    def __init__(self, name, lastname, age,branch) -> None:
        super().__init__(name, lastname, age)
        self.branch=branch

    def teach(self):
        print(f"{self.name} isimli öğretmen {self.branch} eğitimi veriyor.")


# p1=Person("ferdi","saltek",33)
# p1.intro()

s1=student("ali","veli",49,550055)
s1.intro()
s1.study()

t1=teacher("asdasd","qweqwe",44,"math")
t1.intro
print(t1.branch)
t1.teach()
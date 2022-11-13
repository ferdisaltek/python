class Person:

    count=0

    #constructor
    def __init__(self,name ,last_name,year) :
        self.name=name
        self.last_name=last_name
        self.year=year
        Person.count+=1
        
    def intro (self):
        return f"benim adim {self.name} ve soyadim {self.last_name}"

    def yas(self):
        return  f"{2022-self.year}"

p1=Person("asdasd","dlfkgjdlfg",1999)
p2=Person("prtoyğr","vblşckvb",2000)


print(p1.intro())
print(p2.yas())

print(Person.count)



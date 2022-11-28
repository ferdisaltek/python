
class NewDict(dict):
    def __repr__(self) -> str:
        print("repr methodu calıştı")
        return super().__repr__()

    def __missing__(self,key):
        print("olmayan key bilgisi isteniyor")

    def __getitem__(self, key) :
        print("bir eleman cagiriyorsunuz")
        return super().__getitem__(key)

    def  __setitem__(self, key,value):
        print("listeye eleman ekleniyor")
        return super().__setitem__(key,value)

    def __contains__(self, __o: object) -> bool:
        return super().__contains__(__o)


data=NewDict({"first":"ferdi","last":"saltek"})
print(data)
print(data["first"])
data["age"]
data["first"]="aliveli"
print(data)
print("age" in data)
print("first" in data)
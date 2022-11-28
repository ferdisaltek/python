class Counter:
    def __init__(self,start,stop) -> None:
        self.start=start
        self.stop=stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start<=self.stop:
            x=self.start
            self.start+=1
            return x
        else:
            raise StopIteration


for i in Counter(10,20):
    print(i)

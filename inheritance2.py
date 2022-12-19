class  Animal:
    def __init__(self) :
        self.num_eyes=2

    def breathe(self):
        print("Inhale ,exhale")


class fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        return super().breathe()
        print("doing this underwater")

    def swim(self):
        print("moving in weter")

nemo=fish()
nemo.breathe


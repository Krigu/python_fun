TORCH_START_VALUE = 15
THING_START_VALUE = 20
INVISIBLE_START_VALUE = 21
FANTASTIC_START_VALUE = 3


class Story:
    heros = ["Heidi", "Fantastic", "Tourch", "Thing", "Invisible"]

    heidi = 0
    fantastic = FANTASTIC_START_VALUE
    torch = TORCH_START_VALUE
    thing = THING_START_VALUE
    invisible = INVISIBLE_START_VALUE

    def act1_scene1(self):
        self.fantastic = 1
        self.invisible = INVISIBLE_START_VALUE
        if self.fantastic == self.invisible:
            self.act1_scene2()
        else:
            self.torch = 4
            print(self.fantastic)
            self.act1_scene2()

    def act1_scene2(self):
        self.thing = THING_START_VALUE
        self.fantastic = 2
        self.act1_scene3()

    def act1_scene3(self):
        if self.thing <= 1:
            self.act1_scene4()
        else:
            self.fantastic = 4
            self.thing -= 1
            self.act1_scene3()

    def act1_scene4(self):
        self.invisible += self.fantastic / 2
        self.torch -= 1
        if self.thing <= self.torch:
            self.act1_scene2()
        else:
            print(self.invisible)
            self.act1_scene3()

    def act2_scene1(self):
        self.torch = 0
        print(self.torch)
        self.torch = TORCH_START_VALUE

        self.act2_scene2()

    def act2_scene2(self):
        if self.torch % 2 == 1:
            print(self.fantastic)
        else:
            self.thing = self.torch / 2
            self.fantastic += 1
            self.torch = self.thing

            if self.fantastic <= 32:
                self.act2_scene2()


Story().act1_scene1()

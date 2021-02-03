class TestJ:
    def __init__(self, number, count):
        self.num = number
        self.count = count
        self.health = 100
        self.speed = 1

    def heals(self):
        self.health += 10

    def hits(self):
        self.health -= 10

    def buff(self):
        self.speed += 10

    def end_buff(self):
        self.speed = 1

class knop():
    def __init__(self):
        self.naam = 'thijs'

knop1 = knop()

lijst = [6,7,8]
lijst.append(knop1)
lijst.remove(lijst[-1])
print(lijst)


class weapons:
    def __init__(self,damage,speed,prim_attack,seco_attack,pressence):
        self.damage = int(damage)
        self.speed = int(speed)
        self.prim_attack = str(prim_attack)
        self.seco_attack = str(seco_attack)
        self.pressence = int(pressence)

club = weapons(30, 0, "impact", "none", 15)
short_sword = weapons(40, 15, "thrust", "cut", 20)
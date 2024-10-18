class weapons:
    def __init__(self,Damage,Speed,Prim_attack,Seco_attack,Pressence):
        self.Damage = int(Damage)
        self.Speed = int(Speed)
        self.Prim_attack = str(Prim_attack)
        self.Seco_attack = str(Seco_attack)
        self.Pressence = int(Pressence)

Club = weapons(30, 0, "impact", "none", 15)
Short_sword = weapons(40, 15, "thrust", "cut", 20)

weapon_list = ["Club", "Short_sword"]

def call_weapon(weapon, attribute):
    attri = attribute
    if weapon in weapon_list:
        weapon2 = globals()[weapon]
        return (weapon2.__getattribute__(attri))
    else:
        return ("Armor not found")
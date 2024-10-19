class weapons:
    def __init__(self,Damage,Speed,Prim_attack,Seco_attack,Pressence):
        self.Damage = int(Damage)
        self.Speed = int(Speed)
        self.Prim_attack = str(Prim_attack)
        self.Seco_attack = str(Seco_attack)
        self.Pressence = int(Pressence)

C = "Cut"
I = "Impact"
T = "Thrust"
N = "None"

Bastard_sword = weapons(70,-30,C,I,25)
Battle_axe = weapons(70,-30,C,I,25)
Broadsword = weapons(55,-5,C,N,25)
Cavalry_lance = weapons(80,-30,T,N,25)
Cestus = weapons(25,10,T,C,15)
Chain = weapons(25,0,I,N,15)
Club = weapons(30,0,I,N,15)
Dagger = weapons(30,20,T,C,15)
Flail = weapons(40,0,I,N,15)
Foil = weapons(35,15,I,N,20)
Gladiators_net = weapons(5,0,I,C,15)
Great_warhammer = weapons(70,-35,I,N,20)
Halberd = weapons(60,-15,C,I,20)
Hand_axe = weapons(45,0,C,N,15)
Harpoon = weapons(35,-5,T,N,15)
Heavy_battle_mace = weapons(60,-15,I,N,15)
Hook = weapons(30,10,T,N,15)
Javelin = weapons(35,5,T,N,20)
Lance = weapons(40,5,T,N,25)
Lage_multi_headed_mace = weapons(80,-50,I,N,20)
Lasso = weapons(5,10,I,N,20)
Long_sword = weapons(50,0,C,N,25)
Mace = weapons(40,0,I,N,15)
Parrying_dagger = weapons(30,15,T,C,20)
Quaterstaff = weapons(30,10,I,N,30)
Rapier = weapons(40,15,T,C,20)
Saber = weapons(45,10,C,T,20)
Scimitar = weapons(50,-5,C,N,20)
Scythe = weapons(35,0,C,I,25)
Short_sword = weapons(40,15,T,C,20)
Stiletto = weapons(25,20,T,N,15)
Trident = weapons(40,-10,T,N,15)
Two_handed_axe = weapons(100,-70,C,I,30)
Two_handed_sword = weapons(90,-60,C,I,30)
Unarmed = weapons(10,20,I,N,0)
Warhammer = weapons(50,-5,I,N,15)
Whip = weapons(35,-20,C,I,20)

weapon_list = ["Bastard_sword", "Battle_axe", "Broadsword", "Cavalry_lance", "Cestus", "Chain", "Club", "Dagger", "Flail", "Foil", "Gladiators_net", "Great_warhammer", "Halberd", "Hand_axe", "Harpoon", "Heavy_battle-mace", "Hook", "Javelin", "Lance", "Lage_multi-headed_mace", "Lasso", "Long_sword", "Mace", "Parrying_dagger", "Quaterstaff", "Rapier", "Saber", "Scimitar", "Scythe", "Short_sword", "Stiletto", "Trident", "Two-handed_axe", "Two-handed_sword", "Unarmed", "Warhammer", "Whip"]

def call_weapon(weapon, attribute):
    attri = attribute
    if weapon in weapon_list:
        weapon2 = globals()[weapon]
        return (weapon2.__getattribute__(attri))
    else:
        return ("Weapon not found")
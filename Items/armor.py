class armor:
    def __init__(self,cut,impact,thrust,heat,elec,cold,ener):
        self.cut = int(cut)
        self.impact = int(impact)
        self.thrust = int(thrust)
        self.heat = int(heat)
        self.electric = int(elec)
        self.cold = int(cold)
        self.energy = int(ener)

Padded = armor(1,1,1,1,2,2,0)
Leather = armor(1,0,2,1,2,1,0)
Armored_longcoat = armor(1,0,2,1,2,2,0)
Fur = armor(2,1,2,1,2,2,0)
Complete_leather = armor(1,0,2,1,2,1,0)
Hardened_leather = armor(2,2,2,2,2,2,0)
Studded_leather = armor(3,1,2,2,1,2,0)
Chainmail = armor(4,2,1,2,0,1,0)
Breastplate = armor(4,5,4,1,0,1,0)
Partial_plate = armor(4,3,2,3,2,2,0)
Byrnie = armor(4,3,1,2,0,1,0)
Half_plate = armor(4,4,4,2,0,1,1)
Scale_mail = armor(4,4,4,3,0,3,1)
Light_plate = armor(5,4,5,3,0,3,1)
Full_plate = armor(5,5,5,4,0,4,2)
Full_heavy_plate = armor(6,6,6,4,0,4,2)
Full_field_plate = armor(7,7,7,4,0,4,2)

# for future use, helmets
# part of the armor class or there own class?
# Circlet = (2,2,1,1,1,1,0)
# Forhead_protector = (3,3,3,1,1,2,0)
# Leather_hood = (1,0,2,1,3,1,0)
# Casque = (4,4,3,2,0,3,0)
# Mail_coif = (4,2,1,2,0,1,0)
# Open_helm = (5,4,5,3,0,3,1)
# Great_helm = (5,5,5,4,0,4,2)

armor_list = ["Padded", "Leather", "Armored_longcoat", "Fur", "Complete_leather", "Hardened_leather", "Studded_leather", "Chainmail", "Breastplate", "Partial_plate", "Byrnie", "Half_plate", "Scale_mail", "Light_plate", "Full_plate", "Full_heavy_plate", "Full_field_plate"]

def call_armor(armor, attribute):
    attri = attribute
    if armor in armor_list:
        armor2 = globals()[armor]
        return (armor2.__getattribute__(attri))
    else:
        return ("Armor not found")
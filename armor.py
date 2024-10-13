class armor:
    def __init__(self,cut,impact,thrust,heat,elec,cold,ener):
        self.cut = int(cut)
        self.impact = int(impact)
        self.thrust = int(thrust)
        self.heat = int(heat)
        self.electric = int(elec)
        self.cold = int(cold)
        self.energy = int(ener)

Leather = armor(1,0,2,1,2,1,0)
Half_plate = armor(4,4,4,2,0,1,1)
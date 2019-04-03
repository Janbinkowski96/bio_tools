class Basic_calculations():
    """basis components calculations
    rb = type of operations
    1 = acetate buffer ph calculator
    2 = phosphate buffer ph calculator
    return: Mk acid [mol], Mz base [mol], Cmk acid concentration [mol/dm^3], Cmz base concentration [mol/dm^3] CmK ions concentration [mol/dm^3]"""
    
    def __init__(self, rb, V1, V2, c1, c2):
        self.calc_type = rb
        self. V_1 = V1
        self.V_2 = V2
        self.C_1 = c2
        self.C_2 = c2 
    
    def values(self):
        
        if self.calc_type == 1:
            Mk = (self.V_1 * self.C_1)
            Mz = (self.V_2 * self.C_2)
            Vo = self.V_1 + self.V_2
            Cmk = Mk / Vo
            Cmz = Mz / Vo
            
            return(Vo, Cmk, Cmz)

        elif self.calc_type == 2:
            Mk = (self.V_1 * self.C_1)
            Mz = (self.V_2 * self.C_2)
            Vo = self.V_1 + self.V_2
            Cmk = Mk / Vo
            Cmz = Mz / Vo
            CmK = (2 * Mz + Mk) / Vo
            
            return(Vo, Cmk, Cmz, CmK)

        else:
            input("Error, try again, press ENTER")
    


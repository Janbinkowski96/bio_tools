from math import sqrt, log

class Buffer_pH():

    '''ionic strength correction
    u ionic strenght
    F1 base ionic strenght correction
    F2 acid ionic strenght correction
    '''

    def __init__(self, rb, Cmz, Cmk, CmK):
        
        self.calc_type = rb
        self.C_mz = Cmz
        self.C_mk = Cmk
        self.C_mK = CmK
        

    def ionic_strength(self):

        if self.calc_type == 1:
            u = (1 ** 2 * self.C_mz + 1 ** 2 * self.C_mz) / 2 
            logf = -(0.51 * 1 ** 2 * sqrt(u)) / (1 + sqrt(u))
            t = 1 - abs(logf)
            r = 10 ** t
            F = r * 0.1
            return(u, F)

        elif self.calc_type == 2:
            u = (4 * self.C_mz + self.C_mk + self.C_mK) / 2
            logf1 = -((0.51 * 4 * sqrt(u)) / (1 + sqrt(u)))
            t1 = 1 - abs(logf1)
            r1 = 10 ** t1
            F1 = r1 * 0.1

            logf2 = -((0.51 * sqrt(u)) / (1 + sqrt(u))) 
            t2 = 1 - abs(logf2)
            r2 = 10 ** t2
            F2 = r2 * 0.1
            return(u, F1, F2)
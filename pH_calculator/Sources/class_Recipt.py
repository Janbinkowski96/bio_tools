class Solutions_recipt():

    def count_recipt_acetate(rb, czyu, V, C, pH, pKao ):
        from math import sqrt

        if czyu == "T":

            o = pH - pKao
            logz = 10 ** o # CH3COO-/Ch3COOH
            Cs = logz 
            Ck = 1
            Csp = (Cs / (Cs + Ck)) * C 
            
            u2 = (1 ** 2 * Csp + 1 ** 2 * Csp) / 2 
            f = -((0.51 * 1 * sqrt(u2)) / (1 + sqrt(u2))) 
            t1 = 1 - abs(f)
            r1 = 10 ** t1
            F1 = r1 * 0.1 
            
            Cs2 = logz / F1 
            Ck2 = 1 
            
            Cso = (Cs2 / (Cs2 + Ck2)) * C 
            Cko = (Ck2 / (Cs2 + Ck2)) * C
            Mcso = Cso * V 
            Mcko = Cko * V
            u = (Cso + Cso) / 2

            print("\nTo prepare, you need to use:")
            print("basic component [mol]: ", round(Mcso,3))
            print("acid component [mol]: ", round(Mcko,3))
            print("fill with water to volume [dm3]", V)
            print("ionic strength: ", round(u,3))

        elif czyu == "N":
            o = pH - pKao
            logz = 10 ** o # wartość CH3COO-/Ch3COOH
            Cs = logz  
            Ck = 1
            Cso = (Cs / (Cs + Ck)) * C
            Cko = (Ck / (Cs + Ck)) * C
            Mcso = Cso * V
            Mcko = Cko * V

            print("\nTo prepare buffer with specified parameters, you need to use:")
            print("basic component [mol]: ", round(Mcso, 3))
            print("acid component [mol]: ", round(Mcko, 3))
            print("fill with water to volume [dm3]", V)

        return(Mcso, Mcko)

    def count_recipt_fosfotate(V, C, pH, czyu, pKao, pK):
        from math import sqrt

        if czyu == "T":
            
            o = pH - pK # log_x = Y <> 10^y = x
            logz = 10 ** o #  HPO42-/H2PO4-
            Cs = logz 
            Ck = 1

            Csp = (Cs / (Cs + Ck)) * C 
            Ckp = (Ck / (Cs + Ck)) * C

            u = ((2 ** 2 * Csp) + (1 ** 2 * Ckp) + (2 * Csp + Ckp)) / 2  
        
            logf1 = -((0.51 * 2 ** 2 * sqrt(u)) / (1 + sqrt(u)))
            t1 = 1 - abs(logf1)
            r1 = 10 ** t1
            F1 = r1 * 0.1

            logf2 = -((0.51 * 1 * sqrt(u)) / (1 + sqrt(u))) 
            t2 = 1 - abs(logf2)
            r2 = 10 ** t2
            F2 = r2 * 0.1

            Cs2 = logz / F1
            Ck2 = 1 / F2
            dz = Cs2 / Ck2
            
            Cso = (dz / (dz + 1)) * C 
            Cko = (1 / (dz + 1)) * C 
    
            Mcso = Cso * V
            Mcko = Cko * V
            UO = (4 * Cso + Cko + (2 * Cso + Cko)) / 2

            print("\nTo prepare buffer with specified parameters, you need to use:")
            print("basic component {} [mol] HPO42-".format(round(Mcso, 3)))
            print("acid component {} mol H2PO4-".format(round(Mcko, 3)))
            print("ionic strength: ", round(UO, 3))
            print("fill with water to volume {} [dm3]".format(V))
        
        if czyu == "N":

            o = pH - pK 
            logz = 10 ** o # CH3COO-/Ch3COOH
            Cs = logz 
            Ck = 1 
            Cso = (Cs / (Cs + Ck)) * C
            Cko = (Ck / (Cs + Ck)) * C
            Mcso = Cso * V
            Mcko = Cko * V

            print("\nTo prepare buffer with specified parameters, you need to use:")
            print("basic component {} [mol] HPO42-".format(round(Mcso,3)))
            print("acid component {} mol H2PO4-".format(round(Mcko, 3)))
            print("fill with water to volume {} [dm3]".format(V))
        
        return(Mcso, Mcko)


    

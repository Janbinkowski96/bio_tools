from math import sqrt, log
from Sources.class_Basic_calc import Basic_calculations
from Sources.class_Buffer_pH import Buffer_pH
from Sources.class_Save_results import Save_results 
from Sources.class_Recipt import Solutions_recipt

"""Bellow global variables"""
pKao = 4.76
pK = 7.21
e = 2.718281828459
x = 1
y = 0
z = 0
CmK = 0

print("""
Created by Jan Bińkowski
Ph calculator for buffers solutions 
Calculations based on A. Zgirski & R. Gondko "Obliczenia Biochemiczne"
In case of float numbers use dots instead commas !
--
Gene-Calc Team
www.gene-calc.pl
contact: contact@gene-calc.pl
""")

while x == 1:
    print("""
Menu

>Select type of buffer to count pH:  
    acetate [1]
    phosphate [2]   
    
>select type of buffer to create the recipe:
    acetate [3]
    phosphate [4] """)

    rb = int(input("=> "))
    s_res = input("Would you like to save results in file ? t/n ").upper()
    
    if s_res != "T" and s_res != "N":
        input("Wrong answer, press Enter")
        continue

    if rb == 1: 
        y += 1

        print("\npH calculator for acetate buffer pKa = 4.76")
        print("acid component - Ch3COOH")
        print("base component - Ch3COONa")

        V1 = float(input("volume of acid component [dm^3] "))
        V2 = float(input("volume of base component [dm^3] "))
        c1 = float(input("acid concentration [mol/dm^3] "))
        c2 = float(input("base concentration [mol/dm^3] "))

        basic_calc = Basic_calculations(rb, V1, V2, c1, c2)
        Mk, Mz, Vo, Cmk, Cmz = basic_calc.values()
        
        ionic_class = Buffer_pH(rb, Cmz, Cmk, CmK, CmK)
        u, F = ionic_class.ionic_strength()

        Ph = pKao + log((Cmz * F)/Cmk,10)
        Ph0 = pKao + log(Cmz / Cmk, 10)
        
        print("\nionic strength: ", round(u, 3))
        print("activity coefficient f: ", round(F, 3))
        print("Ph with corrections : ", round(Ph, 3))
        print("Ph: ", round(Ph0, 3))
        
        if s_res == "T":
            Save_results.save_results_ph_calc(y, "pH for acetate buffer pKa = 4.76 ", V1, V2, c1, c2, u, Ph, Ph0)

        ask = input("\nTo close press ENTER, to continue press c: ").upper()
        if ask == "C":
            continue
        else:
            exit()

    elif rb == 2: 
        y += 1

        print("\npH calculator for phosphate buffer pKa = 7.21")
        print("acid component - H2PO4-")
        print("base component - HPO42-")

        V1 = float(input("volume of acid component [dm^3] "))
        V2 = float(input("volume of base component [dm^3] "))
        c1 = float(input("acid concentration [mol/dm^3] "))
        c2 = float(input("base concentration [mol/dm^3] "))

        basic_calc = Basic_calculations(rb, V1, V2, c1, c2)
        Mk, Mz, Vo, Cmk, Cmz, CmK = basic_calc.values()
        
        ionic_class = Buffer_pH(rb, Cmz, Cmk, CmK)
        u, F1, F2 = ionic_class.ionic_strength()
        
        Ph = pK + log(((Cmz * F1)/(Cmk * F2)),10)
        Ph0 = pK + log(Cmz / Cmk, 10)

        print("\nionic strength: ", round(u, 3))
        print("acid {}, base {} and K+ {} ions concetrations [mol/dm^3]".format(round(Cmk, 3), round(Cmz, 3), round(CmK,3)))
        print("base activity coefficient: ", round(F1, 3))
        print("acid activity coefficient: ", round(F2, 3))
        print("Ph with correction: ", round(Ph, 3))
        print("Ph: ", round(Ph0, 3))

        if s_res == "T":
            Save_results.save_results_ph_calc(y,"pH for phosphate buffer pKa = 7.21 ", V1, V2, c1, c2, u, Ph, Ph0)

        ask = input("\nTo close press ENTER, to continue press c: ").upper()
        
        if ask == "C":
            continue
        else:
            exit()

    elif rb == 3: 
        z += 1

        print("\nspecify the acetate buffer parameters pKa = 4.76")
        V = float(input("final volume [dm^3]: "))
        C = float(input("final concentration [mol * dm^-3]: "))
        pH = float(input("pH: "))
        czyu = input("Would you like to consider ionic strength ? t/n: ").upper()
        
        Mcso, Mcko = Solutions_recipt.count_recipt_acetate(rb, czyu, V, C, pH, pKao)
        
        if s_res == "T":
            Save_results.save_results_recipt(z, "acetate ", V, pH, C, Mcso, Mcko)
        
        ask = input("\nTo close press ENTER, to continue press c : ").upper()
                
        if ask == "C":
            continue
        else:
            exit()

    elif rb == 4: 
        z += 1

        print("\nspecify the phosphate buffer parameters pKa = 7.21")
        V = float(input("final volume w [dm^3] : "))
        C = float(input("final concentration [mol * dm^-3]: "))
        pH = float(input("pH: "))
        czyu = input("Would you like to consider ionic strength ? t/n ").upper()

        Mcso, Mcko =Solutions_recipt.count_recipt_fosfotate(V, C, pH, czyu, pKao, pK)
        
        if s_res == "T":
            Save_results.save_results_recipt(z, "phosphate ", V, pH, C, Mcso, Mcko)

        ask = input("\nTo close press ENTER, to continue press C: ").upper()
            
        if ask == "C":
            continue
        else:
            exit()

    else:
        input("\n\tError, try again, press ENTER")
        continue


class Save_results():

    def save_results_ph_calc(y, buff_name, V1, V2, c1, c2, u, Ph, Ph0):
        
        file_1 = open("results_ph_calculator.txt", "a")
        file_1.write("""
        >calculations number {}
        {} buffer prepared using: acid volume {} [dm^3], base volume {} [dm^3], acid concentration {} [dmol/dm^3], base concentration {} [mol/dm^3]
        results:
        ionic strength {}, pH with correction {}, ph {}""".format(y, buff_name, V1, V2, c1, c2, u, Ph, Ph0))
        file_1.close()

    def save_results_recipt(z, buff_name, V, pH, C, Mcso, Mcko):
        
        file_2 = open("results_buffer_recipt.txt", "a")
        file_2.write("""
        >calculations number {}
        {} buffer parameters: volume {} [dm3], pH {}, concentration {} [mol/dm^3]
        buffer recipt: basic component {} [mol], acid component {} [mol], fill water to {}
        """.format(z, buff_name, V, pH, C, Mcso, Mcko, V)) 
        file_2.close()

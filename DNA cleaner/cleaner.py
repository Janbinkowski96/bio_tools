list_of_characters = ["A", "C", "T", "G", "N", "Y", "R", "S", "W", "K", "M", "B", "D", "H", "V"]
res = []
file_in = input("Podaj scieżkę pliku w formacie txt zawierającego sekwencje \n>")

data = open(file_in, "r")
for line in data:
    line = line.upper()
    line = line.replace(" ", "")

    for character in line:
        if character in list_of_characters:
            res.append(character)    
        else:
            continue
print("".join(res))
print("długość sekwencji {}bp".format(len(res)))
data.close()
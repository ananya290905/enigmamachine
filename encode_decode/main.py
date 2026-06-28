import random 
from rotor import Rotor
from reflector import Reflector

# configure the plugboard settings here, you can make upto 10 letter pairings
plugboard = {
    "A" : "Q",
    "S" : "W",
    "D" : "E",
    "F" : "R",
    "G" : "T",
    "H" : "Y",
    "J" : "U",
    "K" : "I",
    "L" : "O",
    "Z" : "X"
}


for k, v in list(plugboard.items()):
    plugboard[v] = k
# create 5 rotors
rotor_string_1 = "ZUYWXHVJCDFLGENBOMPASQRTKI"
rotor_string_2 = "PWMEHUQZTLDXVISGBOFYRKACNJ"
rotor_string_3 = "KYVRQDXGOHEBPTFJZWMLSUAINC"
rotor_string_4 = "LNBPWQIKHFAYGEOVCMXJSZRDTU"
rotor_string_5 = "LKVUYMBGQCEPNJOZXSTARWIFHD"

r_1 = Rotor(rotor_string_1)
r_2 = Rotor(rotor_string_2)
r_3 = Rotor(rotor_string_3)
ref = Reflector()


def encodeInput(input_string: str, rotor_1, rotor_2, rotor_3, reflector):

    output = ""
    # for every character in the string
    for c in input_string.upper():

        current = c
        # map to plugboard letter if it exists
        if current in plugboard:
            current = plugboard[current]

        prev_1 = rotor_1.position
        prev_2 = rotor_2.position

        # rotor 1 first rotates always
        rotor_1.rotate()
        # if rotor 1 made a full round rotor 2 rotates
        if rotor_1.position < prev_1:
            rotor_2.rotate()
        # if rotor 2 made a full round rotor 3 rotates
        if rotor_2.position < prev_2:
            rotor_3.rotate()

        # signal passes through rotor 1
        current = rotor_1.forward(current)
        # signal passes through rotor 2 
        current = rotor_2.forward(current)
        # signal passes through rotor 3 
        current = rotor_3.forward(current)

        # pass through reflector 
        current = reflector.reflect(current)

        # signal passes through rotor 3 
        current = rotor_3.backward(current)
        # signal passes through rotor 2
        current = rotor_2.backward(current)
        # signal passes through rotor 1
        current = rotor_1.backward(current) 

        # map to plugboard letter if exists
        if current in plugboard:
            current = plugboard[current]

        output += current 

    return output

    
print("ENIGMA MACHINE")
starter_input = ""
while starter_input != "3":
    print("Would you like to encode (1), decode (2) or quit (3)?")
    starter_input = input()

    if starter_input == "1":


        print("Please write your message : ")
        cipher = ""
        input_string = input()
        begin = (r_1.position, r_2.position, r_3.position)
        words = input_string.split(" ")
        for w in words:
            temp = encodeInput(w, r_1, r_2, r_3, ref)
            cipher += temp 
            cipher += " "
        print(f"Rotor Starting Positions : {begin} ")
        print(f"Ciphertext : {cipher}")

    elif starter_input == "2":
        print("Please write your ciphertext : ")
        plain = ""
        input_string = input()
        print("Enter your rotor starting positions (separated by commas) : ")
        starters = input()
        start_positions = starters.split(",")
        r_1.position, r_2.position, r_3.position = int (start_positions[0]), int (start_positions[1]), int (start_positions[2])
        
        words = input_string.split(" ")
        for w in words:
            temp = encodeInput(w, r_1, r_2, r_3, ref)
            plain += temp 
            plain += " "
        print(plain)
    elif starter_input == "3":
        break 
    else:
        print("Invalid Action")




# input_string = input()
# # encode
# cipher = encodeInput(input_string)
# print(cipher)
# rotor_1.position, rotor_2.position, rotor_3.position = start_positions
# plain = encodeInput(cipher)
# print(plain)


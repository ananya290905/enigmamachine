class Rotor:

    def __init__(self, wiring):

        self.wiring = [ord(w) - ord('A') for w in wiring]
        self.position = 0


    def forward(self, letter):

        # convert the letter to its index
        index = ord(letter) - ord("A")

        # apply the rotor offset aka what the rotor starts on
        index = (index + self.position) % 26 

        # map to the letter according to the wiring
        output = self.wiring[index]

        # undo the offset
        result = (output - self.position) % 26 

        return chr(result + ord('A'))
    
    def backward(self, letter:str):

        # make backward mapping 
        back = [0] * 26
        for i, p in enumerate(self.wiring):
            back[p] = i

        index = ord(letter) - ord('A')
        index = (index + self.position) % 26
        index = back[index]

        index = (index - self.position) % 26

        return chr(index + ord('A'))
        
    
    def rotate(self):
        self.position = (self.position + 1) % 26

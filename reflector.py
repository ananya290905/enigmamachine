class Reflector:

    def __init__(self):

        self.mapping = {
            "A" : "V",
            "B" : "Q",
            "C" : "G",
            "D" : "H",
            "E" : "N",
            "F" : "W",
            "G" : "C",
            "H" : "D",
            "I" : "X",
            "J" : "P",
            "K" : "Z",
            "L" : "O",
            "M" : "R",
            "N" : "E",
            "O" : "L",
            "P" : "J",
            "Q" : "B",
            "R" : "M",
            "S" : "Y",
            "T" : "U",
            "U" : "T",
            "V" : "A",
            "W" : "F",
            "X" : "I",
            "Y" : "S",
            "Z" : "K"
        }

    def reflect(self, letter: str):
        return self.mapping[letter]
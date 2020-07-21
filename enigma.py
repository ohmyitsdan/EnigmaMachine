class Enigma:
    def __init__(self, reflector, pos1, pos2, pos3, **kwargs):
        rotors = {
        # 1930 Model Enigma I (3 Rotors)
        'rotor1': {'alpha':'EKMFLGDQVZNTOWYHXUSPAIBRCJ','turn':'R'},
        'rotor2': {'alpha':'AJDKSIRUXBLHWTMCQGZNPYFVOE','turn':'D'}, #F
        'rotor3': {'alpha':'BDFHJLCPRTXVZNYEIWGAKMUSQO','turn':'D'}, #W
        # 1938 Model M3 Army
        'rotor4': {'alpha':'ESOVPZJAYQUIRHXLNFTGKDCMWB','turn':'S'}, #K
        'rotor5': {'alpha':'VZBRGITYUPSDNHLXAWMJQOFECK','turn':'V'}} #A
        # Reflectors
        reflectors = {
        'reflectorA': 'EJMZALYXVBWFCRQUONTSPIKHGD',
        'reflectorB': 'YRUHQSLDPXNGOKMIEBFZCWVJAT',
        'reflectorC': 'FVPJIAOYEDRZXWGCTKUQSBNMHL'}

        self.pos1 = rotors.get(pos1)
        self.pos2 = rotors.get(pos2)
        self.pos3 = rotors.get(pos3)
        if kwargs.get('pos4'):
            self.pos4 = rotors.get(kwargs.get('pos4'))
        if kwargs.get('pos5'):
            self.pos5 = rotors.get(kwargs.get('pos5'))
        self.numRotors = 3 + len(kwargs)
        self.ref = reflectors.get(reflector)

    def encode(self, phrase):
        resp = []
        for x in phrase:
            if not x.isalnum():
                resp.append(x)
            else:
                resp.append(self.rotorInput(x))
        return ''.join(resp)

    def rotorInput(self, letter, turnover=True):
        in1 = self.pos1['alpha'][ord(letter.upper())-65]
        in2 = self.pos2['alpha'][ord(in1)-65]
        in3 = self.pos3['alpha'][ord(in2)-65]
        if self.numRotors > 3:
            in4 = self.pos4['alpha'][ord(in3)-65]
            rev = chr(self.ref.find(in4)+65)
            last = chr(self.pos4['alpha'].find(rev)+65)
            if self.numRotors > 4:
                in5 = self.pos5['alpha'][ord(in4)-65]
                rev = chr(self.ref.find(in5)+65)
                out5 = chr(self.pos5['alpha'].find(rev)+65)
                last = chr(self.pos4['alpha'].find(out5)+65)
        else:
            last = chr(self.ref.find(in3)+65)

        out3 = chr(self.pos3['alpha'].find(last)+65)
        out2 = chr(self.pos2['alpha'].find(out3)+65)
        out1 = chr(self.pos1['alpha'].find(out2)+65)
        if turnover:
            if self.numRotors == 5:
               self.turnoverNotch(self.pos1['alpha'], self.pos2['alpha'], self.pos3['alpha'], r4 = self.pos4['alpha'], r5 = self.pos5['alpha'])
            elif self.numRotors == 4:
                self.turnoverNotch(self.pos1['alpha'], self.pos2['alpha'], self.pos3['alpha'], r4 = self.pos4['alpha'])
            else:
                self.turnoverNotch(self.pos1['alpha'], self.pos2['alpha'], self.pos3['alpha'])
        return out1

    def turnoverNotch(self, r1, r2, r3, **kwargs):
        r1out = r1[1:] + r1[0]
        if r1out[0] == self.pos1['turn']:
            r2out = r2[1:] + r2[0]
            if r2out[0] == self.pos2['turn']:
                r3out = r3[1:] + r3[0]
                if self.numRotors > 3:
                    r4 = kwargs.get('r4')
                    if r3out[0] == self.pos3['turn']:
                        r4out = r4[1:] + r4[0]
                        self.pos4['alpha'] = r4out
                        if self.numRotors > 4:
                            r5 = kwargs.get('r5')
                            if r4out[0] == self.pos4['turn']:
                                r5out = r5[1:] + r5[0]
                                self.pos5['alpha'] = r5out
                self.pos3['alpha'] = r3out
            self.pos2['alpha'] = r2out
        self.pos1['alpha'] = r1out
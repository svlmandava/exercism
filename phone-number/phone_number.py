class PhoneNumber:
    def __init__(self, number):
        self.number = number
        self.remove()
        self.valid()
        self.pretty()
        self.area_code = self.number[:3]

    def remove(self):
        self.number = ''.join(x for x in self.number if x.isalnum())
        self.number = self.number[1:] if self.number[0] == '1' else self.number

    def valid(self):
        if len(self.number) != 10:
            raise ValueError(".+")
        if self.number[0] in '01' or self.number[3] in '01':
            raise ValueError(".+")
    
    def pretty(self):
        return "({})-{}-{}".format(self.number[:3], self.number[3:6], self.number[6:])


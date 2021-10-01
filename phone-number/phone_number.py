class PhoneNumber:
    def __init__(self, number):
        self.number = number
        self.remove()
        self.valid()
        self.area_code = self.number[:3]

    def remove(self):
        self.number = ''.join(x for x in self.number if x.isalnum())
        self.number = self.number.removeprefix('1')


    def valid(self):
        if len(self.number) != 10 or self.number[0] in '01' or self.number[3] in '01':
            raise ValueError(".+Please enter the valid phone number.")
    
    def pretty(self):
        return (f"({self.number[:3]})-{self.number[3:6]}-{self.number[6:]}")


#checking the string function output based on program on pg 182 and
#output on pg 184

class Int_set (object):
    def __init__(self):
        self.vals = [3,4]
    def __str__(self):
        if self.vals == []:
            return '{}'
        self.vals.sort()
        result = ''
        for elem in self.vals:
            result += str(elem) + ","
        return f'{{{result[:-1]}}}'

obj = Int_set()
print(str(obj))


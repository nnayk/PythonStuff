#finger exercise pg 184
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

    def union (self,other):
        self.vals.extend(other)
        return self.vals

    def __add__(self, other):
        print('si')
        final = self.union(other)
        return final

obj = Int_set()
other = ['a',9]
result = obj + other
print(result)
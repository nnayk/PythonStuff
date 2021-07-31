#finger exercise pg 194
class Person(object):

    def __init__(self,name):
        self._name = name
        try:
            last_blank = name.rindex(' ')
            self._last_name = name[last_blank+1:]
        except:
            self._last_name = name
        self.birthday = None

    def get_name(self):
        return self._name

    def __str__(self):
        return self._name

class Politician(Person):
    def __init__(self,name,party):
        super().__init__(name)
        self._party = party

    def get_party (self):
        return self._party

    def might_agree(self,other):
        return self._party == other._party or (self._party == None or other._party == None)

pol1 = Politician("Donald Trump","Republican")
pol2 = Politician("Joe Biden","Democrat")
print(f"The claim that \"{pol1._name}\" and \"{pol2._name}\" may agree is {pol1.might_agree(pol2)}.")

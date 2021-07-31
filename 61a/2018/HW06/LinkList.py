#NextFib
class Link:
    empty=()

    def __init__(self,start,rest=empty):
        assert rest is Link.empty or isinstance(rest,Link)
        self.first=start
        self.rest=rest

    #def next(self):
    #    self.rest.rest=self.rest.
    def __repr__(self):
        if self.rest:
            rest_str=","+repr(self.rest)
        else:
            rest_str=''
        return "Link({0}{1})".format(self.first,rest_str)

    def __str__(self):
        stri='<'
        while self.rest:
             stri+=str(self.first)+","
             self=self.rest
        return stri+str(self.first)+">"
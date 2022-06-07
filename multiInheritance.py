class father:
    def surename(self):
        self.sure_name = "last"
        return self.sure_name

class mother:
    def medianname(self):
        self.median_name = "median"
        return self.median_name

class child(father,mother):
    def name(self):
        print("first",self.medianname(),self.surename())


obj = child()
obj.name()
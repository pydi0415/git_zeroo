class pfaculty:
    def assign(self,id,na):
        self.idno=id
        self.name=na
    def display(self):
        print(self.idno)
        print(self.name)
pr=pfaculty()
pr.assign(101,"prasu")
pr.display()
p=pfaculty()
p.assign(102,"prabha")
p.display()

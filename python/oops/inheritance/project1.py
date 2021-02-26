class Employee():
    def assign(self,idno,name):
        self.idno=101
        self.name="ravi"
class Developer():
     def project_info(self,pname,manager):
         self.project_name=pname
         self.project_manager=manager
     def display(self):
        #print("Developer Idno:",self.idno)
        #print("Developer Nmae:",self.name)
        print("Developer project name:",self.project_name)
        print("Developer manager:",self.project_manager)
d=Developer()
#d.assign(101,"ravi")
d.project_info("hdjhs","venky")
d.display()


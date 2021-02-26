# class A:
#     def show(self):
#         print("iam prabhakar")
# class B(A):
#     def __init__(self):
#         print("iam from ap")
# b=B()
# b=A()
#
# b=B()
# b.show()
#in above example class A constructor is inherited to class B.
#print("----------------------------------")
class Employee:
    @staticmethod
    def show():
     print("iam prabhakar")
class Developer(Employee):
    def __init__(self):
        print("iam from ap")
Developer()
Developer.show()
#Employee.show()
#in the above example Employee class is inherited by developer class.
print("-----------------------------------")






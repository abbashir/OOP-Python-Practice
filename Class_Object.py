class Student:
    name = "abdul bashir"

    def profile(self, age, address):
        print(self.name, age, address)
        return 0

    def __init__(self):
        print("this is constructor")


std1 = Student()
std2 = Student()

print(std1.profile(25, "Rajshahi"))
print(std2.profile(30, "Dhaka"))

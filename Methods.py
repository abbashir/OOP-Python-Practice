class Student:
    roll = ""
    gpa = ""

    def set_values(self, r, g):
        self.roll = r
        self.gpa = g

    def get_values(self):
        print(f"Roll is {self.roll} and GPA is {self.gpa}")


rahim = Student()
rahim.set_values(101, 3.50)
rahim.get_values()

korim = Student()
korim.set_values(102, 3.70)
korim.get_values()

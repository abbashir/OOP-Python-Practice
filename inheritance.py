class Phone:
    ram = 8
    processor = ""

    def camera(self):
        print("Call Camera")


class Samsung(Phone):
    def rom(self):
        print(f"Rom is 128 and Ram is {Phone.ram}")


samsung = Samsung()
samsung.rom()
samsung.camera()

class Phone:
    def body_shape(self):
        print("i am in Phone class")


class Samsung(Phone):
    def body_shape(self):
        # Phone.body_shape(None)
        print("i am in Samsung class")


sam = Samsung()
sam.body_shape()

class Bird:
    def __init__(self, name):
        self.name = name
        self.eggs = 0

    def fly(self):
        return "I can fly!"

    def countEggs(self):
        return self.eggs

    def layEgg(self):
        self.eggs += 1

    def __repr__(self):
        if self.eggs == 1:
            return "{} has {} egg".format(self.name, str(self.eggs))
        else:
            return "{} has {} eggs".format(self.name, str(self.eggs))


class Penguin(Bird):
    def fly(self):
        return "No flying for me."

    def swim(self):
        return "I can swim!"


class MessengerBird(Bird):
    def __init__(self, name, message=""):
        self.name = name
        self.message = message
        self.eggs = 0

    def deliverMessage(self):
        return self.message

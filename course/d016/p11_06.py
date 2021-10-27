class Car:
    color = ""
    speed = 0
    count = 0

    def __init__(self, color="red", speed=0):
        self.color = color
        self.speed = speed
        Car.count += 1

    def upSpeed(self, value):
        self.speed += value
        self.count += 1

    def downSpeed(self, value):
        self.speed -= value


myCar1 = Car(15, "adsfa")
myCar2 = Car("hello", 10)
myCar2.upSpeed(100)
for i in {myCar1, myCar2, Car}:
    print(f"{i}'s color is {i.color}, speed is {i.speed}, count is {i.count}")

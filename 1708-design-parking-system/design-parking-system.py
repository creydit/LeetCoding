class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.var1=big
        self.var2=medium
        self.var3=small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.var1 >= 1:
                self.var1 -= 1
                return True
            else:
                return False
        elif carType == 2:
            if self.var2 >= 1:
                self.var2 -= 1
                return True
            else:
                return False
        else:
            if self.var3 >= 1:
                self.var3 -= 1
                return True
            else:
                return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
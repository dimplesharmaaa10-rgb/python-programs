class transport:
    def __init__(self,type):
        self.type = input("Enter the type of transport: ")
    def show(self):
        print("Type of transport is:", self.type)
class bus(transport):
    def __init__(self, type, seatno,source,destination):
        super().__init__(type)
        self.seatno = input("Enter the seat number: ")
        self.source = input("Enter the source: ")
        self.destination = input("Enter the destination: ")
    def show(self):
        super().show()
        print("Seat number is:", self.seatno)
        print("Source is:", self.source)
        print("Destination is:", self.destination)
class boat(transport):
    def __init__(self, type, capacity,source,destination):
        super().__init__(type)
        self.capacity = input("Enter the capacity: ")
        self.source = input("Enter the source: ")
        self.destination = input("Enter the destination: ")
    def show(self):
        super().show()
        print("Capacity is:", self.capacity)
        print("Source is:", self.source)
        print("Destination is:", self.destination)
obj1 = bus("Road transport", 10, "kolkata", "mumbai")
obj2 = bus("Road transport", 20, "delhi", "chennai")
obj3 = boat("Water transport", 100, "kolkata", "mumbai")
obj4 = boat("Water transport", 200, "delhi", "chennai")
obj1.show()
obj2.show()
obj3.show()
obj4.show()
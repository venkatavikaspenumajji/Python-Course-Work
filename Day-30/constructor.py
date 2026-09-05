class Flipkart:
    products = {'shirts':1000,'handbag':2000,'pants':3000}
    discount = 30

    @classmethod
    def display(cls):
        print(cls.products)

    def userinfo(self,name,phone,address):
        self.name = name
        self.phone = phone
        self.address = address
        print(f"Hello {self.name}, Welcome to the Flipkart")


    @staticmethod  #helper function
    def displaydiscount():
        print(f"{Flipkart.discount}% is going to provide discount")

vikas = Flipkart()
vikas.userinfo('vikas',9704224688,'hyd')
vikas.display()
vikas.displaydiscount()

bharat = Flipkart()
bharat.userinfo('bharat',9925357291,'che')
bharat.display()
bharat.displaydiscount()

ganesh = Flipkart()
ganesh.userinfo('ganesh',6282965272,'ban')
ganesh.display()
ganesh.displaydiscount()

print(vikas.products)
print(vikas.name)
Flipkart.displaydiscount()
Flipkart.display()
print(Flipkart.products)






class Flipkart:
    def __init__(self,name,phone):
     self.name = name 
     self.phone = phone
     print(f"Hello{self.name},Welcome to the filpkart")
    vikas = Flipkart ('vikas',9704224688)
    bharat = Flipkart ('vikas',9925357291)
    bharat = Flipkart ('vikas',6282965272)

#Encapsulation ex

    class Instagram:

    def __init__(self, username, password):
        self.username = username
        self.__password = password
        self._posts = []

    def getpassword(self):
        return self.__password

    def setpassword(self, newpassword):
        self.__password = newpassword

    @property
    def accesspost(self):
        return self._posts

    @accesspost.setter
    def accesspost(self, newpost):
        self._posts.append(newpost)

    def display(self):
        print(self.username, self.__password, self._posts)


vikas = Instagram("vikas", "vikas@123")

vikas.display()

print(vikas.username)
print(vikas.getpassword())
print(vikas.accesspost)

print(vikas.username)
print(vikas.getpassword())
print(vikas.accesspost)

vikas.username = "Avinash"

vikas.setpassword("Avinash@123")

vikas.accesspost = "sunrise.png"
vikas.accesspost = "bike.png"
vikas.accesspost = "forest.png"

print(vikas.username)
print(vikas.getpassword())
print(vikas.accesspost)
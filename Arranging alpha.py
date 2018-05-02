
class Papu:
    d = []

    def __init__(self):
        self.o = '\nthis program allows user to enter require items and arrange them alphabetically'
        self.p = str(self.o).swapcase()
        print(self.p)
        print("\n")
        self.a = input("Enter how many items you want to arrange")
        for b in range(0, int(self.a), 1):
            self.c = "Enter the name of item " + str(b + 1) + "\n"
            self.r = input(self.c)
            self.d.append(self.r)
        print("\n Alphabetically,")
        print("\n","S.N" ,"" ,"", "Items")
        for e,self.d in enumerate(sorted(self.d)):
            print("\n ", "" ,  e+1, "" ,"" ,    self.d)
n = Papu()




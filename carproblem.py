class car_show_room:

    sgst=5
    cgst=10
    def carcompany(self):
        while True:
            print("1.BMW\n2.Benz")
            self.num=int(input("choose car company"))
            if(self.num==1):
                self.model(self.num)
                break
            elif self.num==2:
                self.model(self.num)
                break
            else:
                print("invalid")

    def model(self,n):
        self.num=n
        d = {"BMW":["ml300","ml400"],"Benz":["gls300","gls100"]}
        if(self.num==1):

            while True:
                print(d["BMW"])
                self.m = input("select model")
                if self.m in d["BMW"]:
                    self.varient()
                    break
                else:
                    print("invalid")
        elif (self.num == 2):

            while True:
                print(d["Benz"])
                self.m = input("select model")
                if self.m in d["Benz"]:
                    self.varient()
                    break
                else:
                    print("invalid")
    def varient(self):
        lis=["petrol","disel"]

        while True:
            print(lis)
            self.var=input("select varient")
            if self.var in lis:
                self.price()
                break
            else:
                print("invalid")
    def price(self):
        d={"ml300":2000000,"ml400":3000000,"gls300":1000000,"gls100":2000000,"petrol":10000,"disel":20000}
        total=d[self.m]+d[self.var]
        total_grand=total+((self.sgst+self.cgst)/100)*total
        print(f"total price={total_grand}")


obj= car_show_room()
obj.carcompany()

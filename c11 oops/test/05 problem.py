from  random import randint

class train:
      
    @staticmethod
    def h():
          print("An indian railways")

    def  __init__(self,trainno):
         self.trainno=trainno
         

    def book(self,fro,to):
        print(f"ticket is booked in {self.trainno} from {fro} to {to}")
    def getstatus(self):
         print(f"trian is succefully started {self.trainno}")
        
    def getfare(self,fro,to):
                print(f"ticket fair is in {self.trainno} from {fro} to {to} is {randint(500,1000)}")


h=train(23456)
h.h()
h.book("abohar","delhi")
h.getstatus()
h.getfare("abohar","delhi")


        

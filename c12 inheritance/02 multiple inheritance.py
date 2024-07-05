class emoployee:
    companye="google"
    def show(self):
        print(f"the name is {self.companye}")


class coder:
     language="python"
     def printlanguage(self):
          print(f"out of all languages here is yours {self.language}")

class programmer(emoployee,coder):
      company="amazon"
      def showlanguage(self):
          print(f"name of the {self.company}")





a=emoployee()
b=programmer()

b.show()
b.printlanguage()
b.showlanguage()



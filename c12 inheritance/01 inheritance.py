class emoployee:
    companye="goodsf"
    def hello(self):
        print(f"the name is {self.companye}")

# class programmer:
#      company="amazon"
#      def hello(self):
#         print(f"the name is {self.name}")

#      def shoelanguage(self):
#        print(f"name of the {self .name}")


class programmer(emoployee):
      company="amazon"
      def shoelanguage(self):
          print(f"name of the {self.company}")





a=emoployee()
p=programmer()
p.shoelanguage()
p.hello()





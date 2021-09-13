from certifi.main import args


class calculator:
    # x = int(input("введите дополнительное число"))
    def plus(self,a,b,*args):
        # z=int(input("put number"))
        for num in args :
            args+=num
        print(a,"+",b,'+',"=",a+b)
    def minus(self,a,b, *args):
        # z=int(input("put number"))
        for num in args :
            args-=num
        print(a, "-", b,'-' ,"=", a - b)
    def multiply(self,a,b,*args):
        # z=int(input("put number"))
        for num in args :
            args*=num
        print(a, "*", b,'*',"=", a * b)
    def divide(self,a,b,*args):
        # z=int(input("put number"))
        for num in args :
            pass
        print(a, "/", b,'/', "=", a / b)

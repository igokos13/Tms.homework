class Math:
    def __init__(self):
        pass
    def addition(self, a:int, b:int):
        print (f'{a} + {b} = {a+b}')
        
    def subtraction (self, a:int, b:int):
        print(f'{a} - {b} = {a - b}')
        
    def multiplication (self, a:int, b:int):
        print(f'{a}*{b} = {a * b}')
        
    def division (self, a:int, b:int):
        if b ==0:
            print ('No zero division!')
        else:
            print(f'{a} / {b} = {a/b}')
            
my_Math = Math()
my_Math.addition (2, 3)
my_Math. subtraction (10, 5)
my_Math.multiplication (5,2)
my_Math.division(6,0)
print(my_Math)
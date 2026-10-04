class Soda:
    def __init__(self, taste:str='' ):
        self.taste = taste
    def __str__(self):
        if self.taste:
            return(f'У вас газировка с {self.taste} вкусом')
        else:
            return(f'У вас обычная газировка')

under_cola = Soda()
print(under_cola)